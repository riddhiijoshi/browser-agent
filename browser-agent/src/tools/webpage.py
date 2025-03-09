import logging
from playwright.sync_api import sync_playwright
from langchain.tools import tool

logger = logging.getLogger(__name__)


@tool
def open_webpage(entity):
    """
    Searches for the product
    Returns the price for the product.
    """

    link = entity.get("link")
    role = entity.get("role")

    logger.info(f"Opening webpage  {link} and searching for: {role}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto(link, timeout=30000)
            page.wait_for_load_state("domcontentloaded")

            page_content = page.content()

            # search for job role
            search_box = page.wait_for_selector(
                "input[placeholder='Search for products, brands and more']",
                timeout=150000,
            )

            page.wait_for_load_state("networkidle")

            if search_box:
                search_box.fill(role)
                search_box.press("Enter")

                logger.info(f"Searched for role: {role}")
                page.wait_for_timeout(15000)

            else:
                logger.warning("No search box found on the page")

            price = page.evaluate(
                """
                () => {
                    // Look for price in window.__INITIAL_STATE__ or similar objects
                    try {
                        // Method 1: Look for price directly in any script containing product data
                        const scripts = document.querySelectorAll('script');
                        for (const script of scripts) {
                            if (script.textContent.includes('"price":') && script.textContent.includes('"mrp":')) {
                                const priceMatch = script.textContent.match(/"price":(\d+)/);
                                if (priceMatch && priceMatch[1]) {
                                    return priceMatch[1];
                                }
                            }
                        }       
                        return null;
                    } catch (e) {
                        console.error(e);
                        return null;
                    }
                }
            """
            )

            return {"price": price}

        except Exception as e:
            logger.error(f"Error accessing {link}: {str(e)}")
            return {
                "price": None,
            }

        finally:
            browser.close()

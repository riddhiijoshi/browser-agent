import json
import logging
from typing import TypedDict
from langchain.tools import tool
from src.llms.anthropic import Anthropic

llm = Anthropic()

logger = logging.getLogger(__name__)


@tool
def extract_product(requirement: str, link: str):
    """
    This function takes in the requirements given by the user and returns the role to be searched for on the webpage.
    """

    logger.info(f" Your requirement : {requirement}")

    PROMPT = f"""
    You are an expert in analyzing the context of requirements. You have been given requirements, 
    and you must identify the what is the user asking to search for, from the given requirement. You must strictly generate a JSON response.

    <requirement>
    {requirement}
    </requirement>

    <link>
    {link}
    </link>

    Role : Everything after the word "Price for" in the requirement.
    Product : Only the product name mentioned after the brand. It should not consider the brand name.
    Sample names of brands - H&M, Zara, The Souled Store, Bonkers.

    <example>
    Example:

    requirement = "Give me the price for The Souled Store Violet Hooded Crop Pullover"

    Your response should be:
    {{
        "link": "Given link",
        "role": "The Souled Store Violet Hooded Crop Pullover",
        "product":"Violet Hooded Crop Pullover",
    }}
    </example>

    Make sure you return the correct action role from <requirement>.
    """

    role = llm.call_llm(PROMPT)

    try:
        entity = json.loads(role.content)

        if "link" not in entity or "role" not in entity:
            raise ValueError("Invalid JSON format: Missing required keys.")

    except (json.JSONDecodeError, ValueError) as e:
        logger.error(f"Invalid JSON response from LLM {entity} adn Error: {str(e)}")
        return {"error": "Invalid response from LLM"}

    return {"entity": entity}

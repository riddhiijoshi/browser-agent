import logging
from langchain.tools import tool
from typing import Tuple

logger = logging.getLogger(__name__)


@tool
def validate_data(price: str, expected_output: Tuple[float, float]):
    """
    Validate if the extracted price falls within the expected price range.
    """

    try:
        extracted_price = float(price)
        min_price, max_price = expected_output
    except ValueError:
        return {"answer": "Validation failed. Invalid price format."}
    except TypeError:
        return {"answer": "Validation failed. Invalid price range format."}

    logger.debug(f"Price extracted from website is  {extracted_price}")
    logger.debug(f"Expected price range is {min_price}-{max_price}")

    if min_price <= extracted_price <= max_price:
        return {
            "answer": f"Validation successful. The product price is : {extracted_price}. It is within the expected range {expected_output}. You can make the purchase. "
        }
    else:
        return {
            "answer": f"Validation Failure. The product price is : {extracted_price}. It is out of the expected range {expected_output}."
        }

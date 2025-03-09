import logging
from langchain.tools import tool
from typing import Dict, List

logger = logging.getLogger(__name__)


@tool
def validate_data(price: str, expected_output: str):
    """
    Validate if the extracted price matches the expected output.
    """

    logger.debug(f"price extracted from website : {price}")
    logger.debug(f"expected_output : {expected_output}")

    if not price or not expected_output:
        return {"answer": "Validation failed. Missing price or expected output."}

    if price == expected_output:
        return {
            "answer": "Validation successful. Extracted price matches expected output."
        }
    else:
        logger.warning(
            f"Validation failed. Expected: {expected_output}, Found: {price}"
        )
        return {"answer": "Failure"}

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

    role : Everything after the "price for" or simialr words in the requirement.
    product : Only the product name mentioned after the brand. It should not consider the brand name.

    Instructions: 
    1. Sample names of brands - H&M, Zara, The Souled Store, Bonkers.
    2. Its crucial that you identify the barnd name. The brand name should always be inside "role" key.

    <example>
    Example:
    requirement = "Give me the price for The Souled Store Violet Hooded Crop Pullover"
    Your response should be:
    {{
        "link": "Given link",
        "role": "The Souled Store Violet Hooded Crop Pullover",
        "product":"Violet Hooded Crop Pullover",
    }}

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

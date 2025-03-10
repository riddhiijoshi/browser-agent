import logging
from langgraph.graph import StateGraph, END

from src.llms.anthropic import Anthropic
from src.dto.state import AgentState
from src.tools.roles import extract_product
from src.tools.webpage import open_webpage
from src.tools.validate import validate_data

logger = logging.getLogger(__name__)


class WorkflowAgent:
    def __init__(self):
        self.model = Anthropic.llm

    @staticmethod
    def create_workflow():
        """
        Pass input price of a product, and 'answer' will be Success if the price matches the expected_ouput price, else 'answer' will be Failed
        """

        workflow = StateGraph(AgentState)

        workflow.add_node("extract_product", extract_product)
        workflow.add_node("open_webpage", open_webpage)
        workflow.add_node("validate", validate_data)

        workflow.set_entry_point("extract_product")
        workflow.add_edge("extract_product", "open_webpage")
        workflow.add_edge("open_webpage", "validate")
        workflow.add_edge("validate", END)

        return workflow.compile()

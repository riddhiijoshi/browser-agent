from typing import Optional, Tuple, TypedDict

from anthropic import BaseModel


# Define state management using LangGraph
class AgentState(TypedDict):
    requirement: str
    expected_output: str
    link: str
    entity: str
    role: str
    status: str
    price: str
    answer: dict


class InputData(BaseModel):
    requirement: str
    expected_output: Tuple[float, float]
    link: str
    entity: Optional[str] = None
    message: Optional[str] = None
    price: Optional[str] = None
    answer: Optional[str] = None

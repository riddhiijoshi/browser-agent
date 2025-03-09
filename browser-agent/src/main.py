import logging

from fastapi import FastAPI
from src.agents.agent import WorkflowAgent
from src.dto.state import InputData

logger = logging.getLogger(__name__)

app = FastAPI()


@app.post("/validate")
def run_workflow(input_data: InputData):

    input_state = input_data.model_dump()
    result_state = WorkflowAgent.create_workflow().invoke(input_state)

    return {"result": result_state}

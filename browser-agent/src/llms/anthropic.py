import os
from langchain_anthropic.chat_models import ChatAnthropic
from langchain_core.messages import HumanMessage
from langchain_core.outputs.llm_result import LLMResult
from dotenv import load_dotenv

load_dotenv()


class Anthropic:
    def __init__(self):
        model = os.getenv("ANTHROPIC_MODEL_NAME")
        anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

        self.llm = ChatAnthropic(
            anthropic_api_key=anthropic_api_key,
            model=model,
            temperature=0,
            max_tokens=4096,
        )

    def call_llm(self, prompt: str) -> LLMResult:
        llm_call = self.llm.invoke([HumanMessage(prompt)])

        return llm_call

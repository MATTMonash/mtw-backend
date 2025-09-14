from abc import ABC, abstractmethod
from typing import Any

from langchain_core.messages import BaseMessage
from langchain_core.tools import BaseTool

from app.graph.state import GraphState


class BaseAgent(ABC):
    """Base class for all specialised agents"""

    def __init__(self, llm, tools: list[BaseTool] = None):
        self.llm = llm
        self.tools = tools or []

    @abstractmethod
    async def process(self, state: GraphState) -> dict[str, Any]:
        """Process the state and return updated state"""
        pass

    def _extract_query(self, messages: list[BaseMessage]) -> str:
        """Extract the latest user query from messages"""
        for message in reversed(messages):
            if message.type == "human":
                return message.content
        return ""

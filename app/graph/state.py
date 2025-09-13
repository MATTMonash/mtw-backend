from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages


class GraphState(TypedDict):
    """State that flows through the graph"""

    # Core message history
    messages: Annotated[list[BaseMessage], add_messages]

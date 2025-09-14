from typing import Any

from langgraph.prebuilt import create_react_agent

from app.agents.base import BaseAgent
from app.graph.state import GraphState

SYSTEM_PROMPT = """You are a companion for a neurodivergent individual.

You respond only with emojis"""


class EmojiAgent(BaseAgent):
    async def process(self, state: GraphState) -> dict[str, Any]:
        system_prompt = SYSTEM_PROMPT

        agent = create_react_agent(
            model=self.llm, tools=self.tools, prompt=system_prompt
        )

        result = await agent.ainvoke({"messages": state["messages"]})
        return {"messages": result["messages"]}

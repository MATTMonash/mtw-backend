from app.agents.emoji import EmojiAgent
from app.graph.state import GraphState
from app.llms.manager import llm_manager


async def emoji_generator_node(state: GraphState) -> GraphState:
    """Emoji generator node"""
    agent = EmojiAgent(llm_manager.get_llm("google"))
    return await agent.process(state)

from langgraph.graph import END, START, StateGraph

from app.graph.nodes import emoji_generator_node
from app.graph.state import GraphState


def create_main_graph():
    """Create the main conversation graph"""
    # Initialise graph
    graph = StateGraph(GraphState)

    # Add nodes
    graph.add_node("emoji_generator", emoji_generator_node)

    # END -> emoji_generator -> END
    graph.add_edge(START, "emoji_generator")
    graph.add_edge("emoji_generator", END)

    final = graph.compile()
    return final


main_graph = create_main_graph()

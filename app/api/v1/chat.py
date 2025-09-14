from fastapi import APIRouter, HTTPException
from langchain_core.messages import AIMessage, HumanMessage

from app.graph.main_graph import main_graph
from app.schemas.chat import ChatRequest

router = APIRouter()


@router.post("")
async def chat(request: ChatRequest):
    """Generic instant response generation"""
    try:
        state = {
            "messages": [HumanMessage(content=request.message)],
        }

        if request.history:
            for msg in request.history:
                if msg.role == "user":
                    state["messages"].insert(0, HumanMessage(content=msg.content))
                else:
                    state["messages"].insert(0, AIMessage(content=msg.content))

        result = await main_graph.ainvoke(state)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

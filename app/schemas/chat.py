from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    timestamp: list[datetime] | None = None


class ChatRequest(BaseModel):
    message: str
    history: list[Message] | None = None


class ChatResponse(BaseModel):
    message: str

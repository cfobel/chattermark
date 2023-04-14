from datetime import datetime
from typing import List

from pydantic import BaseModel


class Message(BaseModel):
    sender: str
    content: str
    timestamp: datetime


class GPTChatSession(BaseModel):
    session_id: str
    messages: List[Message]

    class Config:
        extra = "ignore"  # To ignore any extra fields in the JSON that are not in the Pydantic model

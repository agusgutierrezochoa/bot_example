from pydantic import BaseModel
from typing import Optional


class UserMessage(BaseModel):
    message: str
    user_id: Optional[str] = None


class BotResponse(BaseModel):
    message: str
    metadata: Optional[dict] = None

from fastapi import APIRouter

from schemas.message_schemas import BotResponse, UserMessage


router = APIRouter(
    prefix="/conversation",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=BotResponse)
async def create_message(user_message: UserMessage) -> BotResponse:
    return BotResponse(
        message=str(user_message.message)
    )

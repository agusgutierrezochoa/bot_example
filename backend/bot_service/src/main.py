from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas.create_message_schemas import BotResponse, UserMessage

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/messages/", response_model=BotResponse)
async def create_message(user_message: UserMessage) -> BotResponse:
    return BotResponse(
        message=str(user_message.message)
    )

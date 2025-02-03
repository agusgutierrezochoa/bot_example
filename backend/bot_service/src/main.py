from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core import (
    chatbot_singleton,
    db,
    settings
)
from api.v1_0_0 import bot_api


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.init_db()
    chatbot_singleton.ChatBotSingleton()

    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API for interacting with the chatbot",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bot_api.router)
app.include_router(bot_api.router, prefix="/v1")
app.include_router(bot_api.router, prefix="/latest")

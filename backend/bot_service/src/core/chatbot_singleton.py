import nltk
from chatterbot import ChatBot

from core.settings import (
    MONGO_DATABASE_NAME,
    MONGO_USER_NAME,
    MONGO_PASSWORD
)


nltk.download('punkt_tab')


class ChatBotSingleton:
    """
    Singleton to return just one instance of ChatBot for the whole service.
    """

    _chatbot_instance = None

    def __new__(cls) -> ChatBot:
        if cls._chatbot_instance is None:
            cls._chatbot_instance = ChatBot(
                'MongoBot',
                storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
                database_uri=f'mongodb://{MONGO_USER_NAME}:{MONGO_PASSWORD}@mongo:27017/{MONGO_DATABASE_NAME}'
            )
        return cls._chatbot_instance

from core.chatbot_singleton import ChatBotSingleton
from chatterbot.trainers import ListTrainer


def train_chatbot() -> None:
    instance = ChatBotSingleton()
    trainer = ListTrainer(instance)
    trainer.train(["Who are you?", "I am a chatbot!"])
    print("Training done!")


if __name__ == '__main__':

    train_chatbot()

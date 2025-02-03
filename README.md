# bot_example
A simple bot example


curl -XPOST "http://localhost:8000/latest/conversation/" \
    -H "Content-Type: application/json" \
    -d \
    '{
        "message": "Hello world"
    }' | jq


from core.chatbot_singleton import ChatBotSingleton; response = ChatBotSingleton().get_response("who are you?")

python -m core.train_chatbot

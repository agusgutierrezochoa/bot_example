# bot_example
A simple bot example


curl -XPOST "http://localhost:8000/latest/conversation/" \
    -H "Content-Type: application/json" \
    -d \
    '{
        "message": "Hello world"
    }' | jq
import React, { useState } from "react";
import Box from "@mui/material/Box";
import Grid from  "@mui/material/Grid"

const ChatPrompt = () => {
    const [message, setMessage] = useState("")
    const [chatHistory, setChatHistory] = useState([]);

    const handleSendMessage = async () => {
        if (message.trim()) {
            setMessage("")

            try {
                const response = await fetch("http://localhost:8000/api/messages/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ message: message.trim() }),
                })

                if (!response.ok) {
                    throw new Error("ERROR")
                }

                const apiResponse = await response.json()

                const newMessage = { sender: "User", text: message.trim() };
                const botResponse = { sender: "Chatbot Example", text: apiResponse.message };

                setChatHistory((prev) => [...prev, newMessage, botResponse]);
            } catch(error) {
                console.log("Error fetching bot response: ", error)
                setChatHistory((prev) => [
                    ...prev,
                    { sender: "Chatbot Example", text: "Sorry, something went wrong." }
                ])
            }
        }
    };

    const handleKeyDown = (event) => {
        if (event.key === "Enter") {
            handleSendMessage();
        }
    };

    return (
        <Grid container sx={{ width: '100%' }} style={styles.container}>
            <Grid item xs={12}>
                <Box style={styles.titleContainer}>
                    Chatbot Example
                </Box>
            </Grid>
            <Grid item xs={12}>
                <Box style={styles.promptContainer}>
                    <input
                        type="text"
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        onKeyDown={handleKeyDown}
                        placeholder="Type your message..."
                        style={styles.input}
                    />
                    <button onClick={handleSendMessage} style={styles.button}>
                        Send
                    </button>
                </Box>
            </Grid>
            <Grid item xs={12}>
                <Box style={styles.chatHistoryContainer}>
                    {chatHistory.map((msg, index) => (
                        <div key={index} style={styles.messageHistory}>
                            <strong>{msg.sender}:</strong> {msg.text}
                        </div>
                    ))}
                </Box>
            </Grid>
        </Grid>
    )
};

const styles = {
    container: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#f4f4f4",
    },
    titleContainer: {
        padding: "16px",
        display: 'flex',
        justifyContent: 'center',
        textAlign: 'center',
        border: '1px dashed grey'
    },
    promptContainer: {
        padding: "16px",
        display: "flex",
        justifyContent: "center",
        border: '1px dashed grey'
    },
    input: {
        flex: 1,
        padding: "10px",
        border: "1px solid #ccc",
        borderRadius: "4px",
        fontSize: "16px",
    },
    chatHistoryContainer: {
        padding: "16px",
        border: '1px dashed grey'
    },
    messageHistory: {
        display: "flex"
    }
}

export default ChatPrompt;

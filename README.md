# NexTalk AI

### Intelligent Local AI Chatbot with LangChain Memory

NexTalk AI is an intelligent chatbot built using a Local Large Language Model (LLM). It uses LangChain Memory to remember previous conversations and provide context-aware responses.

## Live Demo

**Try NexTalk AI here:**

https://nextalkai-h6ijp2eryxhnzstjkuqrjn.streamlit.app/

## Project Overview

NexTalk AI allows users to interact with an AI chatbot that understands questions, generates responses, and remembers previous conversations during the active session.

## Features

- Interactive AI chatbot.
- Local LLM integration using Ollama.
- Conversation memory using LangChain.
- Context-aware responses.
- Simple and user-friendly interface.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Ollama | Local LLM Execution |
| Gemma 3 (1B) | Language Model |
| LangChain | LLM Integration |
| LangChain Memory | Conversation History |
| Streamlit | User Interface |

## Project Structure

```text
NexTalk_AI/
│
├── app.py
├── requirements.txt
└── README.md
```

## How It Works

1. User enters a message.
2. LangChain retrieves previous conversation history.
3. The conversation is sent to the local LLM.
4. Gemma 3 generates a response.
5. LangChain updates conversation memory.
6. The response is displayed using Streamlit.

## Memory Implementation

NexTalk AI uses `InMemoryChatMessageHistory` and `RunnableWithMessageHistory` from LangChain.

This allows the chatbot to remember previous messages during the active application session.

Note: Conversation history is temporary and resets when the application restarts.

## Future Enhancements

- Persistent conversation storage.
- Multiple conversation sessions.
- Chat history management.
- Improved chatbot interface.
- Support for additional local LLM models.

## Author

**Devisree T.**

B.Sc. Computer Science with Artificial Intelligence

## Project Tagline

**NexTalk AI – Intelligent Conversations, Powered by Memory.**

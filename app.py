
import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Page Configuration
st.set_page_config(
    page_title="NexTalk AI",
    page_icon="💬",
    layout="centered"
)

# Application Title
st.title("NexTalk AI")
st.caption("Your Intelligent Local AI Chatbot")
st.write("Welcome! Start a conversation with NexTalk AI.")

# Initialize Local LLM
llm = ChatOllama(
    model="gemma3:1b",
    temperature=0.7
)

# Create Chat Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are NexTalk AI, a friendly and helpful assistant. Give clear and simple answers."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Create LLM Chain
chain = prompt | llm

# Conversation Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = InMemoryChatMessageHistory()

# Memory Function
def get_session_history(session_id):
    return st.session_state.chat_history

# Add LangChain Memory
chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# Session ID
session_id = "nextalk_user"

# Display Chat History
for message in st.session_state.chat_history.messages:
    if message.type == "human":
        with st.chat_message("user"):
            st.write(message.content)

    elif message.type == "ai":
        with st.chat_message("assistant"):
            st.write(message.content)

# User Input
user_input = st.chat_input("Message NexTalk AI...")

if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    try:
        with st.chat_message("assistant"):
            with st.spinner("NexTalk AI is thinking..."):

                response = chatbot.invoke(
                    {"input": user_input},
                    config={
                        "configurable": {
                            "session_id": session_id
                        }
                    }
                )

                st.write(response.content)

    except Exception as e:
        st.error("Unable to connect to the local LLM. Please check Ollama.")
        st.error(str(e))

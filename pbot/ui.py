import streamlit as st
import requests

st.set_page_config(page_title="Streamlit Chat Frontend", page_icon="🤖")
st.title("API-Powered Chatbot")

# The URL where your FastAPI backend is running
BACKEND_URL = "http://127.0.0.1:8000/chat"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
if prompt := st.chat_input("Type your question here..."):
    # 1. Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Call the FastAPI Backend
    try:
        with st.spinner("Waiting for backend..."):
            response = requests.post(BACKEND_URL, json={"prompt": prompt})
            response.raise_for_status()
            data = response.json()
            full_response = data.get("response", "Error: No response field found.")
    except Exception as e:
        full_response = f"⚠️ Connection Error: {e}"

    # 3. Display assistant response
    with st.chat_message("assistant"):
        st.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
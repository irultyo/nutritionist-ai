import os
import requests
import streamlit as st

api_base = "https://amused-enjoyed-shrew.ngrok-free.app/v1"


def get_completion(
        prompt):
    messages = [{"role": "user", "content": prompt}]

    data = {
        "messages": messages,
        "mode": "chat",
        "character": "Nutritionist AI"
    }

    response = requests.post(api_base+"/chat/completions", json=data)
    assistant_content = response.json()["choices"][0]["message"]["content"]

    return assistant_content


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Nutritionist AI by Mistral7B")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
user_input = st.chat_input("What would you like to know?")
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response (Assuming your get_completion function returns the response text)
    bot_response = get_completion(user_input)

    # Display bot response in chat message container
    with st.chat_message("assistant"):
        st.markdown(bot_response)

    # Add bot response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response})

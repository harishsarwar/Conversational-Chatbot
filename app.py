import os
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint

# Model setup
repo_id = "microsoft/Phi-3.5-mini-instruct"
api_key = os.getenv("API_KEY")
llm = HuggingFaceEndpoint(
    repo_id=repo_id, max_new_tokens=100,
    temperature=0.7,
    huggingfacehub_api_token=api_key
)

st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]
    st.session_state.last_user_input = ""

# Extract user name if mentioned 
def extract_name(user_input):
    lower_input = user_input.lower()
    if "my name is" in lower_input:
        words = lower_input.split()
        name = words[words.index("is") + 1].capitalize()  # Get the word after "is"
        return name
    return None

# Send user message
def send_message(user_input):
    if user_input.strip() == st.session_state.last_user_input:
        st.warning("You just asked this question!")
        return

    # Extract name if mentioned
    name = extract_name(user_input)
    if name:
        bot_response = f"Hello {name}, nice to meet you!"
    else:
        context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages[-5:]])
        bot_response = llm.invoke(f"{context}\nUser: {user_input}\nAssistant:").strip()

    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.session_state.last_user_input = user_input.strip()

# Display chat history 
for message in st.session_state.messages:
    role = "User" if message["role"] == "user" else "Assistant"
    st.markdown(f"**{role}:** {message['content']}")

# Input field and send button
user_input = st.text_input("You:", placeholder="Type your message...")

if st.button("Send") and user_input.strip():
    send_message(user_input.strip())

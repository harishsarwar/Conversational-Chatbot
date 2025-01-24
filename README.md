# Conversational Q&A Chatbot

A simple chatbot built using Streamlit and the Phi-3.5-mini-instruct model from Hugging Face. The bot engages in a conversation with users and responds based on the context of previous messages.

## Features
- User can chat with the assistant.
- The assistant remembers previous messages and responds contextually.
- Greets users and recognizes if they mention their name using "my name is".

## Requirements
- Python 3.x
- Streamlit
- Langchain (Hugging Face integration)


## Working
Users type messages into the input field.
The assistant responds based on the context of the last 5 messages.
If the user mentions "my name is", the assistant greets them with their name.

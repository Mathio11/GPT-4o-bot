import os
import json
import openai
import streamlit as st
from openai import OpenAI

# Directory and Key Setup
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

# Initialize OpenAI client - this allows easy integration of keys by others
client = OpenAI(api_key=config_data["OPENAI_API_KEY"])

# Steamlit page setup
st.set_page_config(
    page_title="GPT 4o Bot",
    page_icon="💬",
    layout="wide"
)

# Initialization and saving of history
if "chat_hist" not in st.session_state: #session_state is an inbuilt function in streamlit to check the current state of the session
    st.session_state.chat_hist = []

# Page title
st.title("🤖 GPT 4o Bot")

# Chat History Config
for message in st.session_state.chat_hist:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user
user_prompt = st.chat_input("Ask GPT 4o")

if user_prompt:
    # Users message added to chat and displayed 
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_hist.append({"role": "user", "content": user_prompt})  #adding user prompts to the chat history
    

    # Sending users message to GPT and getting back response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Changed from gpt-4 to gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "Take the persona of an expert in all fields and make sure to keep the responses simple and educational"},
            *[{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.chat_hist]  # Pass the full chat history
        ]
    )

    # Extract the GPT response
    gpt_response = response.choices[0].message.content
    st.session_state.chat_hist.append({"role": "assistant", "content": gpt_response})

    # Displaying GPT response
    with st.chat_message("assistant"): #assistant box and its icon
        st.markdown(gpt_response)
            

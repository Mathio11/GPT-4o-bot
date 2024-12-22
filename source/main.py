import os
import json

import openai
import streamlit as st

# Directory and Key Setup
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY  #this repteated variables for easy integration of keys by others


# Steamlit page setup
st.set_page_config(
    page_title="GPT 4o Bot",
    page_icon="💬",
    layout="wide"
)


# Initialization and saving of history
if "chat_hist" not in st.session_state: #session_state is an inbuilt fuction in streamlit to check the current state of the session
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
    st.session_state.chat_hist.append({"role" : "user", 
                                       "content" : user_prompt})  #adding user prompts to the chat history
    
    # Sending users message to GPT and getting back response
    response = openai.Completion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Take the persona of an expert in all fields and make sure to keep the responses simple and educational"},
            *st.session_state.chat_hist
        ]
    )

    gpt_response = response.choices[0].message["content"]
    st.session_state.chat_hist.append({"role": "assistant", "content": gpt_response})


    # Displaying GPT response
    with st.chat_message("assistant"): #assitant box and its icon
        st.markdown(gpt_response)

import streamlit as st
import os 
# from pathlib import Path
# file_dir = Path(__file__).parent

from nodes import planner
from state import query_state

st.set_page_config(
    page_title="SHOPEASE CHATBOT")

st.title("WELCOME TO SHOPEASE CHATBOT ")


# ***************** TAKING USER INPUT *****************
user_input = st.text_input("")
query_state.query = user_input


# ***************** DISPLAYING USER INPUT ****************

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    response = planner(query_state)
    st.write(response.key_themes)
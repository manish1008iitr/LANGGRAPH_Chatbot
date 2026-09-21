import streamlit as st
import os 
# from pathlib import Path
# file_dir = Path(__file__).parent

from src.generator import Response_generator

response_gen = Response_generator()

st.set_page_config(
    page_title="SHOPEASE CHATBOT")

st.title("WELCOME TO SHOPEASE CHATBOT ")


# ***************** TAKING USER INPUT *****************
user_input = st.text_input("")    


# ***************** DISPLAYING USER INPUT ****************

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    response = response_gen.generate_response(user_input)
    st.write(response.key_themes)
    st.write(response.summary)
    st.write(response.sentiment)
    st.write(response.pros)
    st.write(response.cons)



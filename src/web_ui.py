import streamlit as st
from backend_llm import Response_generator

response_gen = Response_generator()

st.set_page_config(
    page_title="LangGraph Chatbot")

st.title("SIMPLE CHATBOT ON UPSC FACTS")


# ***************** TAKING USER INPUT *****************
user_input = st.text_input("")    


# ***************** DISPLAYING USER INPUT ****************

if user_input:
    st.write("You asked:", user_input)
    response = response_gen.generate_response(user_input)
    st.write("Response:", response[-1].content)



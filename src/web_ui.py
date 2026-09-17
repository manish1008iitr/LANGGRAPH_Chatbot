import streamlit as st
import requests

st.set_page_config(
    page_title="LangGraph Chatbot")

st.title("SIMPLE CHATBOT ON UPSC FACTS")


# ***************** TAKING USER INPUT *****************
user_input = st.text_input("Ask me anything about UPSC facts", placeholder="Type your question here...")    


# ***************** DISPLAYING USER INPUT ****************

if user_input:
    st.write("You asked:", user_input)
    response = f"You asked about: {user_input}. I will soon connect you to a LLM agent."
    st.write("Response:", response)

import streamlit as st
import os 
from graph import graph_compiler
graph = graph_compiler()
workflow = graph.get_workflow()

st.set_page_config(
    page_title="SHOPEASE CHATBOT")

st.title("WELCOME TO SHOPEASE CHATBOT ")


# ***************** TAKING USER INPUT *****************
user_input = st.text_input("")
result = workflow.invoke({"query":user_input})
# result = workflow.invoke({"query":user_input})


# ***************** DISPLAYING USER INPUT ****************

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    response = result["main_issue"]
    st.write(response)

from state import ChatState 
from llm_loader import llm
from langchain_core.prompts import PromptTemplate # for prompt generation

#Creating the llm
llm_local = llm()

def prompt_planner(template, query):
    prompt = PromptTemplate.from_template(
        template= template
    )
    formatted_string = prompt.format(text = query)
    return formatted_string

def planner(state:ChatState):
    question = state["query"]
    prompt = prompt_planner("""
    You are a expert in understanding the sentiment of the statement and analyze the text
    And your work is to understand user query and understand the main subject in it. 
    You are strcitly supposed to answer based on the query and not search internet for this
    In you answer choose only among the "product_query", "order_cancellation", "order_status"
    The query is {text}
    """, question)

    response = llm_local.invoke(prompt)
    return {"main_issue": response.content}


    

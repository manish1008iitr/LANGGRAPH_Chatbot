
from state import ChatState 
from llm_loader import llm
from llm_loader import planner_prompt

def planner(state:ChatState):
    question = state["query"]
    prompt = planner_prompt("""
    You are a expert in understanding the sentiment of the statement and analyze the text
    And your work is to understand user query and understand the main subject in it. 
    You are strcitly supposed to answer based on the query and not search internet for this
    In you answer choose only among the "product_query", "order_cancellation", "order_status"
    The query is {question}
    """, question)

    response = llm.invoke(prompt)
    return {"mains_issue":response.content}


    

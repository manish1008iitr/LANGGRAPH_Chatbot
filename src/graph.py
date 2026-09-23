from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages


#Import other function from other pages
from nodes import planner
from state import ChatState


graph = StateGraph(ChatState)
graph.add_node("planner",planner)


# ADD EDGES

graph.add_edge(START, "planner")
graph.add_edge("planner", END)

workflow = graph.compile()
print(workflow.get_graph().print_ascii())
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages


#Import other function from other pages
from nodes_function import planner
from state import ChatState

# class graph_compiler():
# def __init__(self) -> None:
#     pass

def get_workflow():
    graph = StateGraph(ChatState)
        
    # ADD NODES
    graph.add_node("planner", planner)

    # ADD EDGES
    graph.add_edge(START, "planner")
    graph.add_edge("planner", END)
        
    # Compile the graph
    return graph.compile()
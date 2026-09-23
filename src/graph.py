from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated, Literal
from langgraph.graph.message import add_messages


#Import other function from other pages

from state import ChatState

#IMPORTING NODE FUNCTIONS
from nodes_function import planner
from nodes_function import product_query
from nodes_function import order_status
from nodes_function import order_cancellation


# class graph_compiler():
# def __init__(self) -> None:
#     pass

def check_main_issue(state:ChatState) -> Literal["product_query","order_status","order_cancellation"]:
    if state["main_issue"] == "product_query":
        return product_query
    elif state["main_issue"] == "order_status":
        return order_status
    elif state["main_issue"] == "order_cancellation":
        return order_cancellation

def get_workflow():
    graph = StateGraph(ChatState)
        
    # ADD NODES
    graph.add_node("planner", planner)
    graph.add_node("product_query", product_query)
    graph.add_node("order_status", order_status)
    graph.add_node("order_cancellation", order_cancellation)

    # ADD EDGES
    graph.add_edge(START, "planner")
    graph.add_conditional_edges("planner", check_main_issue)
    graph.add_edge("product_query", END)
    graph.add_edge("order_status",END)
    graph.add_edge("order_cancellation", END)
        
    # Compile the graph
    return graph.compile()

# graph = StateGraph(ChatState)
        
#     # ADD NODES
# graph.add_node("planner", planner)
# graph.add_node("product_query", product_query)
# graph.add_node("order_status", order_status)
# graph.add_node("order_cancellation", order_cancellation)

#     # ADD EDGES
# graph.add_edge(START, "planner")
# graph.add_conditional_edges("planner", check_main_issue)
# graph.add_edge("product_query", END)
# graph.add_edge("order_status",END)
# graph.add_edge("order_cancellation", END)
        
#     # Compile the graph
# workflow = graph.compile()

# print(workflow.get_graph().print_ascii())
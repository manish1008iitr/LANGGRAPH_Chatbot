from langgraph.graph import StateGraph
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    query: str
    main_issue: str
    messages:  Annotated[list[str], add_messages]
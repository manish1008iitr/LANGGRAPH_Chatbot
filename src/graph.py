
# Libraries to make langraph 
import langgraph
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field
import dotenv
import os 


import langchain
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama





# ***** SCHEMA **** 
# class Review(TypedDict):
#     key_themes: Annotated[list[str], "Key themes discussed in the review "]
#     summary: Annotated[str, "A breif summary of the review"] 
#             ## LLM will understand that word summary means a summary of the review.  
#     sentiment: Annotated[str, "Overall sentiment of the review (positive, negatice, neutral)"]
#     pros: Annotated[Optional[list[str]], "Optional to give pros"]
#     cons: Annotated[Optional[list[str]], "Optional to give cons"]


class Result(BaseModel):
    key_issue: list[str] = Field(description = "Major issue in the query")
    summary:str = Field(description= "Short summary of query")


def prompt_generator(self, user_input: str):
    self.message = [
            SystemMessage(content="You are a knowledgeable strcutural reviewer who reviews " \
            " the text and give a summary of it. You also add a joyful message in beginning if sentiment is positive" \
            "or a emphathtic message if summary is negative" \
            "Also answer the key themes discussed in the reviews in a list format " \
            "And also provide a brief summary of the review" \
            "Return all of the data in a json format"),
            HumanMessage(content=user_input)    
            ]

def response_generation():
    pass



class Response_generator():
    def __init__(self):
        self.model_name = os.getenv("MODEL_NAME")
        self.chat_model = ChatOllama(
                model = self.model_name, 
                temperature=0.7
            )
        self.structured_model = self.chat_model.with_structured_output(Review)
        self.message = []

    

    def generate_response(self, user_input: str):
        prompt = self.prompt_generator(self.message)
        response = self.structured_model.invoke(user_input)
        return response




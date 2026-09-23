
# Libraries to make langraph 
from langchain_core.prompts import PromptTemplate # for prompt generation

from langchain_groq import ChatGroq
import dotenv
import os 

dotenv.load_dotenv()

#prompt generation fucntion

def llm():
    llm = ChatGroq(
        model=os.environ.get("MODEL_NAME")
    )
    return llm

def planner_prompt(template, query):
    prompt = PromptTemplate.from_template(
        template= template
    )
    formatted_string = prompt.format(text = query)
    return formatted_string

# def generate_response(user_input: str):
#     prompt = planner_prompt(user_input)
#     print(prompt)
#     response = llm.invoke(prompt)
#     print(response.content)




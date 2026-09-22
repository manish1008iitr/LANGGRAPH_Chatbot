
# Libraries to make langraph 

from langchain_groq import ChatGroq
import dotenv
import os 

dotenv.load_dotenv()

#prompt generation fucntion
from tools import planner_prompt

llm = ChatGroq(
    model=os.environ.get("MODEL_NAME")
)

def generate_response(user_input: str):
    prompt = planner_prompt(user_input)
    print(prompt)
    response = llm.invoke(prompt)
    print(response.content)




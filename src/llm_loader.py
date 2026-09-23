
# Libraries to make langraph 
from langchain_groq import ChatGroq
import dotenv
import os 

dotenv.load_dotenv()


def llm():
    llm = ChatGroq(
        model=os.environ.get("MODEL_NAME")
    )
    return llm




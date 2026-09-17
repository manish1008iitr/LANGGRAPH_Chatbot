import langchain
from langchain_ollama import ChatOllama
import dotenv
import os 

key_data = dotenv.load_dotenv()

class Response_generator():
    def __init__(self):
        self.model_name = os.getenv("MODEL_NAME")
        self.chat_model = ChatOllama(
                model = self.model_name, 
                temperature=0.7
            )

    def generate_response(self, user_input: str):
        response = self.chat_model.invoke(user_input)
        return response




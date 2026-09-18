import langchain
from langchain.messages import SystemMessage, HumanMessage, AIMessage
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
        self.message = []

    def prompt_generator(self, user_input: str):
        self.message = [
            SystemMessage(content="You are a knowledgeable assistant that provides accurate and " \
            "concise answers to questions related to UPSC facts. If the relevant " \
            "information is not available, respond with 'I don't know.' Provide the answer "
            "in a clear and concise manner, focusing on the key points."),
            HumanMessage(content=user_input)    
        ]

    def generate_response(self, user_input: str):
        prompt = self.prompt_generator(user_input)
        response = self.chat_model.invoke(self.message)
        self.message.append(AIMessage(content=response.content))
        return self.message




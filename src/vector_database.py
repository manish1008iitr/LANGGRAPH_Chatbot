from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings 
import os 
from pathlib import Path 
vector_db_path = os.path.join(Path(__file__).parent.parent,"data","vector")
EMBEDDING_MODEL = "nomic-embed-text"

def get_embedding_model():
    embedding = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )
    return embedding

def vector_formation(chunks):
    embedding_model = get_embedding_model()
    vector_store = Chroma.from_documents(
        documents = chunks, 
        embedding = embedding_model,
        persist_directory = vector_db_path,
        collection_name = "chatbot collection"
    )

    return vector_store




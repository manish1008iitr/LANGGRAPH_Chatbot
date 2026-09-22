import os 
import pymupdf4llm # converting pdf file into markdown
from pathlib import Path # to ensure that python able to understand the relative path
from langchain_community.document_loaders import CSVLoader # to convert csv into chunks 
from langchain_text_splitters import RecursiveCharacterTextSplitter # to do text splittin of markdown file

script_dir = Path(__file__).parent # file of parent directory

def pdf_to_mark(file_path:str):
    #Conversion into markdown file
    md_text = pymupdf4llm.to_markdown(file_path)
    return md_text

def csv_to_chunk(file_path:str):
    loader = CSVLoader(
        file_path = file_path,
        csv_args={
            "delimiter": ",",
            "quotechar": '"'
        }
    )
    chunks = loader.load()

    return chunks

def chunker_pdf(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,       # The maximum number of characters in each chunk
        chunk_overlap=100,     # The number of characters to overlap between adjacent chunks
        add_start_index=True, # Optional: Includes the chunk's starting position in the original text
    )
    chunks = text_splitter.split_text(text)
    return chunks
    

    
    



import os 
import pymupdf4llm
from pathlib import Path
from langchain_community.document_loaders import CSVLoader
import json
script_dir = Path(__file__).parent

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

    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(chunks_data, json_file, indent=4, ensure_ascii=False)
    print("succesfully converted csv into chunks and saved it")
    

    
    



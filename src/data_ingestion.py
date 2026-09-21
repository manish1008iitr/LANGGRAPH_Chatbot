import os 
import pymupdf4llm
import re
from pathlib import Path
script_dir = Path(__file__).parent

def pdf_to_mark(dir_path:str):

    #Creation of directory 
    raw_data_path = os.path.join(dir_path,"data","processed")
    if not os.path.isdir(raw_data_path):
        os.makedirs(raw_data_path)

    #Conversion into markdown file
    md_text = pymupdf4llm.to_markdown(os.path.join(dir_path,"data","raw","policy.pdf"))

    #Saving markdown file
    filename = script_dir.parent/ "data"/"processed"/"policy_mark.md"
    filename.touch(exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(md_text)
    print("succesfully converted pdf into markdown file and saved it")

def main():
    pdf_to_mark(script_dir.parent)

if __name__ == "__main__":
    main()
    

    
    



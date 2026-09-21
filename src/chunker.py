from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunker_pdf(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,       # The maximum number of characters in each chunk
        chunk_overlap=100,     # The number of characters to overlap between adjacent chunks
        add_start_index=True, # Optional: Includes the chunk's starting position in the original text
    )
    chunks = text_splitter.split_text(text)
    return chunks




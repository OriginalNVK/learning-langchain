from langchain_openai import OpenAIEmbeddings
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma

current_dir = os.path.dirname(os.path.abspath(__file__))
book_path = os.path.join(current_dir, "books", "odyssey.txt")
db_path = os.path.join(current_dir, "db", "chroma_db")

if not os.path.exists(db_path):
    print("Persistent directory does not exist. Initializing vector store...")
    
    if not os.path.exists(book_path):
        raise FileNotFoundError(f"The file {book_path} does not exist. Please check the path.")
    
    # initialize text loader
    text_loader = TextLoader(book_path)
    documents = text_loader.load()
    
    # split documents
    text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    texts = text_splitter.split_documents(documents)
    
    # create embeddings using text-embedding 3 model
    embedding_model = OpenAIEmbeddings(
        model = "text-embedding-3-small"
    )
    
    # storage document embeddings into chroma db
    db_data = Chroma.from_documents(texts, embedding_model, persist_directory=db_path)
else:
    print("Persistent directory already exists. No need to initialize.")
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


current_dir = os.path.dirname(os.path.abspath(__file__))
books_dir = os.path.join(current_dir, "books")
db_dir = os.path.join(current_dir, "db")
db_storage = os.path.join(db_dir, "chroma_db_with_metadata")

if not os.path.exists(db_storage):
    print("Persistent directory does not exist. Initializing vector store...")
    
    if not os.path.exists(books_dir):
        raise FileNotFoundError("Books directory does not exist.")

    book_list = [f for f in os.listdir(books_dir) if f.endswith(".txt")]

    documents = []
    for book in book_list:
        loader = TextLoader(os.path.join(books_dir, book), encoding="utf-8")
        book_contents = loader.load()
        for doc in book_contents:
            doc.metadata = {"Source": book}
            documents.append(doc)
    
    Splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    chunks = Splitter.split_documents(documents)
    
    embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")
    db_data = Chroma.from_documents(
        chunks, embeddings, db_storage
    )
    
else:
    print("Vector store already exists. No need to initialize.")
    
           
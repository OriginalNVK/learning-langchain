import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))    
db_dir = os.path.join(current_dir, "db")
storage_dir = os.path.join(db_dir, "chroma_db_apple")

url = "https://apple.com"

loader = WebBaseLoader(url)
content = loader.load()

text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
docs = text_splitter.split_text(content)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

storage_data = Chroma.from_documents(
    docs, embeddings, storage_dir)

query = "What is the latest news about Apple?"
db = Chroma(embedding_function = embeddings, persist_directory = storage_dir)
retriever = db.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k":3}
)

rel_docs = retriever.invoke(query)

print("Relevant documents: ", rel_docs[0].pages_content)




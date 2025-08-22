import os

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, "db")
storage_directory = os.path.join(db_dir, "chroma_db_with_metadata")

embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")
db = Chroma(embedding_function = embeddings, persist_directory = storage_directory)

def query_vector_store(query, search_type, search_kwargs):
    retriever = db.as_retriever(search_type = search_type, search_kwargs = search_kwargs)
    relevant_docs = retriever.invoke(query)
    if relevant_docs:
        print(f"Relevant documents found: {relevant_docs}")
    else:
        print("No relevant documents found.")

query = "How did juliet die?"

query_vector_store(query, "similarity", {"k":3})
query_vector_store(query, "mmr", {"k": 3, "fetch_k": 5, "lambda_mult": 0.5})
query_vector_store(query, "similarity_score_threshold", {"k":3, "score_threshold": 0.5})


import os
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    SentenceTransformersTokenTextSplitter,
    TextSplitter,
    TokenTextSplitter,
    )
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "romeo_and_juliet.txt")
db_dir = os.path.join(current_dir, "db")

text_loader = TextLoader(file_path)
documents = text_loader.load()  

if not os.path.exists(file_path):
    raise FileNotFoundError("File not found")

def create_vector_store(doc, folder_name):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    db_storage = os.path.join(db_dir, folder_name)
    vector_store = Chroma.from_documents(
        doc, embeddings, db_storage
    )
    
# 1. Sử dụng Character Text Splitter
# Cắt chunk theo độ dài đơn giản
text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
docs = text_splitter.split_documents(documents)
create_vector_store(docs, "chroma_db_char")

# 2. Sử dụng RecursiveCharacterTextSplitter
# Cắt theo đoạn, theo câu, theo từ sử dụng tùy thuộc vào độ giữ nguyên context
# Sử dụng thường xuyên nhất vì bảo đảm ngữ cảnh không bị đứt đoạn
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
docs = text_splitter.split_documents(documents)
create_vector_store(docs, "chroma_db_recursive")

# 3. Sử dụng TokenTextSplitter
# Tách chunk dựa vào tokenize của OpenAI/GPT hoặc HuggingFace
text_splitter = TokenTextSplitter(chunk_size = 1000, chunk_overlap = 200)
docs = text_splitter.split_documents(documents)
create_vector_store(docs, "chroma_db_token")

# 4. Sử dụng SentenceTransformersTokenTextSplitter
# Tách chunk dựa vào sentence và sử dụng mô hình sentence-transformers (HuggingFace)
text_splitter = SentenceTransformersTokenTextSplitter(chunk_size = 1000, chunk_overlap = 200)
docs = text_splitter.split_documents(documents)
create_vector_store(docs, "chroma_db_sentence_transformers")

# 5. Sử dụng TextSplitter
class CustomTextSplitter(TextSplitter):
    def split_text(self, text: str) -> list[str]:
        return text.split("\n\n")  # Split by double newlines
    
text_splitter = CustomTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)
create_vector_store(docs, "chroma_db_custom")

def query_vector_store(query, folder_name):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    persistent_dir = os.path.join(db_dir, folder_name)
    db = Chroma(persistent_directory=persistent_dir, embedding_function=embeddings)
    retrieval = db.as_retriever(
        search_type = "similarity_score_threshold",
        kwargs = { "k": 3, "score_threshold": 0.5}
    )
    
    doc_relevant = retrieval.invoke(query)
    if doc_relevant:
        print(doc_relevant)
    else:
        print("No relevant documents found.")

query = "Tell me who is Romeo and Juliet?"

query_vector_store(query, "chroma_db_char")
query_vector_store(query, "chroma_db_recursive")
query_vector_store(query, "chroma_db_token")
query_vector_store(query, "chroma_db_sentence_transformers")
query_vector_store(query, "chroma_db_custom")
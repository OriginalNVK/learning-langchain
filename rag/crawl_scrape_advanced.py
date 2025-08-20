import os 
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_community.document_loaders import FireCrawlLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, "db")
storage_dir = os.path.join(db_dir, "chroma_db_firecrawl")

embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")
url = "https://apple.com"
api_key = os.getenv("FIRECRAWL_API_KEY")

loader = FireCrawlLoader(url, api_key)
content = loader.load()

text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
docs = text_splitter.split_text(content)

data_storage = Chroma.from_documents(
    docs, embeddings, storage_dir
)

query = "What is the latest news about Apple?"
db = Chroma(embedding_function = embeddings, persist_directory = storage_dir)
retriever = db.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k": 3}
)

rel_docs = retriever.invoke(query)

for doc in rel_docs:
    print(doc.page_content)
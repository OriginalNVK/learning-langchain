import os

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, "db")
storage_dir = os.path.join(db_dir, "chroma_db_with_metadata")

embeddings = OpenAIEmbeddings("text-embedding-3-small")
db = Chroma(embedding_function=embeddings, persist_directory=storage_dir)

retriever = db.as_retriever(
    search_type = "similarity",
    search_kwargs = {
        "k": 5
    }
)

question = "Who is Romeo?"

rel_docs = retriever.invoke(question)

query = "This is some relevant documents to answer the question: " + question  + "\n\nDocuments: " + "\n\n".join([doc.page_content for doc in rel_docs])

model = ChatOpenAI("gpt-4o")

Messages = [
    SystemMessage(content = "You are a professional assistant"),
    HumanMessage(content = query)
]

result = model.invoke(Messages)

print("AI response: " + result.content)


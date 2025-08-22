import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "db", "chroma_db")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = Chroma(persist_directory=db_path, embedding_function=embeddings)

query = "Who is Odysseus's wife?"

retriever = db.as_retriever(
    search_type = "similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.4}
)

documents = retriever.invoke(query)

for i, doc in enumerate(documents, 1):
    print(f"Document {i}: {doc}")
    if doc.metadata:
        print(f"source: {doc.metadata.get('source', 'Unknown')}")
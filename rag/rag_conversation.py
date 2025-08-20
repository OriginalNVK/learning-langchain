import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage 
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain, create_stuff_documents_chain

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, "db")
storage_dir = os.path.join(db_dir, "chroma_db_with_metadata")

embeddings = OpenAIEmbeddings(model = "test-embedding-3-small")
db = Chroma(embedding_function = embeddings, persist_directory = storage_dir)

llm = ChatOpenAI(model = "gpt-4o")

retriever = db.as_retriever(
    search_type = "similarity",
    kwargs = {"k":3}
)

contextualize_q_system_prompt = (
    "Given chat history and the latest user question,"
    "to answer the question need to reference the chat history."
    "Formulate a standalone question can be understood without chat history."
    "Do NOT answer the question, reformulate it if needed"
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
)

history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

system_prompt = (
    "You are an assistant in question-answering task. Use this informations"
    "retrieved from the context to answer the question."
    "If you don't know the correct answer, Just say you don't know"
    "\n\n"
    "{context}"
)

qa_system_prompt = ChatPromptTemplate.from_messages(
    ("system", system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
)

contextualize_qa_system_prompt = create_stuff_documents_chain(
    llm, qa_system_prompt
)

rag_chain = create_retrieval_chain(contextualize_q_prompt, contextualize_qa_system_prompt)

def continual_chat():
    chat_history = []
    while True:
        user_input = input("User: ")
        response = rag_chain.invoke(user_input, chat_history=chat_history)
        print("AI Respose: ", response["answer"])
        chat_history.append(HumanMessage(content = user_input))
        chat_history.append(SystemMessage(content = response["answer"]))

def __main__():
    continual_chat()





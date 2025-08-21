import os
from langchain import hub
from langchain_community.vectorstores import Chroma
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, "..", "..", "rag", "db")
storage_dir = os.path.join(db_dir, "chroma_db_with_metadata")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = Chroma(embedding_function=embeddings, persist_directory=storage_dir)
retriever = db.as_retriever(
    search_type = "similarity",
    search_kwargs = {
        "k": 5
    }
)

llm = ChatOpenAI(model="gpt-4o")

contextualize_q_system_prompt = (
    "Give some information about the user's query and the relevant context."
    "This can be referenced to get the info to create a standalone question can be understood"
    "without chat history. Do NOT answer the question just formulate the question."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")]
)

history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

contextualize_qa_system_prompt = (
    "You are a helpful assistant in question-answering tasks."
    "Use the provided context to generate a relevant question"
    "\n\n"
    "{context}"
)

contextualize_qa_prompt = ChatPromptTemplate.from_messages(
    [("system", contextualize_qa_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")]   
)

stuff_documents = create_stuff_documents_chain(llm, contextualize_qa_prompt)

rag_chain = create_retrieval_chain(history_aware_retriever, stuff_documents)

react_docstore_prompt = hub.pull("hwchase17/react")

tools = [
    Tool(
        name="answer question",
        description="Answer questions based on the provided context.",
        func=lambda input, **kwargs: rag_chain.invoke(
            {"input": input, "chat_history": kwargs.get("chat_history")}
        )
    )
]

agent = create_react_agent(
    tools=tools,
    prompt=react_docstore_prompt,
    llm=llm
)

agent_executor=AgentExecutor.from_agent_and_tools(
    agent, tools, verbose=True, handle_parsing_errors=True
)

chat_history=[]
while True:
    user_input=input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    response=agent_executor.invoke({"input": user_input, "chat_history": chat_history})
    print("AI response: ", response["output"])
    chat_history.append(AIMessage(content=response["output"]))

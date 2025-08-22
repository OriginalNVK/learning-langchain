from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o")  
Messages = [
    ("system", "You are a professional in {topic}."),
    ("human", "Tell me {number} signature in this {topic}")
]

upper_output = RunnableLambda(lambda x: x.upper())
words_count = RunnableLambda(lambda x: f"Words count:  {len(x.split())}\n{x}")

chains = ChatPromptTemplate.from_messages(Messages) | model | StrOutputParser() | upper_output | words_count

response = chains.invoke({"topic": "technology", "number": 5})
print("AI response: ", response)
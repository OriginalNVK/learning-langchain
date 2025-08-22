from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatOpenAI(model="gpt-4o")
messages = [
    SystemMessage(content = "You are a professional in {topic}."),
    HumanMessage(content = "Tell me {number} signature in this {topic}")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
chain = prompt_template | model | StrOutputParser()
result = chain.invoke({"topic": "technology", "number": 5})
print("AI response: ", result.content)
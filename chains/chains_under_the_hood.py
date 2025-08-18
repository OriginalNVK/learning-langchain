from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence

load_dotenv()
model = ChatOpenAI(model="gpt-4o")
Message = [
    ("system", "You are a professional in {topic}."),
    ("human", "Tell me {number} signature in this {topic}")
]

prompt_template = RunnableLambda(lambda x: ChatPromptTemplate.from_messages(Message).format_prompt(**x))
model_invoke = RunnableLambda(lambda x: model.invoke(x.to_messages()))
output = RunnableLambda(lambda x: x.content)

chains = RunnableSequence([prompt_template, model_invoke, output])
response = chains.invoke({"topic": "technology", "number": 5})
print("AI response: ", response)
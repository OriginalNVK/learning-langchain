from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o")
messages = [
    ("system", "You are an expert of product reviewer"),
    ("human", "List the main features of this product: {product_name}")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

def analyze_pros(features):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert of product reviewer"),
            ("human", "given some main features: {features}. List some pros features")
        ]
    )
    return pros_template.format_prompt(features=features)

def analyze_cons(features):
    cons_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert of product reviewer"),
            ("human", "given some main features: {features}. List some cons features")
        ]
    )
    return cons_template.format_prompt(features=features)

cons_branch_chain = RunnableLambda(lambda x: analyze_cons(x)) | model | StrOutputParser()
pros_branch_chain = RunnableLambda(lambda x: analyze_pros(x)) | model | StrOutputParser()

def combined_chain(cons, pros):
    return f"Pros: {pros}, Cons: {cons}"

chain = prompt_template | model | RunnableParallel("branches", [pros_branch_chain, cons_branch_chain]) | RunnableLambda(lambda x: combined_chain(x["branches"]["cons"], x["branches"]["pros"]))

response = chain.invoke({"product_name": "Macbook Air pro"})
print(response.content)
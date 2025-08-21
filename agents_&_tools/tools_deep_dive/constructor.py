from langchain_openai import ChatOpenAI
from langchain.tools import StructuredTool, Tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.pydantic_v1 import BaseModel, Field
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

prompt = hub.pull("hwchase17/openai-tools-agent")

def greet_user(name:str) -> str:
    """Greets the user by name."""
    return f"Hello {name}!"

def reverse_string(text:str) -> str:
    """Reverses the given string."""
    return text[::-1]

def concatenate_string(a:str, b:str) -> str:
    """Concatenates two strings."""
    return a + b

class ConcatenateInput(BaseModel):
    a: str = Field(description="First string")
    b: str = Field(description="Second string")
    
tools = [
    Tool(
        name="GreetUser",
        description="Say hello to user name",
        func=greet_user
    ),
    Tool(
        name="ReverseString",
        description="Reverses the given string",
        func=reverse_string
    ),
    Tool(
        name="ConcatTwoStrings",
        description="Concatenate two strings",
        func=concatenate_string,
        args_schema=ConcatenateInput
    )
]

llm = ChatOpenAI(model="gpt-4o")
agent = create_tool_calling_agent(
    tools=tools, llm=llm, prompt=prompt
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)

response = agent_executor.invoke({"input": "Say hello to Grace"})
print("AI response to 'Grace': ", response["output"])

response=agent_executor.invoke({"input": "Reverse the text 'hello world'"})
print("AI reverse the string: ", response["output"])

response=agent_executor.invoke({"input": "Concatenate 'hello' and 'world'"})
print("AI concat two strings: ", response["output"])

import os
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import BaseTool
from typing import Type
from langchain.pydantic_v1 import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
llm=ChatOpenAI(model="gpt-4o")
prompt=hub.pull("hwchase17/openai-tools-agent")

class searchInput(BaseModel):
    query: str = Field(description="Search query")
    
class multipleInput(BaseModel):
    x: float = Field(description="First number")
    y: float = Field(description="Second number")
    
class searchTool(BaseTool):
    name="search"
    args_schema=searchInput
    description="Search information about a specific topic"
    def _run(self, query: str) -> str:
        from tavily import TavilyClient
        api_key = os.getenv("TAVILY_API_KEY")
        client = TavilyClient(api_key=api_key)
        response = client.search(query)
        return response

class multiplyTool(BaseTool):
    name="multiply"
    args_schema:Type[BaseModel] = multipleInput
    description="Multiply two numbers"
    def _run(self, x: float, y: float) -> float:
        return x * y
    
tools = [
    searchTool(),
    multiplyTool()
]

agents = create_tool_calling_agent(llm, tools, prompt)

agent_executor=AgentExecutor.from_agent_and_tools(
    agents, tools, verbose=True, handle_parsing_errors=True
)

# response = agent_executor.invoke({"input": "Cat"})
# print("AI response cat infor: ", response["output"])

response = agent_executor.invoke({"input": "multiply 10 and 20"})
print("AI response multiple: ", response["output"])
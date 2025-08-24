from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

load_dotenv()
llm = ChatOpenAI(model = "gpt-4o")
class AgentState(TypedDict):
    messages: List[HumanMessage]
    
def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print("AI: ", response.content)
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    agent.invoke({"messages": [HumanMessage(content = user_input)]})
    
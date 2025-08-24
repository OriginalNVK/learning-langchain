import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from typing import TypedDict, List, Union
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4o")

class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]
    
def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print("AI: ", response.content)
    state["messages"].append(AIMessage(content=response.content))
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

conversation_list = []
while True:
    user_input=input("You: ")
    if user_input.lower() == "exit":
        break
    conversation_list.append(HumanMessage(content=user_input))
    state = agent.invoke({"messages": conversation_list})
    conversation_list = state['messages']

with open("db/logging.txt", "w") as file:
    file.write("Conversation start write in logging.txt file\n")
    for message in conversation_list:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n")
    file.write("End of conversation")
print("Conversation Logged saved to logging.txt")
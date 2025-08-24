from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, BaseMessage, HumanMessage
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Sequence
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langchain.tools import tool
from langgraph.prebuilt import ToolNode

load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    
@tool
def add(a: int, b: int) -> int:
    """Additional 2 numbers"""
    return a + b

@tool
def subtract(a: int, b: int) -> int:
    """Subtraction 2 numbers"""
    return a - b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplication 2 numbers"""
    return a * b

tools = [add, subtract, multiply]
llm = ChatOpenAI(model="gpt-4o").bind_tools(tools)

def react_agent(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(content = "You are a helpful AI assistant, please answer the question")
    response = llm.invoke([system_prompt] + state['messages'])
    return {'messages': [response]}

def should_continue(state: AgentState):
    last_message = state['messages'][-1]
    if not getattr(last_message, "tool_calls", None):
        return "end"
    return "continue"

graph = StateGraph(AgentState)
graph.add_node("react_agent", react_agent)
tool_node = ToolNode(tools = tools)
graph.add_node("tool_node", tool_node)
graph.set_entry_point("react_agent")
graph.add_conditional_edges("react_agent", should_continue, {
    "continue": "tool_node",
    "end": END
})
graph.add_edge("tool_node", "react_agent")
agent = graph.compile()

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()
    
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    init_state = {"messages": [HumanMessage(content = user_input)]}
    print_stream(agent.stream(init_state, stream_mode="values"))


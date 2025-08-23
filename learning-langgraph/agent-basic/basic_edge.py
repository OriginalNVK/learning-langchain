from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    age: int
    result: str

def first_node(state: AgentState) -> AgentState:
    """This node will add greeting name to the result"""
    state['result'] = f"Hello {state['name']}!"
    return state

def second_node(state: AgentState) -> AgentState:
    """This node will show age of the name to the result"""
    state['result'] = state['result'] + f": You are {state['age']} years old"
    return state

graph = StateGraph(AgentState)
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.set_finish_point("second_node")

app = graph.compile()

result = app.invoke({"name": "Original NVK", "age": 22})
print(result['result'])
from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    age: int
    skill: List[str]
    result: str
    
def first_node(state: AgentState) -> AgentState:
    """This node will add greeting name to the result"""
    state['result'] = f"Hello {state['name']}!"
    return state

def second_node(state: AgentState) -> AgentState:
    """This node will show the age of the name to the result"""
    state['result'] = state['result'] + f": You are {state['age']} years old"
    return state

def third_node(state: AgentState) -> AgentState:
    """This node will show some skills of the name to the result"""
    state['result'] = state['result'] + f": Your skills are {', '.join(state['skill'])}"
    return state

graph = StateGraph(AgentState)
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.add_node("third_node", third_node)
graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.add_edge("second_node", "third_node")
graph.set_finish_point("third_node")

app = graph.compile()

result = app.invoke({"name": "Original NVK", "age": 22, "skill": ["Python", "Java", "C++"]})
print(result['result'])
from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
import random

class AgentState(TypedDict):
    name: str
    count: int
    number: List[int]

def greeting(state: AgentState) -> AgentState:
    state['name'] = f"Hello {state['name']}!"
    state['count'] = 0
    return state

def random_number(state: AgentState) -> AgentState:
    state['number'].append(random.randint(1, 10))
    state['count'] += 1
    return state

def decide_continue(state: AgentState) -> str:
    if state['count'] < 5:
        return 'loop'
    return 'end'

graph = StateGraph(AgentState)
graph.add_node("greeting", greeting)
graph.add_node("loop", random_number)
graph.add_edge("greeting", "loop")
graph.set_entry_point("greeting")
graph.add_conditional_edges("loop", decide_continue, {
    "loop": "loop",
    "end": END
})

app = graph.compile()
initState = AgentState({
    'name': 'World',
    'count': 0,
    'number': []
})
result = app.invoke(initState)
print(result)

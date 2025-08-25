from typing import TypedDict
from langgraph.graph import StateGraph, END, START

class AgentState(TypedDict):
    number1: int
    number2: int
    operation1: str
    number3: int
    operation2: str
    result: int
    
def sum_node(state: AgentState) -> AgentState:
    state['result'] = state['number1'] + state['number2']
    return state

def subtract_node(state: AgentState) -> AgentState:
    state['result'] = state['number1'] - state['number2']
    return state

def multiply_node(state: AgentState) -> AgentState:
    state['result'] = state['number1'] * state['number2']
    return state

def sum_node_2(state: AgentState) -> AgentState:
    state['result'] = state['result'] + state['number3']
    return state

def subtract_node_2(state: AgentState) -> AgentState:
    state['result'] = state['result'] - state['number3']
    return state    

def multiply_node_2(state: AgentState) -> AgentState:
    state['result'] = state['result'] * state['number3']
    return state

def decide_next_node(state: AgentState) -> str:
    if state['operation1'] == '+':
        return "addition_node"
    elif state['operation1'] == '-':
        return "subtraction_node"
    elif state['operation1'] == '*':
        return "multiplication_node"

def decide_next_node_2(state: AgentState) -> str:
    if state['operation2'] == '+':
        return "addition_node_2"
    elif state['operation2'] == '-':
        return "subtraction_node_2"
    elif state['operation2'] == '*':
        return "multiplication_node_2"

graph = StateGraph(AgentState)

graph.add_node("addition_node", sum_node)
graph.add_node("subtraction_node", subtract_node)
graph.add_node("multiplication_node", multiply_node)

graph.add_node("addition_node_2", sum_node_2)
graph.add_node("subtraction_node_2", subtract_node_2)
graph.add_node("multiplication_node_2", multiply_node_2)

graph.add_conditional_edges(START, decide_next_node, {
    "addition_node": "addition_node",
    "subtraction_node": "subtraction_node",
    "multiplication_node": "multiplication_node"
})

graph.add_conditional_edges("addition_node", decide_next_node_2, {
    "addition_node_2": "addition_node_2",
    "subtraction_node_2": "subtraction_node_2",
    "multiplication_node_2": "multiplication_node_2"
})

graph.add_conditional_edges("subtraction_node", decide_next_node_2, {
    "addition_node_2": "addition_node_2",
    "subtraction_node_2": "subtraction_node_2",
    "multiplication_node_2": "multiplication_node_2"
})

graph.add_conditional_edges("multiplication_node", decide_next_node_2, {
    "addition_node_2": "addition_node_2",
    "subtraction_node_2": "subtraction_node_2",
    "multiplication_node_2": "multiplication_node_2"
})

graph.add_edge("addition_node_2", END)
graph.add_edge("subtraction_node_2", END)
graph.add_edge("multiplication_node_2", END)

app = graph.compile()

initState = AgentState({
    "number1": 5,
    "number2": 10,
    "operation1": "+",
    "number3": 3,
    "operation2": "*",
    "result": 0,
})

result = app.invoke(initState)
print(result['result']) 

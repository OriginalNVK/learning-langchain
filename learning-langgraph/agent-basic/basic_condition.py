from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    number1: int
    number2: int
    operation: str
    result: str

def sum_node(state: AgentState) -> AgentState:
    """This node will add two numbers"""
    state['result'] = state['number1'] + state['number2']
    return state

def subtract_node(state: AgentState) -> AgentState:
    """This node will subtract two numbers"""
    state['result'] = state['number1'] - state['number2']
    return state

def decided_next_node(state: AgentState) -> AgentState:
    """This node will decide the next node based on the operation"""
    if state['operation'] == '+':
        return "addition_node"
    elif state['operation'] == '-':
        return "subtraction_node"
    else:
        raise ValueError("Invalid operation. Please use '+' or '-'.")

graph = StateGraph(AgentState)
graph.add_node("addition_node", sum_node)
graph.add_node("subtraction_node", subtract_node)
graph.add_node("decided_next_node", lambda state: state)

graph.add_edge(START, "decided_next_node")
graph.add_conditional_edges(
    "decided_next_node",
    decided_next_node,
    {
        "addition_node": "addition_node",
        "subtraction_node": "subtraction_node"
    }
)
graph.add_edge("decided_next_node", END)

app = graph.compile()

initState = AgentState({
    "number1": 10,
    "number2": 5,
    "operation": "+"
})
result = app.invoke(initState)
print(result['result'])

from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    values: List[int]
    name: str
    result: str
    operation: str

def processor(state: AgentState) -> AgentState:
    """This processor handles the operations of the list values"""
    if state['operation'] == '*':
        state['result'] = f"{state['name']}: multiply the list values is {eval('*'.join(map(str, state['values'])))}"
    elif state['operation'] == '+':
        state['result'] = f"{state['name']}: sum the list values is {sum(state['values'])}"
    elif state['operation'] == '-':
        state['result'] = f"{state['name']}: subtract the list values is {eval('-'.join(map(str, state['values'])))}"
    return state

graph = StateGraph(AgentState)
graph.add_node("processor", processor)
graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()

result = app.invoke({"values": [1, 2, 3, 4], "name": "Original NVK", "operation": "*"})
print(result)

result = app.invoke({"values": [1, 2, 3, 4], "name": "Original NVK", "operation": "+"})
print(result)

result = app.invoke({"values": [1, 2, 3, 4], "name": "Original NVK", "operation": "-"})
print(result)
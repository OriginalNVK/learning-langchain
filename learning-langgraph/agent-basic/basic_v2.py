from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    values: List[int]
    name: str
    result: str
    
def processor_sum(state: AgentState) -> AgentState:
    """This processos handle the sum of list number"""
    state['result'] = f"{state['name']:} the sum of list number is: {sum(state['values'])}"
    return state

graph = StateGraph(AgentState)
graph.add_node("processor", processor_sum)
graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()

result = app.invoke({"values": [1, 2, 3, 4], "name": "OriginalNVK"})

print(result['result'])

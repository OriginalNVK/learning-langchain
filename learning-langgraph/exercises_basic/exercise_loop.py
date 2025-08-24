from typing import TypedDict, List
from langgraph.graph import StateGraph, END
import random

class AgentState(TypedDict):
    bound_min: int
    bound_max: int
    attempts: int
    guess_number: int
    number: int
    result: str
    
def start_game(state: AgentState) -> AgentState:
    state['attempts'] = 0
    state['bound_min'] = 1
    state['bound_max'] = 20
    return state

def make_guess(state: AgentState) -> AgentState:
    state['guess_number'] = random.randint(state['bound_min'], state['bound_max'])
    state['attempts'] += 1
    return state

def check_result(state: AgentState) -> str:
    if state['attempts'] < 7:
        if state['guess_number'] < state['number']:
            state['result'] = f"The number you guessed is too low."
            res = "low"
        elif state['guess_number'] > state['number']: 
            state['result'] = f"The number you guessed is too high."
            res = "high"
        else:
            state['result'] = f"Congratulations! You've guessed the number {state['number']}!"
            res = "correct"
        return res
    state['result'] = f"Game over! You've used all attempts. The number was {state['number']}."
    return "over"
    
    

graph = StateGraph(AgentState)
graph.add_node("start_game", start_game)
graph.add_node("make_guess", make_guess)
graph.set_entry_point("start_game")
graph.add_edge("start_game", "make_guess")
graph.add_conditional_edges("make_guess", check_result,
                            {
                                "low": "make_guess",
                                "high": "make_guess",
                                "correct": END,
                                "over": END
                            })
app = graph.compile()

init_state = AgentState(
    {
        "bound_min": 1,
        "bound_max": 20,
        "number": 7
    }
)

result = app.invoke(init_state)
print(result)


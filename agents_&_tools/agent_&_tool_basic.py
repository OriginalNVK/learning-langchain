from langchain_openai import ChatOpenAI
from langchain_core.agents import AgentExecutor, create_react_agent
from langchain_core.tools import Tool
from dotenv import load_dotenv
from langchain import hub

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def get_current_time(*arg, **kwargs):
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

tools = [
    Tool(
        name="Time",
        func = get_current_time,
        description = "useful for get the current time"
    )
]

prompt_template = hub.pull("hwchase17/react")

agents = create_react_agent(
    llm, tools, prompt_template, stop_sequence=True
)

ag_and_tool = AgentExecutor.create_agent_and_tool(
    tools=tools,
    agents=agents,
    verbose=True
)

query = "What time is it?"
response = ag_and_tool.invoke(query)

print("AI response: ", response)
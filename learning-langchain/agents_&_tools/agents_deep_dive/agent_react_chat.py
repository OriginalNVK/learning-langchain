from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain.tools import Tool
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def get_current_time(*args, **kwargs):
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def search_wikipedia(query):
    from wikipedia import summary
    try:
        return summary(query, sentences=2)
    except:
        return "Sorry, I couldn't find any information on that."

tools =[
     Tool(
        name = "Time",
        func = get_current_time,
        description = "Useful for getting the current time."
    ),
    Tool(
        name = "wikipedia search",
        func = search_wikipedia,
        description = "Useful for getting information about a topic"
    )
]

prompt_template = hub.pull("hwchase17/structured-chat-agent")

agents = create_structured_chat_agent(
    llm = llm,
    tools = tools,
    prompt = prompt_template
)

memory = ConversationBufferMemory(
    memory_key = "chat_history",
    return_messages = True
)

ag_and_tool = AgentExecutor.from_agent_and_tools(
    agent=agents,
    tools=tools,
    verbose=True,
    memory=memory,
    handle_parsing_error=True
)

initial_message = "You are a professional assistant. Can help any topic in the world"
memory.chat_memory.add_message(SystemMessage(content=initial_message))

while True:
    user_input = input("You: ")
    memory.chat_history.add_message(HumanMessage(content = user_input))
    response = ag_and_tool.invoke(user_input)
    print("AI response: ", response["output"])
    memory.chat_history.add_message(AIMessage(content = response["output"]))
from langchain_openai import ChatOpenAI
from dotenv import load_env
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_env()

model = ChatOpenAI(model="gpt-4o")

chat_history = []
system_message = SystemMessage("You are a helpful AI assistant.")

chat_history.append(system_message)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content = response.content))
    print("AI:", response.content)

print("Chat history: ", chat_history)
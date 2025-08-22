from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="gpt-4o")

ProjectID="langchain-demo"
SessionID="session-test"
CollectionName="chat_history"

firestore_client = firestore.Client(project=ProjectID)
chatHistory = FirestoreChatMessageHistory(
    firestore_client=firestore_client,
    session_id=SessionID,
    collection_name=CollectionName
)

while True:
    user_input = input("Your message: ")
    if user_input.lower() == "exit":
        break
    chatHistory.add_user_message(user_input)
    response = model.invoke(chatHistory.messages)
    chatHistory.add_ai_message(response.content)
    print("AI:", response.content)
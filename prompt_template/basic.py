from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

prompt_sample = "Tell me {count} things about {topic}."
prompt_template = ChatPromptTemplate.from_template(prompt_sample)
prompt = prompt_template.invoke({"count": 3, "topic": "cats"})
print(prompt)
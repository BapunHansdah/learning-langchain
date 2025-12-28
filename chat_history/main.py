from langchain_classic.schema import HumanMessage, AIMessage, SystemMessage
from basic_llm_call.main import llm

messages = [
    SystemMessage(content="You are a friendly tutor teaching Python."),
    HumanMessage(content="What is a list in Python?"),
]

response = llm.invoke(messages)
print("Example 4 - Chat with Context:")
print(response.content)

# Continue the conversation
messages.append(AIMessage(content=response.content))
messages.append(HumanMessage(content="Can you give me an example?"))

response = llm.invoke(messages)
print("\nFollow-up response:")
print(response.content)
print("\n" + "="*50 + "\n")
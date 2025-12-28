from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
print(openai_api_key)

llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo", 
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7,
    api_key=openai_api_key
)

# response = llm.invoke("Tell me a joke about programming")
# print("Example 1 - Simple LLM Call:")
# print(response.content)
# print("\n" + "="*50 + "\n")
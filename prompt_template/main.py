from langchain_core.prompts import PromptTemplate
from basic_llm_call.main import llm


template = """
You are a helpful assistant. 
Answer the question about {topic} in a {style} way.

Question: {question}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["topic", "style", "question"]
)

# Fill in the template
formatted_prompt = prompt.format(
    topic="Python programming",
    style="simple and friendly",
    question="What is a variable?"
)

response = llm.invoke(formatted_prompt)
print("Example 2 - Prompt Template:")
print(response.content)
print("\n" + "="*50 + "\n")
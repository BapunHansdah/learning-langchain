from langchain_classic.chains import LLMChain
from basic_llm_call.main import llm
from langchain_core.prompts import PromptTemplate

template = """
You are a helpful assistant. 
Answer the question about {topic} in a {style} way.

Question: {question}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["topic", "style", "question"]
)

chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
result = chain.invoke({
    "topic": "cooking",
    "style": "enthusiastic",
    "question": "How do I make pasta?"
})

print("Example 3 - Simple Chain:")
print(result["text"])
print("\n" + "="*50 + "\n")
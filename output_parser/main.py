from langchain_classic.output_parsers import CommaSeparatedListOutputParser
from langchain_classic.chains import LLMChain
from basic_llm_call.main import llm
from langchain_core.prompts import PromptTemplate

output_parser = CommaSeparatedListOutputParser()

format_instructions = output_parser.get_format_instructions()

prompt_template = """
List 5 {item_type}.
{format_instructions}
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["item_type"],
    partial_variables={"format_instructions": format_instructions}
)

chain = LLMChain(llm=llm, prompt=prompt)

output = chain.invoke({"item_type": "programming languages"})
parsed_output = output_parser.parse(output["text"])

print("Example 5 - Output Parser:")
print("Raw output:", output["text"])
print("Parsed output (as list):", parsed_output)
print(type(parsed_output))  
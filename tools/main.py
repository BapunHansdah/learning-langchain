"""
Tools let the AI do actions like:
- Search the web
- Calculate math
- Access databases
- Read files
"""

from langchain.tools import tool

@tool
def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius."""
    import math
    return math.pi * radius ** 2

@tool
def search_wikipedia(query: str) -> str:
    """Search Wikipedia for information."""
    return f"Searching Wikipedia for: {query}"

tools = [calculate_circle_area, search_wikipedia]

print("TOOLS Example:")
print(f"Tool 1: {calculate_circle_area.name}")
print(f"Description: {calculate_circle_area.description}")
print(f"Example use: Area = {calculate_circle_area.invoke({'radius': 5})}")
print("\n" + "="*50 + "\n")

print(f"Tool 2: {search_wikipedia.name}")
print(f"Description: {search_wikipedia.description}")
print(f"Example use: {search_wikipedia.invoke({'query': 'Python programming'})}")
print("\n" + "="*50 + "\n")


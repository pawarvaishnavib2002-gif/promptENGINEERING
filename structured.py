# structured output prompting

from ai_helper import ask_ai

prompt = """
Explain Python in simple words.

Return the answer in this JSON format:
{
    "definition": "...",
    "example": "..."
}
"""

print(ask_ai(prompt))
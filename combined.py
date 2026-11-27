from ai_helper import ask_ai

prompt = """
Role: Act as a Python teacher.

Context: I am a beginner learning Python for Data Analyst jobs.

Task: Explain Python lists.

Instructions:
1. Use simple English.
2. Give one code example.
3. Return the answer in 3 bullet points.
"""

print(ask_ai(prompt))
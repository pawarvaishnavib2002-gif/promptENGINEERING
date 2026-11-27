from ai_helper import ask_ai

topic="python"
level="beginner"

prompt=f"""

explain {topic} to a {level}

give one simple example.

"""
print(ask_ai(prompt))
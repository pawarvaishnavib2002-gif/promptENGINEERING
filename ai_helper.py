import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv(r"C:\Users\g11111\Desktop\genai\.env")

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Check key
print("Key loaded:", bool(api_key))

# Create client
client = OpenAI(api_key=api_key)

# Ask AI function
def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
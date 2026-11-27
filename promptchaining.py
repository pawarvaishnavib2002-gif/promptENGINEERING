from ai_helper import ask_ai

# Step 1: Generate code
code = ask_ai("Write Python code to add two numbers.")

# Step 2: Explain the code
explanation = ask_ai(f"Explain this code to a beginner:\n{code}")

print("CODE:")
print(code)

print("\nEXPLANATION:")
print(explanation)
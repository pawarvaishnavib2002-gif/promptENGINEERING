from ai_helper import ask_ai

prompt = """
Classify the review as Positive or Negative.

Review: I love this product.
Answer: Positive

Review: This product is terrible.
Answer: Negative

Review: The phone is amazing.
Answer:
"""

print(ask_ai(prompt))

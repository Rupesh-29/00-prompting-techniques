import sys
from pathlib import Path   
sys.path.append(str(Path(__file__).resolve().parent.parent / "prompts"))
from helper import get_completion
refund_policy = """
Refund policy:
1. Customers can request a refund within 10 days of purchase.
2. If any damage may occur during the return process, the refund will not be valued.
3. The Refunded Amount will be credited to the bank account of the customer within 5 working dyas after the refund is accepted.
"""

customer_question = """
I have Bought this product 3 days ago.
I am satisfied with the product but I want to return it because I don't need this right now.
Can i get a refund for this one...?
"""

prompt = f"""
Role:
You are a customer support assistant for a software company.

Task:
Answer the customer question using only the refund policy provided below.

Instruction Guardrails:
1. Use only the information from the policy text.
2. Do not invent any new company rules.
3. If the policy does not clearly answer the question, say:
   "Please contact human support for clarification."
4. Keep the answer short and clear.
5. Use a polite professional tone.
6. End with one next-step suggestion for the customer.

Refund Policy:
{refund_policy}

Customer Question:
{customer_question}
"""

response = get_completion(prompt)
print(response)
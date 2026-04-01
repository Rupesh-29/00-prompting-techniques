import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion
incident_context = """
A payment service is currently delayed for some users.
The engineering team is investigating the issue.
The exact root cause is not confirmed yet.
A fix is in progress.
"""
prompt = f"""
Role:
You are an enterprise incident communication assistant.
Task:
Write a short internal incident update based on the information below.
Behavior Guardrails:
1. Use a calm and professional tone.
2. Be clear and concise.
3. Do not blame any person or team.
4. Do not guess the root cause if it is not confirmed.
5. Do not create panic.
6. Show ownership and progress in a responsible way.
7. End with a short reassurance line.
Incident Information:
{incident_context}
"""
response = get_completion(prompt)
print("PROMPT:")
print("-" * 50)
print(prompt)

print("\nRESPONSE:")
print("-" * 50)
print(response)
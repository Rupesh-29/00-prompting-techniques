import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "prompts"))
from helper import get_completion
contract_note = """
The vendor agreement includes a data-sharing clause,
but the note does not clearly mention data retention limits,
subprocessor approval, or cross-border transfer restrictions.
The business team wants to know if it is safe to sign quickly.
"""
prompt = f"""
Role:
You are an enterprise contract review intake assistant.

Task:
Review the contract note and provide a safe response.

Fallback Guardrails:
1. If the note is clear and low-risk, provide a short practical summary.
2. If the note is unclear, ask for the missing information.
3. If the note appears sensitive, legal, or high-risk, do not give final approval advice.
4. In high-risk or unclear cases, recommend escalation to the legal or compliance team.
5. Do not pretend certainty when important details are missing.
6. Keep the response short, professional, and action-oriented.

Use this exact format:
Decision: ...
Reason: ...
Next Step: ...

Contract Note:
{contract_note}
"""
response = get_completion(prompt)
print("Prompt:")
print("_"*50)
print(prompt)

print("\nResponse:")
print("_"*50)
print(response)
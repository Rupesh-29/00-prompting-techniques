import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "prompts"))
from helper import get_completion
device_name = "Infusion Pump X2"
location = ""
issue_summary = "The screen freezes during startup."
severity = "urgent"
if not device_name.strip():
    print("Blocked: device_name is required.")

elif not location.strip():
    print("Blocked: location is required.")

elif not issue_summary.strip():
    print("Blocked: issue_summary is required.")

elif severity.lower() not in ["low", "medium", "high", "critical"]:
    print("Blocked: severity must be low, medium, high, or critical.")

else:
     prompt = f"""
Role:
You are a medical device support intake assistant.

Task:
Convert the intake details below into a short internal support summary.

Rules:
1. Use only the details provided.
2. Keep the summary short and clear.
3. Do not guess the technical cause.
4. Recommend the next intake route based on severity.

Use this format:
Device: ...
Location: ...
Severity: ...
Issue Summary: ...
Recommended Intake Route: ...

Validated Intake Details:
Device Name: {device_name}
Location: {location}
Issue Summary: {issue_summary}
Severity: {severity}
"""
response = get_completion(prompt)
print("prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)
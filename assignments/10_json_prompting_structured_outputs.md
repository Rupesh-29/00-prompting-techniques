import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "prompts"))
from helper import get_completion
prompt = """
Create a 5 day plan to learn prompt Engineering for a beginner. 
Read only valid JSON.
Do Not include markdown.
Do Not include code fences.
Use this exact structure:{
    "topic" : "string",
    "audience" : "string",
    "days" : [
    {
    "day" : 1,
    "focus" : "string",
    "task" : "string",
    "estimated time" : 0,
    }
    ]
}
Rules:
Keep Exactly 7 days
The language should clear and understandable
Make each task realstic for 1 hour or less
"""

response=get_completion(prompt)

print("prompt:")
print("_"*50)
print(prompt)

print("\nResponse:")
print("_"*50)
print(response)

print("\nParsed JSON")
print("_"*50)

try:
    data = json.loads(response)
    print(json.dumps(data, indent=2))
except json.JSONDecodeError:
    print("The response was not valid JSON.")
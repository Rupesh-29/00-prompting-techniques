import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent /"prompts"))
sys.path.append('../prompts')
from helper import get_completion
topic = "prompt Engineering"
time_available = "1 hour per day"
audience = "A complete Beginner with a full time job"
prompt_v1 = """
Create a 5-day plan for prompt Engineering
"""

prompt_v2 = """
Role:
You are a complete beginner friendly AI coach

Task:
Create a 5-day plan for prompt Engineering

Constraints:
Keep the teaching very simple.
Keep it clear and understandable.
Don't use technical words.
Language Should be very Normal. 

Context:
The learner is A complete beginner with a full time job
The learner can study only 1 hour per day

Output format:
Day 1 : ....
Day 2 : ....
Day 3 : ....
Day 4 : ....
Day 5 : ....
"""
response_v1=get_completion(prompt_v1)
response_v2=get_completion(prompt_v2)

print("PROMPT VERSION 1")
print("_"*50)
print(prompt_v1)

print("\n RESPONSE VERSION 1")
print("_"*50)
print(response_v1)

print("PROMPT VERSION 2")
print("_"*50)
print(prompt_v2)

print("\n RESPONSE VERSION 2")
print("_"*50)
print(response_v2)
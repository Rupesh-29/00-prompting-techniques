import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "prompts"))
from helper import get_completion
prompt = """
Role:
You are a beginner friendly AI learning coach.

Task:
Create A 10 days plan to learn AI.

Context:
The Learner is a student and give the plan accordingly to that.
Give him more in a practical manner not textual content.

Constraints:
Use only beginner friendly language.
Do Not include the technical words.
It should be easy and able to understand.

Output Format:
Return the output in this format:

Day 1 : .....
Day 2 : .....
Day 3 : .....
Day 4 : .....
Day 5 : .....
Day 6 : .....
Day 7 : .....
Day 8 : .....
Day 9 : .....
Day 10 : .....
"""
response=get_completion(prompt)
print("prompt:")
print("_"*50)
print(prompt)

print("\nResponse:")
print("_"*50)
print(response)
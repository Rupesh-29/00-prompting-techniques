import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent / "prompts"))

from helper import get_completion

prompt = """
Convert the sentence into a more professional business tone.

Example:
Input: send me the file fast
Output: Could you please share the file at your earliest convenience?

Now do the same for:
Input: How Much Time will you take to complete the work. The Manager is very serious about the deadline. So complete the work as soon as posssible.
Output:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "prompts"))

from helper import get_completion
prompt = """
classify the following sentence as positive, negative, neutral.

sentence:I am very good at Programming.
semantic:positive

sentence: I am not good at programming.
semantic:negative

sentence: I am good at programming but I'm a little bit confused at Data Structures.
semantic:neutral

sentence: I Can Do programming very well and also I am also very passionate about it but the Main problem is I can't understand about the DSA concepts.
semantic:

"""
response = get_completion(prompt)
print("prompt:")
print("_"*50)
print(prompt)

print("\nResponse:")
print("_"*50)
print(response)
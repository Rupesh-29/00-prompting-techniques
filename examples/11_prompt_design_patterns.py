import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "prompts"))
from helper import get_completion
review_text = """
I have bought the I Phone last Month and the performance is very fast and very good actually. 
But After sometime the battery might get drained but I am Happy with the overall performance of the phone. 
"""

classification_prompt = """
classify the following sentiment into positive, Negative and Neutral.

Review:
{review_text}
"""
extraction_prompt = """
Extract the following details from the review. 

Model Name :
Positive Points :
Negative Points :
Overall opinion :
Review:
{review_text}
"""

Geneartion_prompt = """
Based on the following prompt generate a short summary for the customer happiness. 

Review:
{review_text}
"""
classification_response = get_completion(classification_prompt)
extraction_response = get_completion(extraction_prompt)
Generation_response = get_completion(Geneartion_prompt)

print("Classification")
print("_"*50)
print(classification_response)

print("\nextraction")
print("_"*50)
print(classification_response)

print("\nExtraction")
print("_"*50)
print(extraction_response)

print("\nGeneration")
print("_"*50)
print(Generation_response)
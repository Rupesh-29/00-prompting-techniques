"""
Prompting Techniques
Example: System, User, and Assistant/Model roles
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

Client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_instruction = """
You are beginner friendly Gym trainer for a student.
Tell him how to be prepared for a workout and also tell him what type of food habits will he want to take.
Tell him in a very clear and understanable way.
Keep the language simple and concised.
"""

user_message = "Teach me how to drive a car for the first time."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_message,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.7,
        top_p=0.95,
        max_output_tokens=400,
    ),
)

print("SYSTEM ROLE:")
print("-" * 50)
print(system_instruction)

print("\nUSER ROLE:")
print("-" * 50)
print(user_message)

print("\nASSISTANT / MODEL RESPONSE:")
print("-" * 50)
print(response.text)
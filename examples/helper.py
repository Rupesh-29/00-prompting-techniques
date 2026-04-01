from dotenv import load_dotenv
from google import genai
import os

load_dotenv()  

print("API Key:", os.getenv("GEMINI_API_KEY"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  # Capital C

def get_completion(prompt, model="gemini-2.5-flash"):
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    return response.text

print(get_completion("Say hello"))
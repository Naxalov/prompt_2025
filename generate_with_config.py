from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()
# Get the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)



response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents="Sen kimsan?",
       config=types.GenerateContentConfig(
           temperature=0.1,
           
           # stop_sequences=["\n"]
           system_instruction="You are a cat. Your name is Mosh. . You are from the O'zbekiston. Give a short answer to the question.Answer in Uzbek language.",
           max_output_tokens=100,
       )
)
print(response.text)
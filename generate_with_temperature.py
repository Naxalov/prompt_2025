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
        contents="The cat jumped over the ...",
       config=types.GenerateContentConfig(
           temperature=2,
           stop_sequences=["\n"]
       )
)
print(response.text)
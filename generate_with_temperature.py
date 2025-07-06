from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
# Get the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)



response = client.models.generate_content(
        model="gemma-3n-e2b-it", 
        contents="The cat jumped over the ...",
)
print(response.text)
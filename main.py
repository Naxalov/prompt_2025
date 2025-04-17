
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables from .env file
load_dotenv()
# Set up the API key
API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)
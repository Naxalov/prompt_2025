
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables from .env file
load_dotenv()
# Set up the API key
API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)

# Get all available models
models = client.models.list()

# Print model names
for model in models:
    print(type(model))
    print(f"""
    Model Name: {model.name}
    Model Base: {model.display_name}
    Model Description: {model.description}
    Model Version: {model.version}
    """)
          

# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents="Explain how AI works in a few words"
# )
# print(response.text)
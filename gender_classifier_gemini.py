from dotenv import load_dotenv
from google import genai
import os

# Load environment variables from .env file
load_dotenv()
# Set up the API key
API_KEY = os.getenv("GOOGLE_API_KEY")
print(API_KEY)
# Set up the# Authenticate
client = genai.Client(api_key="AIzaSyD7gt39JsVQgWYT8YldeLeyyd_-_vCZCOM")

# Upload image file (replace with your actual image path)
myfile = client.files.upload(file="test10.jpg")

# Ask the Gemini model to classify the gender
response = client.models.generate_content(
    model="gemini-2.5-pro-exp-03-25",  # or "gemini-2.0-flash" for faster, lighter model
    contents=[
        myfile,
          """
        You are given a photo of a person's face.
        Please estimate:
        - Gender ('Male' or 'Female') with confidence as a percentage.
        - Age (as a number or age range, e.g., '25' or '20-30') with confidence as a percentage.

        Respond ONLY in JSON format like:
        {
            "gender": "Male",
            "gender_confidence": 92.5,
            "age": "25-30",
            "age_confidence": 85.0
        }
        """
    ]
)

# Output the model's prediction
print(response.text)
print(response.usage_metadata)


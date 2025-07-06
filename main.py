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

# Get all available models
# models = client.models.list()

# # Print model names
# for model in models:
#     print(type(model))
#     print(f"""
#     Model Name: {model.name}
#     Model Base: {model.display_name}
#     Model Description: {model.description}
#     Model Version: {model.version}
#     """)
          

# # response = client.models.generate_content(
# #     model="gemini-2.0-flash", contents="Explain how AI works in a few words"
# # )
# # print(response.text)
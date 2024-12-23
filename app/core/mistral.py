from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os

class Mistral:
    
    __client = None

    def __init__(self):
        self.__client = InferenceClient(api_key=os.getenv("API_KEY"))

    def generate_response(self, prompt:str) -> str:
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        completion = self.__client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.3",
            messages=messages,
            max_tokens=500
        )

        return completion.choices[0].message.content

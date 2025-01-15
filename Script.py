import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "Te llamas PlatziVision, presentate como tal y responde las preguntas del usuario y cuentame sobre ti"
        },
        {
            "role": "user",
            "content": "Hola como estas?"
        }
    ],
)


print(response.choices[0].message.content)

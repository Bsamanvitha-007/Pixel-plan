import openai
import requests
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def generate_design_prompt(style, room_type):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an interior designer."},
            {"role": "user", "content": f"Suggest a {style} design for a {room_type}"}
        ]
    )

    return response["choices"][0]["message"]["content"]


def generate_image(prompt):
    response = requests.post(
        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
        headers={"Authorization": "Bearer YOUR_HF_TOKEN"},
        json={"inputs": prompt},
    )

    return response.content
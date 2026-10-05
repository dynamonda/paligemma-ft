import ollama
from . import config


def run_ollama_with_image(image_path: str):
    response = ollama.chat(
        model=config.OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": "この画像を説明してください。",
                "images": [image_path],
            }
        ],
    )
    print(response["message"]["content"])

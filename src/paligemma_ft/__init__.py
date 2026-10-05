import argparse

from PIL import Image

from .immich import post_favorite_images
from .paligemma import run_llm
from .ollama import run_ollama_with_image

parser = argparse.ArgumentParser(description="PailGemmaを実行する")
parser.add_argument("image_path", type=str, help="画像のパス")
args = parser.parse_args()


def main() -> None:
    # post_favorite_images()

    image_path = args.image_path
    # image = Image.open(image_path)

    # run_llm(image)
    run_ollama_with_image(image_path)

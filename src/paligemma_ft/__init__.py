import argparse
from transformers import AutoProcessor, PaliGemmaForConditionalGeneration
from PIL import Image
import torch

model_id = "google/paligemma-3b-pt-448"

parser = argparse.ArgumentParser(description="PailGemmaを実行する")
parser.add_argument("image_path", type=str, help="画像のパス")
args = parser.parse_args()


def main() -> None:
    model = PaliGemmaForConditionalGeneration.from_pretrained(model_id).eval()
    processor = AutoProcessor.from_pretrained(model_id)

    image_path = args.image_path
    image = Image.open(image_path)

    prompt = "キャプションは、"
    model_inputs = processor(text=prompt, images=image, return_tensors="pt")
    input_len = model_inputs["input_ids"].shape[-1]

    with torch.inference_mode():
        generation = model.generate(**model_inputs, max_new_tokens=100, do_sample=False)
        generation = generation[0][input_len:]
        decoded = processor.decode(generation, skip_special_tokens=True)
        print(decoded)

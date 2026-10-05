from dotenv import load_dotenv
import os
import httpx

load_dotenv()  # .envファイルから環境変数を読み込む

IMMICH_SERVER_URL = os.getenv("IMMICH_SERVER_URL")
IMMICH_API_KEY = os.getenv("IMMICH_API_KEY")

search_url = f"{IMMICH_SERVER_URL}/api/search/metadata"
headers = {"x-api-key": IMMICH_API_KEY, "Content-Type": "application/json"}

payload = {"isFavorite": True, "type": "IMAGE", "size": 100}


def post_favorite_images():
    response = httpx.post(search_url, json=payload, headers=headers)
    if response.status_code == 200:
        search_results = response.json()
        print(search_results)

import httpx
from . import config

search_url = f"{config.IMMICH_SERVER_URL}/api/search/metadata"
headers = {"x-api-key": config.IMMICH_API_KEY, "Content-Type": "application/json"}

payload = {"isFavorite": True, "type": "IMAGE", "size": 100}


def post_favorite_images():
    response = httpx.post(search_url, json=payload, headers=headers)
    if response.status_code == 200:
        search_results = response.json()
        print(search_results)

import os

from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む

IMMICH_SERVER_URL = os.getenv("IMMICH_SERVER_URL")
IMMICH_API_KEY = os.getenv("IMMICH_API_KEY")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

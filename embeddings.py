import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
EMBED_MODEL_NAME = os.getenv(
    "EMBED_MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2"
)


API_URL = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{EMBED_MODEL_NAME}"

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def get_embedding(text: str) -> list[float]:

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": text, "options": {"wait_for_model": True}}
    )
    
    if response.status_code != 200:
        raise Exception(f"HuggingFace API error: {response.text}")
    
    result = response.json()
    
    if isinstance(result, list) and isinstance(result[0], list):
        return result[0]
    
    return result

import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
EMBED_MODEL_NAME = os.getenv("EMBED_MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")

model = SentenceTransformer(EMBED_MODEL_NAME, token=HF_API_KEY)

def get_embedding(text: str) -> list[float]:
    embedding = model.encode(text)
    return embedding.tolist()

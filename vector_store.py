# 1. imports
import os
import uuid
import chromadb
from dotenv import load_dotenv


# 2. load env variables (CHROMA_DB_HOST, CHROMA_DB_PORT)
load_dotenv()

CHROMA_DB_HOST = os.getenv("CHROMA_DB_HOST", "localhost")
CHROMA_DB_PORT = int(os.getenv("CHROMA_DB_PORT", 8080))

# 3. connect to chromeDb client using the host and port
client = chromadb.HttpClient(
    host=CHROMA_DB_HOST,
    port=CHROMA_DB_PORT
)   

# 4. get or create a collection in ChromaDB
collection = client.get_or_create_collection(name="rag_documents")

# 5. define a function called add_documents(chunks, embeddings)
def add_documents(chunks: list[str], embeddings: list[list[float]]):
    ids = [str(uuid.uuid4()) for _ in chunks]
    
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

# 6. define a function called search(query_embedding, top_k=5)
def search(query_embedding: list[float], top_k: int = 5) -> list[str]:
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    #return just the text chunks
    return results["documents"][0]

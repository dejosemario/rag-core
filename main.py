# 1. imports
import os
import uvicorn
import subprocess
import time
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

from chunker import chunk_text
from embeddings import get_embedding
from vector_store import add_documents, search
from llm import generate_response

# 2. load env variables (RAG_DATA_DIR, SERVER_PORT)
load_dotenv()

RAG_DATA_DIR = os.getenv("RAG_DATA_DIR", "./data")
SERVER_PORT = int(os.getenv("SERVER_PORT", 8080))

# 3. initialize FastAPI app
app = FastAPI()

# 4. create the data directory if it doesn't exist
os.makedirs(RAG_DATA_DIR, exist_ok=True)

# 5. GET /health endpoint
@app.get("/health")
def health():
    return JSONResponse(status_code=200, content={"status": "app is live!"})

# 6. POST /upload endpoint
@app.post("/upload")
async def upload(files: list[UploadFile] = File(...)):
    for file in files:
        # save the file to file direcotry
        file_path = os.path.join(RAG_DATA_DIR, file.filename)
        contents = await file.read()
        
        with open(file_path, "wb") as f:
            f.write(contents)
            
        # extract the  text from the file
        text = contents.decode("utf-8", errors="ignore")
        
        # pass text to chunker.py -> get chunks
        chunks = chunk_text(text)
        
        # get emeddings for each chunk
        embeddings = [get_embedding(chunk) for chunk in chunks]
        
        # save to ChromaDB
        add_documents(chunks, embeddings)
        
    return JSONResponse(
        status_code=200,
        content={"messages": f"{len(files)} file(s) uploaded and indexed succeessfully"}
    )
        
        

# 7. POST /prompt endpoint
class PromptRequest(BaseModel):
    query: str
    
@app.post("/prompt")
async def prompt(request: PromptRequest):
    # convert question to vector
    query_embedding = get_embedding(request.query)
    
    # search ChromaDB for relevant chunks
    context_chunks = search(query_embedding)
    
    # generate response from Gemini
    answer = generate_response(request.query, context_chunks)
    
    return JSONResponse(
        status_code=200,
        content={"answer": answer}
    )

# 8. start ChromaDB automatically
subprocess.Popen(["chroma", "run", "--port", "8000"])
time.sleep(2) 

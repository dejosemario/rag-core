# 1. imports

# 2. load env variables (RAG_DATA_DIR, SERVER_PORT)

# 3. initialize FastAPI app

# 4. create the data directory if it doesn't exist
#    - this is where uploaded files will be saved temporarily

# 5. GET /health endpoint
#    - just returns 200 with a message "app is live"

# 6. POST /upload endpoint
#    - receives uploaded files (multipart/form-data, field name: "files")
#    - for each file:
#        - save the file to RAG_DATA_DIR
#        - extract the text from the file
#        - pass text to chunker.py → get chunks
#        - pass each chunk to embeddings.py → get vectors
#        - pass chunks + vectors to vector_store.py → save to ChromaDB
#    - return success message

# 7. POST /prompt endpoint
#    - receives a question (application/json, field name: "query")
#    - convert question to vector using embeddings.py
#    - search ChromaDB using vector_store.py → get context chunks
#    - pass query + context chunks to llm.py → get answer
#    - return answer

# 8. run the app with uvicorn on SERVER_PORT

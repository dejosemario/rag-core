# 1. imports

# 2. load env variables (CHROMA_DB_HOST, CHROMA_DB_PORT)

# 3. connect to chromeDb client using the host and port

# 4. get or create a collection in ChromaDB

# 5. define a function called add_documents(chunks, embeddings)
#    - takes a list of chunks (text) and their vectors
#    - saves them into the ChromaDB collection
#    - each chunk needs a unique ID

# 6. define a function called search(query_embedding, top_k=5)
#    - takes a query vector (the question converted to numbers)
#    - searches ChromaDB for the most similar chunks
#    - returns the top 5 most relevant chunks

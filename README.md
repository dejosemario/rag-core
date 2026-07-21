# RAG Core

A Retrieval-Augmented Generation (RAG) API built with FastAPI, ChromaDB, HuggingFace embeddings, and Gemini Flash 2.5.

## Project Structure

```
rag-core/
├── main.py          # FastAPI app + all 3 endpoints
├── embeddings.py    # HuggingFace embedding logic
├── vector_store.py  # ChromaDB operations
├── chunker.py       # Semantic chunking
├── llm.py           # Gemini Flash generation
├── .env.example     # Template env file
├── .env             # Your actual secrets (never commit this)
└── requirements.txt # Python dependencies
```

## Prerequisites

- Python 3.10+
- ChromaDB running as a server
- HuggingFace API key
- Gemini API key

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/rag-core.git
   cd rag-core
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and fill in your keys:
   ```bash
   cp .env.example .env
   ```

5. Start ChromaDB in a separate terminal:
   ```bash
   chroma run --port 8000
   ```

6. Start the server:
   ```bash
   uvicorn main:app --reload --port 8080
   ```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `HF_API_KEY` | HuggingFace API key | required |
| `EMBED_MODEL_NAME` | Embedding model name | sentence-transformers/all-MiniLM-L6-v2 |
| `GEMINI_API_KEY` | Gemini API key | required |
| `LLM_MODEL_NAME` | Gemini model name | gemini-2.5-flash |
| `CHROMA_DB_HOST` | ChromaDB host | localhost |
| `CHROMA_DB_PORT` | ChromaDB port | 8000 |
| `RAG_DATA_DIR` | Directory for uploaded files | ./data |
| `CHUNK_LENGTH` | Word count per chunk | 200 |
| `SERVER_PORT` | Server port | 8080 |

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Check if server is running |
| POST | `/upload` | Upload context files (multipart/form-data, field: `files`) |
| POST | `/prompt` | Ask a question (application/json, field: `query`) |

## Testing

### Health check:
```bash
curl http://localhost:8080/health
```

### Upload a file:
```bash
curl -X POST http://localhost:8080/upload \
  -F "files=@/path/to/your/document.pdf"
```

### Ask a question:
```bash
curl -X POST http://localhost:8080/prompt \
  -H "Content-Type: application/json" \
  -d '{"query": "What is this document about?"}'
```

## How It Works

1. **Upload** — File is chunked → embedded → stored in ChromaDB
2. **Prompt** — Question is embedded → similar chunks retrieved → Gemini generates answer

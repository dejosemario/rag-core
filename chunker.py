import nltk
import os
from dotenv import load_dotenv

load_dotenv()
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

CHUNK_LENGTH = int(os.getenv("CHUNK_LENGTH", 200))

def chunk_text(text: str) -> list[str]:
    sentences = nltk.sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0 
    
    for sentence in sentences:
        word_count = len(sentence.split())
        
        if current_length + word_count > CHUNK_LENGTH and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0 
        current_chunk.append(sentence)
        current_length += word_count
        
    if current_chunk: 
        chunks.append(" ".join(current_chunk))
        
    return chunks
        
            

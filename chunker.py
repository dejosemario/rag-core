import nltk
import os
from dotenv import load_dotenv

load_dotenv()
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

CHUNK_LENGTH = int(os.getenv("CHUNK_LENGT", 200))

def chunk_text(text: str) -> list[str]:
    sentences = nltk.sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0 
    
    for sentence in sentences:
        #get the word count length with var word_count
        word_count = len(sentence.split())
        
        #loop through and check if the curreent_lenght plus the word count is greater than or equal to the chunk_lenght and current_chunk, if not
        if current_length + word_count > CHUNK_LENGTH and current_chunk:
            #if so, then appened the chunk with the current chunk and set everyhing bak to 0
            chunks.append
            

# 1. imports
import os
from google import genai
from dotenv import load_dotenv

# 2. load env variables (GEMINI_API_KEY, LLM_MODEL_NAME)
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "gemini-2.5-flash")

# 3. configure the Gemini client using the API key
client = genai.Client(api_key=GEMINI_API_KEY)


# 4. define a function called generate_response(query, context_chunks)
def generate_response(query: str, context_chunks: list[str]) -> str:
    
    context = "\n\n".join(context_chunks)
    
    # build the prompt
    prompt = f"""You are a helpful assistant. 
    Use ONLY the context below to answer the question.
    If the answer is not in the context, say "I don't have enough information to answer that."

    Context:
    {context}
    
    Question: {query}
    
    Answer:"""

    # send to Gemini and get response
    response = client.models.generate_content(        
        model=LLM_MODEL_NAME,
        contents=prompt
        )
    
    return response.text

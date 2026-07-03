import os
from dotenv import load_dotenv
import re

load_dotenv()

# --- LLM ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = "llama-3.3-70b-versatile"

# --- Embeddings ---
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# --- Vector store ---
CHROMA_COLLECTION = "pcc_math_005a_reviews"
CHROMA_PATH = "./chroma_db"

# --- Retrieval ---
N_RESULTS = 7

# --- Documents ---
DOCS_PATH = "./documents"
REVIEW_PATTERN = re.compile(r"(?m)^---\s*Review\s+(\d+)\s*---\s*$")
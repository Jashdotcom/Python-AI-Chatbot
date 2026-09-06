import os

from dotenv import load_dotenv
from openai import OpenAI
from sentence_transformers import SentenceTransformer
import chromadb

#1. Load environment variables:

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

#2. Create OpenRouter Client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

#Load Embedding model:
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

#5. Connect Chroma:
client = chromadb.PersistentClient(
    path="./chromadb"
)

collection = chroma_client.get_collection(
    name="college_rules"
)

#6. 
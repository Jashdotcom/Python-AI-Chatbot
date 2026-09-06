from sentence_transformers import SentenceTransformer
import chromadb

#1. Load Embedding model:
model = SentenceTransformer("all-MiniLM-L6-v2")

#2. Connect to chroma:
client = chromadb.PersistentClient(
    path = "./chromadb"
)

collection = client.get_collection(
    name="college_rules"
)

#3. Ask question:
question = "What is the minimum attendance requirement?"

#4. Create Embedding:
embedding = model.encode(question)

#5. Search Chroma:
results = collection.query(
    query_texts = ["What is the minimum attendance requirement?"],
    n_results = 3
)

#6. Display Results
print("\nQuestion:")
print(question)

print("\nRelevant chunks: ")

for i, document in enumerate(results["documents"][0], start=1):

    print(f"\\n---Result {i} ---")
    print(document)


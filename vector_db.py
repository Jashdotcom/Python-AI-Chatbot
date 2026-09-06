import chromadb
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="./chromadb"
)

collection = client.get_or_create_collection(
    name="college_rules"
)

documents = [ "Documents/college_rules.pdf"]

ids = [
    "chunk1",
    "chunk2",
    "chunk3"
]

collection.add(
    documents = documents,
    ids = ids
)

results = collection.query(
    query_texts = ["What attendance is required?"],
    n_results = 2
)

print("\nSearch results:")
print(results["documents"])
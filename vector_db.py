import chromadb

client = chromadb.PersistentClient(
    path="./chromadb"
)

collection = client.get_or_create_collection(
    name="college_rules"
)

documents = [
    "Students must maintain a minimum attendance of 75%.",
    "The college library is open from 8 AM to 6 PM.",
    "Students must carry their identity card inside the college."
]

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
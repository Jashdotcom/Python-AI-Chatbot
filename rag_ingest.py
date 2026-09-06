from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb

# 1. READ PDF:
pdf_path = "documents/college_rules.pdf"

reader = PdfReader(pdf_path)

all_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        text = " ".join(text.split())
        all_text += text + "\n"

# 2. CREATE CHUNKS:
chunk_size = 1000
overlap = 200

chunks = []

for i in range(0, len(all_text), chunk_size - overlap):
    chunk = all_text[i:i + chunk_size]
    chunks.append(chunk)


print("Pages:", len(reader.pages))
print("Chunks:", len(chunks))

# 3. CREATE EMBEDDINGS:
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

print("Embeddings created!")
print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))

# 4. CONNECT TO CHROMA
client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="college_rules"
)

# 5. STORE CHUNKS & EMBEDDINGS
ids = []

for i in range(len(chunks)):

    ids.append(f"chunk_{i}")


collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist()
)


print("Documents stored in Chroma!")

print("Total documents:",
      collection.count())
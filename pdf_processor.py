from pypdf import PdfReader

pdf_path = "documents/college_rules.pdf"

reader = PdfReader(pdf_path)

all_text=""

for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text()

    if text:
        all_text += text + "\n"

print("Number of pages: ", len(reader.pages))
print("\nExtracted text: ")
print(all_text)

chunk_size = 1000

chunks = []

for i in range(0, len(all_text), chunk_size):
    chunk = all_text[i:i + chunk_size]
    chunks.append(chunk)

print("Number of pages: ", len(reader.pages))
print("Number of chunks: ", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print(f"\n---Chunk {i} ---")
    print(chunk)

        
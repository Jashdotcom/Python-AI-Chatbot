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

        
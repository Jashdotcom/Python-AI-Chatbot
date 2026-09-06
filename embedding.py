from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

text1 = "Students must maintain a minimum attendance of 75%."
text2 = "What percentage of attendance is required?"
text3 = "The library is open from 8 AM to 6 PM."

embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
embedding3 = model.encode(text3)

similarity_1 = cosine_similarity(
    [embedding1],
    [embedding2],
)
similarity_2 = cosine_similarity(
    [embedding1],
    [embedding3],
)

print("Attendance vs Attendance question: ")
print(similarity_1)

print("\n Attendance vs Library: ")
print(similarity_2)
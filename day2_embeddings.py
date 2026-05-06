from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "The dog ran across the yard",
    "The puppy chased the squirrel outside",
    "Stock prices fell hard this morning",
    "The investor sold what she had invested in",
    "Kayaking in no fun when it there is lightning outside"
]

embeddings = model.encode(sentences)

print(f"Embedding shape: {embeddings.shape}")

similarity_matrix = cosine_similarity(embeddings)

labels = ["Dog-1", "Dog-2", "Finance-1", "Finance-2", "Ambiguous"]

print("\nSimilarity Scores:")
for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        score = similarity_matrix[i][j]
        print(f" {labels[i]} vs {labels[j]}: {score:.3f}")
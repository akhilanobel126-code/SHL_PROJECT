import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("catalog.json", "r", encoding="utf-8") as f:
    data = json.load(f)

index = faiss.read_index("shl_index.faiss")


def search(query, k=5):
    q_vec = model.encode([query])
    distances, indices = index.search(np.array(q_vec), k)

    results = []
    for i in indices[0]:
        results.append(data[i])

    return results


# TEST YOUR SEARCH
if __name__ == "__main__":
    query = "java developer test"
    results = search(query)

    for r in results:
        print(r["name"], "→", r["url"])


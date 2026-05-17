import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("catalog.json", "r") as f:

    data = json.load(f)

texts = []

for item in data:

    description = item.get("description", "")

    texts.append(description)

embeddings = model.encode(texts)

embeddings = np.array(embeddings)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, "shl_index.faiss")

print("FAISS index created successfully")
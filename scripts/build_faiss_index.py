import numpy as np
import faiss
import os

# Paths
embedding_path = "data/processed/patient_embeddings.npy"
index_path = "data/processed/patient_index.faiss"

print("🔍 Loading embeddings...")
embeddings = np.load(embedding_path).astype("float32")

print("⚙️ Building FAISS index...")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

print(f"💾 Saving index to {index_path}...")
faiss.write_index(index, index_path)

print("✅ FAISS index built and saved.")

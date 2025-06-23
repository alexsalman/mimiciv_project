import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

# === Configuration ===
summary_path = "data/processed/text_summaries.csv.gz"
index_path = "data/processed/patient_index.faiss"
model_name = "sentence-transformers/all-MiniLM-L6-v2"
top_k = 5
query = "elderly patient in ICU with respiratory issues and chest infiltrates"
summary_column = "text_summary"

# === Load Data ===
print("🔍 Loading FAISS index and summaries...")
df = pd.read_csv(summary_path)
df.reset_index(drop=True, inplace=True)

index = faiss.read_index(index_path)
df = df.iloc[:index.ntotal]
df.reset_index(drop=True, inplace=True)

model = SentenceTransformer(model_name)

# === Encode query and search ===
print("🔎 Searching...")
query_embedding = model.encode([query])
_, indices = index.search(query_embedding, top_k)

# === Show results ===
print("\nTop results:")
for rank, idx in enumerate(indices[0]):
    try:
        summary = df.iloc[int(idx)][summary_column]
        print(f"{rank + 1}. {summary[:300]}...\n")
    except Exception as e:
        print(f"⚠️ Error retrieving summary for index {idx}: {e}")

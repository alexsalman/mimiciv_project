import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import os

# Paths
input_path = "data/processed/text_summaries.csv.gz"
output_path = "data/processed/patient_embeddings.npy"

# Load summaries
df = pd.read_csv(input_path)

# Use correct column name
column_name = "summary" if "summary" in df.columns else df.columns[0]

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Generate embeddings
print("Generating embeddings...")
texts = df[column_name].astype(str).tolist()
embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

# Save
np.save(output_path, embeddings)
print(f"✅ Saved embeddings to {output_path}")




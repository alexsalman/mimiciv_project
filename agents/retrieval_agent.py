# agents/retrieval_agent.py

import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

class RetrievalAgent:
    def __init__(self, index_path="data/processed/patient_index.faiss", summary_path="data/processed/text_summaries.csv.gz", model_name="sentence-transformers/all-MiniLM-L6-v2"):
        print("🔍 Initializing Retrieval Agent...")
        self.index = faiss.read_index(index_path)
        self.df = pd.read_csv(summary_path)
        self.df.reset_index(drop=True, inplace=True)
        self.model = SentenceTransformer(model_name)
        print("✅ Retrieval Agent ready.")

    def retrieve(self, query: str, k: int = 5):
        print(f"🔎 Retrieving top {k} results for query: {query}")
        query_vector = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_vector, k)

        results = []
        for idx in indices[0]:
            if idx < len(self.df):
                row = self.df.iloc[idx]
                results.append({
                    "subject_id": row.get("subject_id"),
                    "hadm_id": row.get("hadm_id"),
                    "summary": row.get("text_summary", "")[:500]
                })
        return results

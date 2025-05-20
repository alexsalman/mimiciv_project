# agents/retrieval_agent.py

import re
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer

class RetrievalAgent:
    def __init__(
        self,
        index_path:   str = "data/processed/patient_index.faiss",
        summary_path: str = "data/processed/text_summaries.csv.gz",
        model_name:   str = "sentence-transformers/all-MiniLM-L6-v2"
    ):
        # load FAISS + summaries for RAG
        self.index = faiss.read_index(index_path)
        self.df    = pd.read_csv(summary_path)
        self.df.reset_index(drop=True, inplace=True)
        self.model = SentenceTransformer(model_name)

    def retrieve(self, query: str, k: int = 3):
        # 1) detect “patient id: N” queries
        m = re.search(r'patient\s*id[:\s]+(\d+)', query.lower())
        if m:
            pid = int(m.group(1))
            rows = self.df[self.df["subject_id"] == pid]
            # convert to “documents” format to match RAG API
            docs = rows["text_summary"].head(k).tolist()
            return {"documents": [docs], "ids": rows.index[:k].tolist()}

        # 2) fallback to vector‐based retrieval
        qv = self.model.encode([query])
        D, I = self.index.search(qv, k)
        docs = [ self.df.iloc[i]["text_summary"] for i in I[0] ]
        return {"documents": [docs], "ids": I[0].tolist()}

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
        self.index = faiss.read_index(index_path)
        self.df    = pd.read_csv(summary_path)
        self.df.reset_index(drop=True, inplace=True)
        self.model = SentenceTransformer(model_name)

    def retrieve(self, query: str, k: int = 3):
        # 1) patient‐ID exact lookup
        m = re.search(r"patient\s*id[:\s]+(\d+)", query.lower())
        if m:
            pid  = int(m.group(1))
            sub  = self.df[self.df["subject_id"] == pid]
            topk = sub.head(k)
        else:
            # 2) semantic‐search fallback
            qv    = self.model.encode([query])
            _, idx = self.index.search(qv, k)
            topk  = self.df.iloc[idx[0]]

        # build plain record dicts
        records = []
        for _, row in topk.iterrows():
            records.append({
                "subject_id": int(row["subject_id"]),
                "hadm_id":    int(row["hadm_id"]),
                "summary":    row["text_summary"]
            })
        return records
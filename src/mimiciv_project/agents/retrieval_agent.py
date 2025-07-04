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
        # 1) load FAISS index
        self.index = faiss.read_index(index_path)

        # 2) load the summaries DataFrame
        self.df = pd.read_csv(summary_path)
        self.df.reset_index(drop=True, inplace=True)

        # 3) sentence-transformer for query embeddings
        self.model = SentenceTransformer(model_name)

    def retrieve(self, query: str, k: int = 3):
        query_lower = query.lower()

        def make_hit(r):
            return {
                "subject_id": int(r.subject_id),
                "hadm_id":    int(r.hadm_id),
                "summary":    r.text_summary,
                "note_text":  r.text_summary,   # raw clinician note placeholder
            }

        # 1a) “Does patient id: X exhibit signs of DISEASE?”
        m = re.match(r"does patient id:\s*(\d+)\s+exhibit signs of\s+(.+?)\?", query_lower)
        if m:
            disease = m.group(2)
            mask = self.df["text_summary"].str.contains(disease, case=False, na=False)
            if mask.any():
                return [make_hit(r) for r in self.df[mask].head(k).itertuples()]
            return [{"subject_id": None, "hadm_id": None,
                     "summary": f"No mentions of {disease} found in the top {k} records.",
                     "note_text": ""}]

        # 1b) “Check for any mention of DISEASE in patient id: X”
        m2 = re.match(r"check for any mention of\s+(.+?)\s+in patient id:\s*(\d+)", query_lower)
        if m2:
            disease = m2.group(1)
            mask = self.df["text_summary"].str.contains(disease, case=False, na=False)
            if mask.any():
                return [make_hit(r) for r in self.df[mask].head(k).itertuples()]
            return [{"subject_id": None, "hadm_id": None,
                     "summary": f"No mentions of {disease} found in the top {k} records.",
                     "note_text": ""}]

        # 1c) “Is there evidence of DISEASE for patient id: X?”
        m3 = re.match(r"is there evidence of\s+(.+?)\s+for patient id:\s*(\d+)\?", query_lower)
        if m3:
            disease = m3.group(1)
            mask = self.df["text_summary"].str.contains(disease, case=False, na=False)
            if mask.any():
                return [make_hit(r) for r in self.df[mask].head(k).itertuples()]
            return [{"subject_id": None, "hadm_id": None,
                     "summary": f"No mentions of {disease} found in the top {k} records.",
                     "note_text": ""}]

        # 2) Patient-ID exact lookup
        m_id = re.search(r"patient\s*id[:\s]+(\d+)", query_lower)
        if m_id:
            pid   = int(m_id.group(1))
            subset = self.df[self.df["subject_id"] == pid].head(k)
            return [make_hit(r) for r in subset.itertuples()]

        # 3) Semantic FAISS fallback
        qv, = self.model.encode([query])
        _, idx = self.index.search(qv.reshape(1, -1), k)
        topk   = self.df.iloc[idx[0]]
        return [make_hit(r) for r in topk.itertuples()]
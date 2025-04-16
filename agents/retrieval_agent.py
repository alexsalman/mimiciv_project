# agents/retrieval_agent.py

from rag.vector_store import get_vector_db
from rag.embedder import embed_text

class RetrievalAgent:
    def __init__(self):
        self.db = get_vector_db()

    def retrieve(self, query: str, k: int = 3):
        query_vector = embed_text(query)
        results = self.db.query(query_embeddings=[query_vector], n_results=k)
        return results

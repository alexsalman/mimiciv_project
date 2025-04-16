# scripts/test_retrieval.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.retrieval_agent import RetrievalAgent
from rag.vector_store import get_vector_db
from rag.embedder import embed_text

# Create or load the vector DB
db = get_vector_db()

# Sample mock patient records (normally these come from MIMIC-IV)
patients = [
    {"id": "p1", "text": "Patient with type 2 diabetes and hypertension."},
    {"id": "p2", "text": "Patient admitted for chest pain and elevated troponin."},
    {"id": "p3", "text": "ICU patient with respiratory failure and mechanical ventilation."}
]

# Add documents to vector DB
for patient in patients:
    embedding = embed_text(patient["text"])
    db.add(
        ids=[patient["id"]],
        documents=[patient["text"]],
        embeddings=[embedding]
    )

# Test retrieval
agent = RetrievalAgent()
results = agent.retrieve("breathing problem and ICU", k=2)

for r in results['documents'][0]:
    print("Retrieved:", r)

# tests/test_retrieval_agent.py

from agents.retrieval_agent import RetrievalAgent

agent = RetrievalAgent()
results = agent.retrieve("patient with high blood pressure and chest pain", k=5)

print("\n📄 Top Results:")
for i, res in enumerate(results, 1):
    print(f"\n{i}. Patient ID: {res['subject_id']} | Admission ID: {res['hadm_id']}\nSummary: {res['summary']}")

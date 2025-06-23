# tests/test_retrieval_agent.py

from mimiciv_project.agents.retrieval_agent     import RetrievalAgent
from mimiciv_project.agents.summarization_agent import SummarizationAgent
from mimiciv_project.agents.diagnosis_agent     import DiagnosisAgent
from mimiciv_project.agents.master_agent        import MasterAgent
from mimiciv_project.utils.scoring_utils        import compute_feedback_score

agent = RetrievalAgent()
results = agent.retrieve("patient with high blood pressure and chest pain", k=5)

print("\n📄 Top Results:")
for i, res in enumerate(results, 1):
    print(f"\n{i}. Patient ID: {res['subject_id']} | Admission ID: {res['hadm_id']}\nSummary: {res['summary']}")

# scripts/test_master_agent.py

from mimiciv_project.agents.retrieval_agent     import RetrievalAgent
from mimiciv_project.agents.summarization_agent import SummarizationAgent
from mimiciv_project.agents.diagnosis_agent     import DiagnosisAgent
from mimiciv_project.agents.master_agent        import MasterAgent
from mimiciv_project.utils.scoring_utils        import compute_feedback_score

query = "elderly patient in ICU with respiratory issues and chest infiltrates"

agent = MasterAgent()
response = agent.handle_query(query)

print("\n✅ Final Response:")
print("Summary:", response["summary"])
print("Diagnoses:", response["diagnoses"])
print("Feedback Score:", response["feedback_score"])

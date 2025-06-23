# tests/test_summarization_agent.py

from mimiciv_project.agents.retrieval_agent     import RetrievalAgent
from mimiciv_project.agents.summarization_agent import SummarizationAgent
from mimiciv_project.agents.diagnosis_agent     import DiagnosisAgent
from mimiciv_project.agents.master_agent        import MasterAgent
from mimiciv_project.utils.scoring_utils        import compute_feedback_score

print("🧠 Initializing Summarization Agent...")
agent = SummarizationAgent()
print("✅ Summarization Agent ready.")

sample_text = """
The patient is a 67-year-old female admitted for evaluation of chest pain. She has a history of hypertension,
diabetes, and prior myocardial infarction. ECG shows ST depressions. Troponin is elevated. She is started on aspirin,
heparin, and nitroglycerin. Cardiology is consulted for possible catheterization.
"""

print("📝 Original Text:")
print(sample_text)

summary = agent.summarize(sample_text)
print("\n🧾 Summary:")
print(summary)

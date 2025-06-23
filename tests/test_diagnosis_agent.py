# tests/test_diagnosis_agent.py

from mimiciv_project.agents.retrieval_agent     import RetrievalAgent
from mimiciv_project.agents.summarization_agent import SummarizationAgent
from mimiciv_project.agents.diagnosis_agent     import DiagnosisAgent
from mimiciv_project.agents.master_agent        import MasterAgent
from mimiciv_project.utils.scoring_utils        import compute_feedback_score

print("🧠 Initializing Diagnosis Agent...")
agent = DiagnosisAgent()
print("✅ Diagnosis Agent ready.")

sample_summary = """
The patient is a 67-year-old female who has been admitted due to chest pain. 
She has a known history of hypertension, diabetes, and prior myocardial infarction. 
ECG shows ST depressions and elevated troponin levels. She is on aspirin, heparin, and nitroglycerin.
"""

print("📝 Patient Summary:")
print(sample_summary.strip())

print("\n🩺 Diagnosing...")
diagnosis = agent.diagnose(sample_summary)

print("\n💡 Possible Diagnoses:\n")
print(diagnosis)

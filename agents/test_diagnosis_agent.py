# agents/test_diagnosis_agent.py

from agents.diagnosis_agent import DiagnosisAgent

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

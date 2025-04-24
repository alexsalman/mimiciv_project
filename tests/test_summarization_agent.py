# tests/test_summarization_agent.py

from agents.summarization_agent import SummarizationAgent

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

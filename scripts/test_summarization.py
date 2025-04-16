# scripts/test_summarization.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.summarization_agent import SummarizationAgent

text = """
72-year-old male admitted to ICU with shortness of breath and abnormal ABG values. 
CXR shows bilateral infiltrates. Oxygen saturation dropped to 85%. 
Started on BiPAP and later transitioned to mechanical ventilation.
"""

agent = SummarizationAgent(model="mistral")
summary = agent.summarize(text)

print("📝 Summary:\n", summary)

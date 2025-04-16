# scripts/test_diagnosis.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.diagnosis_agent import DiagnosisAgent

summary = """
The 72-year-old male patient is in the ICU due to respiratory distress. Chest X-ray shows bilateral infiltrates. 
Oxygen saturation dropped to 85%. Required BiPAP and mechanical ventilation.
"""

agent = DiagnosisAgent(model="gemma")
diagnosis = agent.diagnose(summary)

print("🩺 Possible Diagnoses:\n", diagnosis)

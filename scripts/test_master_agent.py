# scripts/test_master_agent.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.master_agent import MasterAgent

query = "elderly patient in ICU with respiratory issues and chest infiltrates"

agent = MasterAgent()
response = agent.handle_query(query)

print("\n✅ Final Response:")
print("Summary:", response["summary"])
print("Diagnoses:", response["diagnoses"])
print("Feedback Score:", response["feedback_score"])

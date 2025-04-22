# agents/test_master_agent.py

from agents.master_agent import MasterAgent

print("🧠 Initializing Master Agent...")
agent = MasterAgent()
print("✅ Master Agent ready.")

# Sample user query
query = "elderly patient with shortness of breath and chest X-ray showing infiltrates"
print(f"\n🤖 User Query: {query}")

response = agent.handle_query(query)

print("\n✅ Final Output:")
print("📝 Summary:", response["summary"])
print("\n🩺 Diagnoses:", response["diagnoses"])
print("\n📊 Feedback Score:", response["feedback_score"])

# agents/master_agent.py

from agents.retrieval_agent import RetrievalAgent
from agents.summarization_agent import SummarizationAgent
from agents.diagnosis_agent import DiagnosisAgent
from utils.scoring_utils import compute_feedback_score

class MasterAgent:
    def __init__(self):
        print("🧠 Initializing Master Agent...")
        self.retrieval_agent = RetrievalAgent()
        self.summarizer      = SummarizationAgent(model="mistral")
        self.diagnoser       = DiagnosisAgent(model="gemma")
        print("✅ Master Agent ready.")

    def handle_query(self, query: str, top_k: int = 3):
        # 1) Retrieval
        print(f"\n🔍 Retrieving top {top_k} similar cases for query: {query}")
        retrieved = self.retrieval_agent.retrieve(query, k=top_k)

        # 2) Summarization
        combined = "\n".join(
            rec.get("summary", rec.get("text_summary")) for rec in retrieved
        )
        print("\n📝 Summarizing patient data...")
        summary = self.summarizer.summarize(combined)

        # 3) Diagnosis
        print("\n🩺 Suggesting possible diagnoses...")
        diagnoses = self.diagnoser.diagnose(summary)

        # 4) Feedback scoring
        score = compute_feedback_score(diagnoses)

        # 5) Return structured result
        return {
            "summary":       summary,
            "diagnoses":     diagnoses,
            "feedback_score": score
        }

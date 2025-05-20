# agents/master_agent.py

from utils.feedback_logger       import log_feedback
from agents.retrieval_agent      import RetrievalAgent
from agents.summarization_agent  import SummarizationAgent
from agents.diagnosis_agent      import DiagnosisAgent

class MasterAgent:
    def __init__(self):
        print("🧠 Initializing Master Agent...")
        self.retrieval_agent = RetrievalAgent()
        self.summarizer      = SummarizationAgent(model="mistral")
        self.diagnoser       = DiagnosisAgent(model="gemma")
        print("✅ Master Agent ready.")

    def handle_query(self, query: str, top_k: int = 3):
        print(f"\n🔍 Retrieving top {top_k} results for query: {query}")
        out    = self.retrieval_agent.retrieve(query, k=top_k)
        text   = "\n\n".join(out["documents"][0])

        print("\n📝 Summarizing patient data...")
        summary = self.summarizer.summarize(text)

        print("\n🩺 Suggesting possible diagnoses...")
        diagnoses = self.diagnoser.diagnose(summary)

        # simple keyword‐based feedback
        feedback = 1.0 if "diagnosis" in diagnoses.lower() else 0.5
        log_feedback(query, summary, diagnoses, feedback)

        return {
            "summary":       summary,
            "diagnoses":     diagnoses,
            "feedback_score": feedback
        }

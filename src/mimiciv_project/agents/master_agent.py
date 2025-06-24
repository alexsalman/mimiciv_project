from mimiciv_project.utils.feedback_logger import log_feedback
from mimiciv_project.utils.scoring_utils import compute_feedback_score
from mimiciv_project.agents.retrieval_agent import RetrievalAgent
from mimiciv_project.agents.summarization_agent import SummarizationAgent
from mimiciv_project.agents.diagnosis_agent import DiagnosisAgent

class MasterAgent:
    def __init__(self):
        print("🧠 Initializing Master Agent...")
        self.retrieval_agent = RetrievalAgent()
        self.summarizer      = SummarizationAgent(model="mistral")
        self.diagnoser       = DiagnosisAgent(model="gemma")
        print("✅ Master Agent ready.")

    def handle_query(self, query: str, top_k: int = 3):
        # 1) Retrieval
        print(f"\n🔍 Retrieving top {top_k} results for query: {query}")
        records = self.retrieval_agent.retrieve(query, k=top_k)

        # 2) Summarization
        text_blob = "\n".join(r["summary"] for r in records)
        summary = self.summarizer.summarize(text_blob, query=query)
        print(summary)

        # 3) Decide if we should skip diagnosis/scoring
        ql = query.lower()
        extract_triggers = ["extract", "list", "report", "does patient id"]
        if any(qt in ql for qt in extract_triggers):
            # Extraction‐only: skip diagnosis and scoring
            log_feedback(query, summary, None, None)
            return {"summary": summary, "diagnoses": None, "feedback_score": None}

        # 4) Diagnosis
        print("\n🩺 Suggesting possible diagnoses…")
        diagnoses = self.diagnoser.diagnose(summary)
        print(diagnoses)

        # 5) Feedback scoring
        feedback_score = compute_feedback_score(diagnoses)

        # 6) Log feedback
        log_feedback(query, summary, diagnoses, feedback_score)

        return {
            "summary":       summary,
            "diagnoses":     diagnoses,
            "feedback_score": feedback_score
        }
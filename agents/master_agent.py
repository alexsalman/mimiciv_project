# agents/master_agent.py

from utils.feedback_logger import log_feedback
from utils.scoring_utils import compute_feedback_score
from agents.retrieval_agent import RetrievalAgent
from agents.summarization_agent import SummarizationAgent
from agents.diagnosis_agent import DiagnosisAgent

class MasterAgent:
    def __init__(self):
        self.retrieval_agent = RetrievalAgent()
        self.summarizer = SummarizationAgent(model="mistral")
        self.diagnoser = DiagnosisAgent(model="gemma")

    def handle_query(self, query: str):
        print("\n🔍 Retrieving relevant patient records...")
        retrieved = self.retrieval_agent.retrieve(query, k=2)
        text = " ".join(retrieved[0]) if retrieved else "No data retrieved."

        print("\n📝 Summarizing patient data...")
        summary = self.summarizer.summarize(text)
        print(summary)

        print("\n🩺 Suggesting possible diagnoses...")
        diagnoses = self.diagnoser.diagnose(summary)
        print(diagnoses)

        # 🧠 Basic feedback score logic
        feedback_score = compute_feedback_score(diagnoses)
        
        log_feedback(query, summary, diagnoses, feedback_score)

        return {
            "summary": summary,
            "diagnoses": diagnoses,
            "feedback_score": feedback_score
        }

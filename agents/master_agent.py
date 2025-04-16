# agents/master_agent.py

from utils.feedback_logger import log_feedback
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
        text = " ".join(retrieved['documents'][0])

        print("\n📝 Summarizing patient data...")
        summary = self.summarizer.summarize(text)
        print(summary)

        print("\n🩺 Suggesting possible diagnoses...")
        diagnoses = self.diagnoser.diagnose(summary)
        print(diagnoses)

        # 🧠 Basic feedback score logic
        feedback_score = 1.0 if "diagnosis" in diagnoses.lower() else 0.5
        
        log_feedback(query, summary, diagnoses, feedback_score)

        return {
            "summary": summary,
            "diagnoses": diagnoses,
            "feedback_score": feedback_score
        }

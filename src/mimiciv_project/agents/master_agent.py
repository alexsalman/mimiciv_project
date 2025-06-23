# src/mimiciv_project/agents/master_agent.py

from mimiciv_project.agents.retrieval_agent import RetrievalAgent
from mimiciv_project.agents.summarization_agent import SummarizationAgent
from mimiciv_project.agents.diagnosis_agent import DiagnosisAgent
from mimiciv_project.utils.scoring_utils import compute_feedback_score
from mimiciv_project.utils.feedback_logger  import log_feedback

class MasterAgent:
    def __init__(self):
        print("🧠 Initializing Master Agent...")
        self.retrieval_agent = RetrievalAgent()
        self.summarizer       = SummarizationAgent(model="mistral")
        self.diagnoser        = DiagnosisAgent(model="gemma")
        print("✅ Master Agent ready.")

    def handle_query(self, query: str, top_k: int = 3):
        # 1) Retrieve
        print(f"\n🔍 Retrieving top {top_k} results for query: {query}")
        retrieved = self.retrieval_agent.retrieve(query, k=top_k)

        # 2) Extract summaries whether retrieve() gave a dict or list
        if isinstance(retrieved, dict) and "documents" in retrieved:
            docs = retrieved["documents"][0]
        elif isinstance(retrieved, list):
            # test‐style: list of record‐dicts with 'summary' key
            docs = []
            for r in retrieved[:top_k]:
                if "summary" in r:
                    docs.append(r["summary"])
                elif "text_summary" in r:
                    docs.append(r["text_summary"])
                else:
                    raise KeyError(f"No summary field in record: {r.keys()}")
        else:
            raise TypeError(f"Unexpected retrieve() return type: {type(retrieved)}")

        text = " ".join(docs)

        # 3) Summarize
        print("\n📝 Summarizing patient data...")
        summary = self.summarizer.summarize(text)
        print(summary)

        # 4) Diagnose
        print("\n🩺 Suggesting possible diagnoses...")
        diagnoses = self.diagnoser.diagnose(summary)
        print(diagnoses)

        # 5) Score
        feedback_score = compute_feedback_score(diagnoses)

        # 6) Log
        log_feedback(query, summary, diagnoses, feedback_score)

        return {
            "summary":        summary,
            "diagnoses":      diagnoses,
            "feedback_score": feedback_score
        }
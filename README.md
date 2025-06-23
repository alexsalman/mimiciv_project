# mimiciv_project

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**No Cloud, No Problem:** Secure & Explainable Offline AI Agents  
for Clinical Q&A with Lightweight LLMs

---

## 🚀 Quick Start

```bash
git clone https://github.com/alexsalman/mimiciv_project.git
cd mimiciv_project
pip install -r requirements.txt
pip install -e .

📦 Installation
	1.	Clone the repo
	2.	Activate your Python 3.8+ environment
	3.	Install dependencies:
      pip install -r requirements.txt
      pip install -e .

🖥️ Usage
mimiciv-cli "elderly patient with chest pain and cough" -k 3

Python API
from mimiciv_project.agents.master_agent import MasterAgent

agent = MasterAgent()
out = agent.handle_query("ICU patient with sepsis and hypotension", top_k=2)
print("Summary:",        out["summary"])
print("Diagnoses:",      out["diagnoses"])
print("Feedback Score:", out["feedback_score"])

📂 Project Structure
mimiciv_project/
├── src/mimiciv_project/
│   ├── agents/              # Retrieval, Summarization, Diagnosis, MasterAgent
│   ├── utils/               # scoring_utils, feedback_logger, etc.
│   └── cli.py               # `mimiciv-cli` entrypoint
├── data/
│   ├── raw/                 # original MIMIC-IV CSVs
│   └── processed/           # summaries, embeddings, FAISS index
├── scripts/                 # ETL & embedding-generation scripts
├── notebooks/               # profiling & demo notebooks
├── tests/                   # pytest unit tests
├── requirements.txt
├── pyproject.toml
└── README.md

✔️ Completed Tasks
	•	Data acquisition
Downloaded MIMIC-IV v3.1 full dataset (credentialed PhysioNet access).
	•	Raw data inspection & exploration
• patients.csv.gz, admissions.csv.gz, diagnoses_icd.csv.gz (hosp)
• icustays.csv.gz, chartevents.csv.gz (icu)
	•	Merging & preview
Joined patients + icustays on subject_id; mapped key itemid labels.
	•	Text-summary preparation
Built per-admission summaries → data/processed/text_summaries.csv.gz.
	•	Embedding generation
Encoded summaries with SentenceTransformer → data/processed/patient_embeddings.npy.
	•	FAISS index building
Created & saved data/processed/patient_index.faiss for nearest-neighbor retrieval.
	•	Retrieval Agent
Wrapped FAISS lookup (and patient-ID override) in src/mimiciv_project/agents/retrieval_agent.py.
	•	Summarization Agent
HTTP-based Ollama/Mistral client in src/mimiciv_project/agents/summarization_agent.py.
	•	Diagnosis Agent
HTTP-based Ollama/Gemma client in src/mimiciv_project/agents/diagnosis_agent.py.
	•	Composite Feedback Scoring
Keyword & acronym-based rubric in src/mimiciv_project/utils/scoring_utils.py.
	•	MasterAgent Orchestration
src/mimiciv_project/agents/master_agent.py tying retrieval → summarization → diagnosis → scoring.
	•	CLI Demo
src/mimiciv_project/cli.py for offline querying (mimiciv-cli "<prompt>" -k N).
	•	Notebook Demo & Profiling
Jupyter notebooks measuring runtimes and plotting stage breakdowns.

🎯 Next Steps
	1.	Enhance feedback-scorer with clinician-validated weights
	2.	Add direct patient-ID lookup workflow in MasterAgent
	3.	Build a lightweight GUI for interactive clinical use
	4.	Fine-tune LLMs on medical-specific corpora
	5.	Prepare conference submission manuscript

⸻

📄 Citation

If you use this work, please cite:

Salman A., et al. “No Cloud, No Problem: Secure & Explainable Offline AI Agents for Clinical Q&A with Lightweight LLMs.” 2025.

© 2025 Ali Salman · MIT License
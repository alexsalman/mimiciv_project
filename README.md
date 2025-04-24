## Completed Tasks

- [x] **Data acquisition**  
  Downloaded MIMIC-IV v3.1 full dataset (credentialed PhysioNet access).

- [x] **Raw data inspection & exploration**  
  • `patients.csv.gz`, `admissions.csv.gz`, `diagnoses_icd.csv.gz` (hosp)  
  • `icustays.csv.gz`, `chartevents.csv.gz` (icu)

- [x] **Merging & preview**  
  Joined `patients` + `icustays` on `subject_id`; mapped key `itemid` labels.

- [x] **Text‐summary preparation**  
  Built per‐admission summaries → `data/processed/text_summaries.csv.gz`.

- [x] **Embedding generation**  
  Encoded summaries with SentenceTransformer → `patient_embeddings.npy`.

- [x] **FAISS index building**  
  Created & saved `patient_index.faiss` for nearest‐neighbor retrieval.

- [x] **Retrieval agent**  
  Wrapped FAISS lookup in `agents/retrieval_agent.py`.

- [x] **Summarization agent**  
  HTTP‐based Ollama call to Mistral in `agents/summarization_agent.py`.

- [x] **Diagnosis agent**  
  HTTP‐based Ollama call to Gemma in `agents/diagnosis_agent.py`.

- [x] **Composite feedback scoring**  
  `utils/scoring_utils.py` combining rubric weights + floor/cap logic.

- [x] **MasterAgent orchestration**  
  `agents/master_agent.py` tying retrieval → summarization → diagnosis → scoring.

- [x] **CLI demo**  
  `cli.py` for offline querying (`./cli.py "<prompt>" -k N`).

- [x] **Notebook demo & profiling**  
  Cells 1–6 measuring stage runtimes and plotting feedback scores.

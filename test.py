# test.py

import json
from pathlib import Path

# --- 1) Define fixed patient IDs for evaluation ---
# These specific IDs will be used for all context-bound queries
patient_ids = [12374058, 14256548, 16874298]

# ensure results folder exists
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

# save specified IDs
ids_path = results_dir / "test_patient_ids.json"
with open(ids_path, "w") as f:
    json.dump(patient_ids, f, indent=2)
print(f"Fixed patient IDs saved to {ids_path}")

# For context-bound prompts, use the first ID
context_id = patient_ids[0]

# --- 2) Build CLI queries list ---
queries = []

# A) Patient-ID queries (k=1, embed each ID)
for pid in patient_ids:
    queries.append({
        "query": f"patient id: {pid}",
        "k": 1
    })

# B) Disease-Keyword Probing (context-bound)
queries += [
    {"query": f"Does patient id: {context_id} exhibit signs of sepsis?", "k": 3},
    {"query": f"Is there evidence of acute respiratory distress syndrome for patient id: {context_id}?", "k": 3},
    {"query": f"Check for any mention of acute myocardial infarction in patient id: {context_id}", "k": 3},
]

# C) General Clinical Summary (context-bound)
queries += [
    {"query": f"Provide a concise summary of patient id: {context_id}’s ICU stay", "k": 3},
    {"query": f"Summarize key events and interventions during the first 48 hours for patient id: {context_id}", "k": 3},
    {"query": f"Give me a narrative focusing on comorbidities and treatments for patient id: {context_id}", "k": 3},
]

# D) Vitals Extraction (context-bound)
queries += [
    {"query": f"Extract heart rate, blood pressure, respiratory rate, temperature, and SpO2 on admission for patient id: {context_id}", "k": 3},
    {"query": f"List all SpO2 readings with timestamps from patient id: {context_id} record", "k": 3},
    {"query": f"Report patient id: {context_id}’s mean arterial pressure trend on day one", "k": 3},
]

# E) Laboratory Results (context-bound)
queries += [
    {"query": f"Which lab values were most abnormal on admission for patient id: {context_id}?", "k": 3},
    {"query": f"List creatinine, BUN, and electrolytes with values and dates for patient id: {context_id}", "k": 3},
    {"query": f"Extract the first arterial blood gas result for patient id: {context_id}", "k": 3},
]

# F) Interventions & Medications (context-bound)
queries += [
    {"query": f"What medications were started within 6 hours of ICU admission for patient id: {context_id}?", "k": 3},
    {"query": f"List all vasopressors and ventilator settings used for patient id: {context_id}", "k": 3},
    {"query": f"Describe the timing and dosing of antibiotic administration for patient id: {context_id}", "k": 3},
]

# G) Diagnostic Reasoning (context-bound)
queries += [
    {"query": f"List the top 3 differential diagnoses with rationale for patient id: {context_id}", "k": 3},
    {"query": f"What evidence in the note supports a diagnosis of sepsis for patient id: {context_id}?", "k": 3},
    {"query": f"Identify signs of acute kidney injury and explain your reasoning for patient id: {context_id}", "k": 3},
]

# H) Timeline & Trends (context-bound)
queries += [
    {"query": f"Create a timeline of key events (intubation, dialysis, vasopressors) for patient id: {context_id}", "k": 3},
    {"query": f"How did lactate levels change over time for patient id: {context_id}?", "k": 3},
    {"query": f"Summarize daily SOFA scores for the first three days for patient id: {context_id}", "k": 3},
]

# --- 3) Save queries for evaluation ---
queries_path = results_dir / "cli_eval_queries.json"
with open(queries_path, "w") as f:
    json.dump(queries, f, indent=2)
print(f"CLI evaluation queries saved to {queries_path}")

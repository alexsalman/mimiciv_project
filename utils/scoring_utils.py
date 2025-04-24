# utils/scoring_utils.py

from typing import Dict

# Hard‐coded weights for core clinical conditions
WEIGHT_MAP: Dict[str, float] = {
    "acute myocardial infarction":       1.0,
    "ami":                               1.0,
    "copd exacerbation":                0.6,
    "hypertension":                     0.1,
    "cad":                               0.5,
    # New entries:
    "pneumonia":                         0.7,
    "community-acquired pneumonia":      0.8,
    "sepsis":                            1.0,
    "acute respiratory distress":        0.8,
    "ards":                              0.8,
    "respiratory failure":               0.6,
}

def compute_feedback_score(diagnoses: str) -> float:
    """
    Scan the diagnoses text for known keywords/acronyms, sum their weights,
    cap at 1.0, and enforce a floor of 0.1 if nothing matches.
    """
    text = diagnoses.lower()
    score = 0.0
    for key, wt in WEIGHT_MAP.items():
        if key in text:
            score += wt

    if score <= 0:
        return 0.1
    return round(min(score, 1.0), 3)

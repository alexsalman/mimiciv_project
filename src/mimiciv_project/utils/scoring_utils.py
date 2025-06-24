# src/mimiciv_project/utils/scoring_utils.py

from typing import Dict, Set
from pathlib import Path

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

# Load all ICD keyword phrases for extra coverage
ICD_KEYWORDS: Set[str] = set()
icd_file = Path(__file__).parents[3] / "data" / "processed" / "icd_keywords.txt"
if icd_file.exists():
    with icd_file.open("r", encoding="utf-8") as f:
        for line in f:
            kw = line.strip().lower()
            if kw:
                ICD_KEYWORDS.add(kw)

def compute_feedback_score(diagnoses: str) -> float:
    """
    Scan the diagnoses text for:
      1) high‐value keywords/acronyms in WEIGHT_MAP, and
      2) any ICD keyword matches from ICD_KEYWORDS (each counts as 0.01)
    Sum the weights, cap at 1.0, and enforce a floor of 0.1 if nothing matches.
    """
    text = diagnoses.lower()
    score = 0.0

    # 1) core condition weights
    for key, wt in WEIGHT_MAP.items():
        if key in text:
            score += wt

    # 2) bonus for any ICD keyword hits
    #    (small weight per distinct phrase, up to 0.1 total)
    hits = 0
    for kw in ICD_KEYWORDS:
        if kw in text:
            hits += 1
    if hits:
        # allocate up to 0.1 across ICD matches
        bonus = min(hits * 0.01, 0.1)
        score += bonus

    # apply floor / ceiling
    if score <= 0:
        return 0.1
    return round(min(score, 1.0), 3)
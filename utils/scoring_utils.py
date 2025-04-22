# utils/scoring_utils.py

def compute_feedback_score(diagnoses: str, icd_keywords_path="data/processed/icd_keywords.txt") -> float:
    """
    Computes a basic feedback score based on whether the diagnosis output contains known ICD keyword phrases.
    """
    try:
        with open(icd_keywords_path, "r") as f:
            keywords = set([line.strip().lower() for line in f.readlines()])
    except FileNotFoundError:
        print(f"⚠️ ICD keywords file not found at: {icd_keywords_path}")
        return 0.5  # Default score

    found = sum(1 for kw in keywords if kw in diagnoses.lower())
    score = min(1.0, found / 5) if found else 0.5
    return round(score, 2)

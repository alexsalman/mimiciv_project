# utils/feedback_logger.py

import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("results/feedback_log.json")

def log_feedback(query, summary, diagnoses, score):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "summary": summary,
        "diagnoses": diagnoses,
        "feedback_score": score
    }

    if LOG_FILE.exists():
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

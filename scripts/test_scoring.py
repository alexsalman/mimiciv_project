# scripts/test_scoring.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.scoring_utils import compute_feedback_score

examples = [
    "- **Acute myocardial infarction (AMI)**: Consistent with ECG changes and enzymes.",
    "- **COPD exacerbation**: Worsening dyspnea, increased sputum production.",
    "No valid diagnosis here."
]

for ex in examples:
    score = compute_feedback_score(ex)
    print(f"Input: {ex}\n→ Score: {score}\n")

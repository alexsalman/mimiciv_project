# tests/test_scoring_utils.py

import pytest
from utils.scoring_utils import compute_feedback_score

@pytest.mark.parametrize("diag,expected", [
    ("- **Acute myocardial infarction (AMI)**: ECG changes", 1.0),
    ("- **COPD exacerbation**: Worsening dyspnea", 0.6),
    ("No valid diagnosis here.", 0.1),
    ("Possible cad and ami present", 1.0),  # both acronyms
    ("Just mentions hypertension", 0.1),     # not in acronyms map
])
def test_compute_feedback_score(diag, expected):
    score = compute_feedback_score(diag)
    assert pytest.approx(score, rel=1e-2) == expected

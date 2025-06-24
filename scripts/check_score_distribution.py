import random
import pandas as pd
from mimiciv_project.utils.scoring_utils import compute_feedback_score, ICD_KEYWORDS

# load a random 1 000 summaries
df = pd.read_csv("data/processed/text_summaries.csv.gz", usecols=["text_summary"]).sample(1000, random_state=42)
scores = df["text_summary"].apply(compute_feedback_score)

# tally
floor = (scores == 0.1).sum()
cap   = (scores == 1.0).sum()
mid   = len(scores) - floor - cap

print(f"Score distribution over 1k samples:")
print(f"  floor (0.1): {floor} ({floor/10:.1f}%)")
print(f"  mid-range (0.1<score<1.0): {mid} ({mid/10:.1f}%)")
print(f"  cap (1.0): {cap} ({cap/10:.1f}%)")
print()
print(f"Number of ICD keywords loaded: {len(ICD_KEYWORDS)}")
print(f"Sample ICD keywords: {list(ICD_KEYWORDS)[:10]}")
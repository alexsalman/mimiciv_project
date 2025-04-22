# notebooks/load_data.py

import os
import pandas as pd

# Step 1: Check file paths
required_files = [
    "data/raw/icu/chartevents.csv.gz",
    "data/raw/hosp/patients.csv.gz",
    "data/raw/hosp/admissions.csv.gz",
    "data/raw/hosp/diagnoses_icd.csv.gz"
]

for path in required_files:
    if os.path.exists(path):
        print(f"✅ Found: {path}")
    else:
        print(f"❌ Missing: {path}")

# Step 2: Proceed with loading if all files are found
# patients_df = pd.read_csv("../data/raw/hosp/patients.csv.gz")
# ...

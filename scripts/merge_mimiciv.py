import pandas as pd

# Define file paths
patients_path = "data/raw/hosp/patients.csv.gz"
admissions_path = "data/raw/hosp/admissions.csv.gz"
diagnoses_path = "data/raw/hosp/diagnoses_icd.csv.gz"
chartevents_path = "data/raw/icu/chartevents.csv.gz"

# Load datasets
patients_df = pd.read_csv(patients_path, compression='gzip')
admissions_df = pd.read_csv(admissions_path, compression='gzip')
diagnoses_df = pd.read_csv(diagnoses_path, compression='gzip')

# Merge step-by-step
merged_df = pd.merge(admissions_df, patients_df, on="subject_id", how="left")
merged_df = pd.merge(merged_df, diagnoses_df, on=["subject_id", "hadm_id"], how="left")

# Preview result
print(merged_df.shape)
print(merged_df.head())

merged_df.to_csv("data/processed/merged_hosp.csv.gz", index=False, compression="gzip")


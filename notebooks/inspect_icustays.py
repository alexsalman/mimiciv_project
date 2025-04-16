# notebooks/inspect_icustays.py

import pandas as pd

icustays_path = "data/raw/icu/icustays.csv.gz"
icu_df = pd.read_csv(icustays_path)

print(icu_df.shape)
print(icu_df.dtypes)
print(icu_df.head())

patients_path = "data/raw/hosp/patients.csv.gz"
patients_df = pd.read_csv(patients_path)

merged_df = pd.merge(icu_df, patients_df, on="subject_id", how="left")

print(merged_df.shape)
print(merged_df[["subject_id", "hadm_id", "stay_id", "gender", "anchor_age", "intime", "outtime"]].head())

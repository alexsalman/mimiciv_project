# notebooks/inspect_patients.py

import pandas as pd

patients_path = "data/raw/hosp/patients.csv.gz"
patients_df = pd.read_csv(patients_path)

print(patients_df.shape)
print(patients_df.dtypes)
print(patients_df.head())

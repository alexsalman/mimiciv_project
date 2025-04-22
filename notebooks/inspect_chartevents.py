# notebooks/inspect_chartevents.py

import pandas as pd

chartevents_path = "data/raw/icu/chartevents.csv.gz"
chartevents_df = pd.read_csv(chartevents_path, nrows=100000)  # load first 100k rows

print(chartevents_df.shape)
print(chartevents_df.dtypes)
print(chartevents_df.head())
print(chartevents_df["itemid"].value_counts().head(10))

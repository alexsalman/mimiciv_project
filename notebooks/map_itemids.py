# notebooks/map_itemids.py

import pandas as pd

d_items_path = "data/raw/icu/d_items.csv.gz"
d_items_df = pd.read_csv(d_items_path)

print(d_items_df[d_items_df["itemid"].isin([227969, 220045, 220277, 220210, 220048, 220181, 220179, 220180, 224650, 227958])])

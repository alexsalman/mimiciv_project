import pandas as pd

# Paths to input files
diagnoses_path = "data/raw/hosp/diagnoses_icd.csv.gz"
desc_path = "data/raw/hosp/d_icd_diagnoses.csv.gz"
output_path = "data/processed/icd_keywords.txt"

# Load data
diagnoses_df = pd.read_csv(diagnoses_path)
desc_df = pd.read_csv(desc_path)

# Merge to get long titles
merged_df = pd.merge(diagnoses_df, desc_df, on=["icd_code", "icd_version"], how="left")

# Extract and clean unique titles
keywords = (
    merged_df["long_title"]
    .dropna()
    .str.lower()
    .str.replace(r"[^a-zA-Z0-9\s]", "", regex=True)  # remove punctuation
    .str.strip()
    .unique()
)

# Save to text file
with open(output_path, "w") as f:
    for kw in sorted(keywords):
        f.write(f"{kw}\n")

print(f"✅ Saved {len(keywords)} ICD keyword phrases to {output_path}")

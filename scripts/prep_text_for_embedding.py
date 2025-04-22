import pandas as pd

# Load merged hospital data (you already created this earlier)
merged_path = "data/processed/merged_hosp.csv.gz"
df = pd.read_csv(merged_path)

# Drop rows with missing hadm_id or subject_id just in case
df = df.dropna(subset=["subject_id", "hadm_id"])

# Optional: map ICD-9/10 codes to descriptions later if needed

def build_summary(row):
    parts = [
        f"Patient ID: {row['subject_id']}",
        f"Age: {row['anchor_age']}",
        f"Gender: {row['gender']}",
        f"Admission Type: {row['admission_type']}",
        f"Admission Time: {row['admittime']}",
        f"Discharge Time: {row['dischtime']}",
        f"Diagnoses: {row['icd_code']} (ICD version {row['icd_version']})"
    ]
    return " | ".join([str(p) for p in parts if pd.notnull(p)])

# Create the text summary
df["text_summary"] = df.apply(build_summary, axis=1)

# Save for embedding later
output_path = "data/processed/text_summaries.csv.gz"
df[["subject_id", "hadm_id", "text_summary"]].to_csv(output_path, index=False)

print(f"Saved {len(df)} patient summaries to {output_path}")

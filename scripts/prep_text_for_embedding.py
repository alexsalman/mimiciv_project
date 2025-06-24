import pandas as pd

# Load merged hospital data (you already created this earlier)
merged_path = "data/processed/merged_hosp.csv.gz"
df = pd.read_csv(merged_path)

# Drop rows with missing hadm_id or subject_id just in case
df = df.dropna(subset=["subject_id", "hadm_id"])

def build_summary(row):
    parts = [
        f"Patient ID: {row['subject_id']}",
        f"Age: {row['anchor_age']}",
        f"Gender: {row['gender']}",
        f"Admission Type: {row['admission_type']}",
        f"Admission Time: {row['admittime']}",
        f"Discharge Time: {row['dischtime']}",
    ]

    # Insert vital signs if available
    vitals = []
    if pd.notnull(row.get("heart_rate")):
        vitals.append(f"HR: {int(row['heart_rate'])} bpm")
    if pd.notnull(row.get("sys_bp")) and pd.notnull(row.get("dia_bp")):
        vitals.append(f"BP: {int(row['sys_bp'])}/{int(row['dia_bp'])} mmHg")
    if pd.notnull(row.get("spo2")):
        vitals.append(f"SpO₂: {int(row['spo2'])}%")
    if vitals:
        parts.append("Vitals on admission: " + ", ".join(vitals))

    # Diagnoses
    parts.append(f"Diagnoses: {row['icd_code']} (ICD v{row['icd_version']})")

    return " | ".join(parts)

# Create the text summary
df["text_summary"] = df.apply(build_summary, axis=1)

# Save for embedding later
output_path = "data/processed/text_summaries.csv.gz"
df[["subject_id", "hadm_id", "text_summary"]].to_csv(output_path, index=False)

print(f"Saved {len(df)} patient summaries to {output_path}")
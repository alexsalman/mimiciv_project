#!/usr/bin/env python3
import pandas as pd
from dateutil.relativedelta import relativedelta

# Load merged hospital data (assumes this file already exists)
merged_path = "data/processed/merged_hosp.csv.gz"
df = pd.read_csv(merged_path)

# Drop rows with missing hadm_id or subject_id
df = df.dropna(subset=["subject_id", "hadm_id"])

def build_summary(row):
    # Parse raw datetimes and correct the year by subtracting 150 years
    admit_raw = pd.to_datetime(row["admittime"])
    disch_raw = pd.to_datetime(row["dischtime"])
    admit = admit_raw - relativedelta(years=150)
    disch = disch_raw - relativedelta(years=150)

    parts = [
        f"Patient ID: {int(row['subject_id'])}",
        f"Age: {int(row['anchor_age'])}",
        f"Gender: {row['gender']}",
        f"Admission Type: {row['admission_type']}",
        f"Admission Time: {admit.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Discharge Time: {disch.strftime('%Y-%m-%d %H:%M:%S')}",
    ]

    # Vitals on admission, if available
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

# Build the text_summary column
df["text_summary"] = df.apply(build_summary, axis=1)

# Save to CSV for later embedding
output_path = "data/processed/text_summaries.csv.gz"
df[["subject_id", "hadm_id", "text_summary"]].to_csv(output_path, index=False)

print(f"Saved {len(df)} patient summaries to {output_path}")
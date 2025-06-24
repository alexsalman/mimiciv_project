#!/usr/bin/env python
import json
import re
import pandas as pd
import sys

def main(queries_path, summaries_path, output_path):
    # 1) Load the queries
    with open(queries_path, 'r') as f:
        queries = json.load(f)

    # 2) Load the summaries DataFrame
    df = pd.read_csv(summaries_path)
    df.reset_index(drop=True, inplace=True)

    gold_list = []
    for q in queries:
        query = q["query"]
        k = q["k"]
        entry = {"query": query, "k": k, "gold": []}

        q_lower = query.lower()
        # disease-keyword probe
        m = re.match(r"does patient id:\s*(\d+)\s+exhibit signs of\s+(\w+)\?", q_lower)
        if m:
            disease = m.group(2)
            mask = df["text_summary"].str.contains(disease, case=False, na=False)
            matches = df[mask].head(k)
        else:
            # patient-id exact
            m2 = re.search(r"patient\s*id[:\s]+(\d+)", q_lower)
            if m2:
                pid = int(m2.group(1))
                matches = df[df["subject_id"] == pid].head(k)
            else:
                # can’t auto-generate gold for more complex queries
                matches = pd.DataFrame()

        # collect
        for _, row in matches.iterrows():
            entry["gold"].append({
                "subject_id": int(row["subject_id"]),
                "hadm_id":    int(row["hadm_id"]),
                "summary":    row["text_summary"]
            })

        gold_list.append(entry)

    # 3) Write out
    with open(output_path, 'w') as f:
        json.dump(gold_list, f, indent=2)

    print(f"Wrote {len(gold_list)} gold entries to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: generate_gold.py <queries.json> <text_summaries.csv.gz> <output_gold.json>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
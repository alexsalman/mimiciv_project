#!/usr/bin/env python3
import pandas as pd
from mimiciv_project.agents.retrieval_agent import RetrievalAgent
from tqdm import tqdm

def evaluate_retrieval(test_csv: str = "data/processed/retrieval_test.csv", top_ks=(1,3,5)):
    df = pd.read_csv(test_csv)
    agent = RetrievalAgent()

    # Counters for each k
    hits = {k: 0 for k in top_ks}

    for _, row in tqdm(df.iterrows(), total=len(df)):
        query     = row["query"]
        true_id   = int(row["subject_id"])
        # retrieve top max(top_ks)
        k_max = max(top_ks)
        records = agent.retrieve(query, k=k_max)
        returned_ids = [r["subject_id"] for r in records]

        for k in top_ks:
            if true_id in returned_ids[:k]:
                hits[k] += 1

    # report
    for k in top_ks:
        acc = hits[k] / len(df)
        print(f"Top-{k} retrieval accuracy: {acc:.2%} ({hits[k]}/{len(df)})")

if __name__ == "__main__":
    evaluate_retrieval()
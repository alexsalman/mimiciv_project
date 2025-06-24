#!/usr/bin/env python
import json
import logging
import sys

from mimiciv_project.agents.retrieval_agent import RetrievalAgent

logging.basicConfig(level=logging.DEBUG)

def main(queries_path, output_path):
    # 1) Load the CLI eval queries
    with open(queries_path, 'r') as f:
        queries = json.load(f)

    # 2) Initialize our agent
    agent = RetrievalAgent(
        index_path="data/processed/patient_index.faiss",
        summary_path="data/processed/text_summaries.csv.gz"
    )

    # 3) Run each and collect into a list
    all_results = []
    for q in queries:
        query, k = q["query"], q["k"]
        logging.info(f"Running query={query!r} k={k}")
        recs = agent.retrieve(query, k=k)
        all_results.append({
            "query": query,
            "k": k,
            "predictions": recs
        })

    # 4) Dump to JSON
    with open(output_path, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"Wrote {len(all_results)} entries to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python -m src.mimiciv_project.test_queries <queries.json> <preds_output.json>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
# scripts/evaluate_cli_queries.py

import json
import sys
from pathlib import Path

# Ensure the project 'src' directory is on the Python path
sys.path.insert(0, str(Path.cwd() / "src"))

from mimiciv_project.agents.master_agent import MasterAgent

def main():
    base_dir = Path.cwd()
    queries_path = base_dir / "results" / "cli_eval_queries.json"
    output_path = base_dir / "results" / "cli_eval_results.json"
    
    # Load the prepared CLI queries
    with open(queries_path, "r") as f:
        queries = json.load(f)
    
    # Initialize the MasterAgent
    agent = MasterAgent()
    
    all_results = []
    for entry in queries:
        query = entry["query"]
        k = entry.get("k", 3)
        print(f"Running query (k={k}): {query}")
        # Execute the pipeline
        result = agent.handle_query(query, top_k=k)
        # Collect
        all_results.append({
            "query": query,
            "k": k,
            "summary": result["summary"],
            "diagnoses": result["diagnoses"],
            "feedback_score": result["feedback_score"]
        })
    
    # Write out the results
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nAll results saved to {output_path}")

if __name__ == "__main__":
    main()
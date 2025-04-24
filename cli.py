#!/usr/bin/env python3
import argparse
from agents.master_agent import MasterAgent

def main():
    parser = argparse.ArgumentParser(description="Offline Clinical Q&A")
    parser.add_argument("query", help="Patient-level clinical query")
    parser.add_argument("-k", type=int, default=3, help="Number of similar cases to retrieve")
    args = parser.parse_args()

    agent = MasterAgent()
    result = agent.handle_query(args.query, top_k=args.k)

    print("\n=== Final Response ===")
    print("Summary:\n", result["summary"])
    print("\nDiagnoses:\n", result["diagnoses"])
    print("\nFeedback Score:", result["feedback_score"])

if __name__ == "__main__":
    main()

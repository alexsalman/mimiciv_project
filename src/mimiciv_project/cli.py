#!/usr/bin/env python3
import argparse
from agents.master_agent import MasterAgent

def main():
    p = argparse.ArgumentParser()
    p.add_argument("query", help="Natural-language query or ‘Patient ID: 12345’")
    p.add_argument("-k","--k", type=int, default=3, help="How many records to fetch")
    args = p.parse_args()

    agent = MasterAgent()
    resp  = agent.handle_query(args.query, top_k=args.k)

    print("\n=== Final Response ===")
    print("Summary:\n", resp["summary"], "\n")
    print("Diagnoses:\n", resp["diagnoses"], "\n")
    print("Feedback Score:", resp["feedback_score"])

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
from mimiciv_project.agents.master_agent import MasterAgent

def main():
    p = argparse.ArgumentParser()
    p.add_argument("query", help="Natural-language query or ‘Patient ID: 12345’")
    p.add_argument("-k","--k", type=int, default=3, help="How many records to fetch")
    args = p.parse_args()

    agent = MasterAgent()
    resp  = agent.handle_query(args.query, top_k=args.k)

    # 1) Print the structured timestamps if available
    if "timestamps" in resp:
        print("\n📅 Record Timestamps:")
        for i, ts in enumerate(resp["timestamps"], start=1):
            admit = ts.get("admit_ts") or "N/A"
            disch = ts.get("discharge_ts") or "N/A"
            print(f"  {i}. Admit: {admit}   Discharge: {disch}")

    # 2) Print summary & diagnoses
    print("\n=== Final Response ===")
    print("Summary:")
    print(resp["summary"], "\n")
    print("Diagnoses:")
    print(resp["diagnoses"], "\n")

    # 3) Print feedback score
    print("Feedback Score:", resp["feedback_score"])

if __name__ == "__main__":
    main()
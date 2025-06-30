#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone
import json

from mimiciv_project.agents.master_agent import MasterAgent

def handle_single_query(agent, query: str, k: int):
    resp = agent.handle_query(query, top_k=k)
    resp["timestamp"] = datetime.now(timezone.utc).isoformat()

    if "timestamps" in resp:
        print("\n📅 Record Timestamps:")
        for i, ts in enumerate(resp["timestamps"], start=1):
            admit = ts.get("admit_ts") or "N/A"
            disch = ts.get("discharge_ts") or "N/A"
            print(f"  {i}. Admit: {admit}   Discharge: {disch}")

    print("\n=== Final Response ===")
    print("Summary:")
    print(resp["summary"], "\n")
    print("Diagnoses:")
    print(resp.get("diagnoses") or "—", "\n")
    # raw_records now exists
    print("Clinician Note:")
    note = resp.get("raw_records", [{}])[0].get("summary", "—")
    print(note, "\n")

    print("Feedback Score:", resp.get("feedback_score") or "—")

def handle_eval_mode(agent, queries_path: str, output_path: str):
    with open(queries_path, "r") as f:
        queries = json.load(f)

    feedback_log = []
    for q in queries:
        ts = datetime.now(timezone.utc).isoformat()
        entry = {
            "timestamp":     ts,
            "query":         q["query"],
            "k":             q.get("k", 3),
        }

        result = agent.handle_query(q["query"], top_k=entry["k"])

        # pull the first retrieved record’s summary as "clinician_note"
        raw = result.get("raw_records", [])
        clinician_note = raw[0].get("summary") if raw else None

        entry.update({
            "summary":        result.get("summary"),
            "diagnoses":      result.get("diagnoses"),
            "feedback_score": result.get("feedback_score"),
            "clinician_note": clinician_note
        })
        feedback_log.append(entry)

    with open(output_path, "w") as out:
        json.dump(feedback_log, out, indent=2)
    print(f"Wrote {len(feedback_log)} entries to {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Interact with or evaluate the offline clinical Q&A system"
    )
    subparsers = parser.add_subparsers(dest="mode", required=True)

    single = subparsers.add_parser("run", help="Run one query at a time")
    single.add_argument("query", help="Natural-language query or ‘Patient ID: 12345’")
    single.add_argument("-k", "--k", type=int, default=3, help="How many records to fetch")

    evalp = subparsers.add_parser("eval", help="Batch-evaluate a set of queries")
    evalp.add_argument("--queries", required=True,
                       help="Path to JSON file listing queries (with 'query' and 'k')")
    evalp.add_argument("--output", required=True,
                       help="Path where to write feedback_log.json")

    args = parser.parse_args()
    agent = MasterAgent()

    if args.mode == "run":
        handle_single_query(agent, args.query, args.k)
    else:
        handle_eval_mode(agent, args.queries, args.output)

if __name__ == "__main__":
    main()
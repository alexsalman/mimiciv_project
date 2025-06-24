#!/usr/bin/env python
import json
import argparse

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def match_record(pred, gold):
    """
    Return True if pred and gold refer to the same record
    (match on subject_id and hadm_id).
    """
    return (
        pred.get("subject_id") == gold.get("subject_id")
        and pred.get("hadm_id") == gold.get("hadm_id")
    )

def evaluate(preds, golds, k):
    # Build a lookup for gold by query
    gold_map = {item["query"]: item for item in golds}

    total_queries = len(preds)
    sum_recall = 0.0
    sum_precision = 0.0

    for p in preds:
        q = p["query"]
        # <-- changed here to pull your model’s outputs:
        pred_list = p.get("predictions", [])[:k]
        gold_list = gold_map[q].get("gold", [])

        # count how many gold items are retrieved
        correct = 0
        for pr in pred_list:
            if any(match_record(pr, g) for g in gold_list):
                correct += 1

        recall = correct / len(gold_list) if gold_list else 0.0
        precision = correct / k

        sum_recall += recall
        sum_precision += precision

    return {
        "queries_evaluated": total_queries,
        f"recall@{k}": sum_recall / total_queries,
        f"precision@{k}": sum_precision / total_queries,
    }

def main():
    parser = argparse.ArgumentParser(
        description="Evaluate retrieval predictions against gold labels"
    )
    parser.add_argument("--pred", required=True,
                        help="path to your prediction JSON (with 'predictions' key)")
    parser.add_argument("--gold", required=True,
                        help="path to gold JSON (with 'gold' key)")
    parser.add_argument("--k", type=int, default=3,
                        help="number of top predictions to evaluate (default 3)")
    args = parser.parse_args()

    preds = load_json(args.pred)
    golds = load_json(args.gold)
    metrics = evaluate(preds, golds, args.k)

    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    main()
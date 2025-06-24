import pandas as pd

def sample_retrieval_test(
    summary_path: str = "data/processed/text_summaries.csv.gz",
    output_path:  str = "data/processed/retrieval_test.csv",
    num_samples:  int = 100,
    random_seed:  int = 42
):
    """
    Samples `num_samples` rows from the summary CSV and constructs retrieval test queries.
    Each query is the first sentence of the `text_summary`.
    Outputs a CSV with columns: query, subject_id, hadm_id
    """
    df = pd.read_csv(summary_path)
    df = df.dropna(subset=["text_summary", "subject_id", "hadm_id"])
    sampled = df.sample(n=num_samples, random_state=random_seed)

    # Use the first sentence of the summary as the query
    def first_sentence(text):
        return text.split(".")[0] + "."

    test_df = pd.DataFrame({
        "query": sampled["text_summary"].apply(first_sentence),
        "subject_id": sampled["subject_id"].astype(int),
        "hadm_id": sampled["hadm_id"].astype(int)
    })

    test_df.to_csv(output_path, index=False)
    print(f"Generated {len(test_df)} retrieval test queries → {output_path}")

if __name__ == "__main__":
    sample_retrieval_test()
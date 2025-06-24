#!/usr/bin/env python3
import pandas as pd
from mimiciv_project.agents.summarization_agent import SummarizationAgent
from rouge_score import rouge_scorer
from bert_score import score as bert_score
from tqdm import tqdm

def evaluate_summarization(test_csv: str = "data/processed/summarization_test.csv",
                           model: str = "mistral",
                           base_url: str = "http://127.0.0.1:11434/v1"):
    # 1) Load test data
    df = pd.read_csv(test_csv)
    agent = SummarizationAgent(model=model, base_url=base_url)

    # 2) Prepare scorers
    rouge = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    refs = df['reference_summary'].tolist()
    hyps = []

    # 3) Summarize and score ROUGE
    rouge_l_f1 = []
    for _, row in tqdm(df.iterrows(), total=len(df)):
        text = row['query']
        hyp  = agent.summarize(text)
        hyps.append(hyp)

        scores = rouge.score(row['reference_summary'], hyp)
        rouge_l_f1.append(scores['rougeL'].fmeasure)

    # 4) Compute BERTScore
    P, R, F = bert_score(hyps, refs, lang='en', rescale_with_baseline=True)
    bert_f1 = F.mean().item()

    # 5) Report
    print(f"Avg ROUGE-L F1: {sum(rouge_l_f1)/len(rouge_l_f1):.4f}")
    print(f"Avg BERTScore F1: {bert_f1:.4f}")

if __name__ == "__main__":
    evaluate_summarization()
# src/mimiciv_project/agents/diagnosis_agent.py

import requests

class DiagnosisAgent:
    def __init__(
        self,
        model: str = "gemma:latest",
        base_url: str = "http://127.0.0.1:11434/v1"
    ):
        self.model    = model
        self.endpoint = f"{base_url}/chat/completions"

    def diagnose(self, summary: str) -> str:
        prompt = (
            "🩺 Based on the patient summary below, list the top 3 most likely diagnoses as markdown bullets. "
            "For each, include the condition name and ICD code, followed by a one-sentence rationale:\n\n"
            f"{summary}"
        )
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }
        resp = requests.post(self.endpoint, json=payload, timeout=60)
        resp.raise_for_status()                              # <-- will raise if Ollama isn’t reachable
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
# agents/diagnosis_agent.py

import requests

class DiagnosisAgent:
    def __init__(self,
                 model: str = "gemma",
                 base_url: str = "http://127.0.0.1:11434/v1"):
        self.model    = model
        self.endpoint = f"{base_url}/chat/completions"

    def diagnose(self, summary: str) -> str:
        prompt = (
            "🩺 Given this patient summary, list the most likely diagnoses "
            "with brief explanations for each:\n\n"
            f"{summary}"
        )
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }
        resp = requests.post(self.endpoint, json=payload)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()

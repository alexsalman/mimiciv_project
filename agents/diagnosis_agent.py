# agents/diagnosis_agent.py

import subprocess

class DiagnosisAgent:
    def __init__(self, model="gemma"):
        self.model = model

    def diagnose(self, summary: str) -> str:
        prompt = (
            "🩺 Given the following patient summary, list the most likely diagnoses. "
            "Provide a short explanation for each:\n\n"
            f"{summary}\n\n"
            "Respond in markdown bullet format."
        )
        result = subprocess.run(
            ["ollama", "run", self.model, prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

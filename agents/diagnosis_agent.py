# agents/diagnosis_agent.py

import subprocess

class DiagnosisAgent:
    def __init__(self, model="gemma"):
        self.model = model

    def diagnose(self, summary: str):
        prompt = (
            "Given the following patient summary, what are the most likely conditions? "
            "List possible diagnoses:\n\n"
            f"{summary}"
        )
        result = subprocess.run(
            ["ollama", "run", self.model, prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

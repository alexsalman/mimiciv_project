# agents/summarization_agent.py

import subprocess

class SummarizationAgent:
    def __init__(self, model="mistral"):
        self.model = model

    def summarize(self, text: str):
        prompt = f"Summarize the patient's condition:\n{text}"
        result = subprocess.run(
            ["ollama", "run", self.model, prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

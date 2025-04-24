# agents/summarization_agent.py

import requests

class SummarizationAgent:
    def __init__(self,
                 model: str = "mistral",
                 base_url: str = "http://127.0.0.1:11434/v1"):
        self.model    = model
        self.endpoint = f"{base_url}/chat/completions"

    def summarize(self, text: str) -> str:
        prompt = (
            "📝 Summarize the following ICU patient record into a concise, "
            "clinically relevant summary:\n\n"
            f"{text}"
        )
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }
        resp = requests.post(self.endpoint, json=payload)
        resp.raise_for_status()
        data = resp.json()
        # assume OpenAI‐style response
        return data["choices"][0]["message"]["content"].strip()

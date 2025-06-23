# agents/summarization_agent.py

import requests
import os

class SummarizationAgent:
    def __init__(
        self,
        model: str = "mistral",
        base_url: str = "http://127.0.0.1:11434/v1"
    ):
        """
        SummarizationAgent wraps a local LLM (via Ollama's HTTP API).
        """
        self.model = model
        self.endpoint = f"{base_url}/chat/completions"

    def summarize(self, text: str) -> str:
        """
        Summarize an ICU patient record into a concise narrative.
        """
        prompt = (
            "📝 Summarize the following ICU patient record into a concise, "
            "clinically relevant summary:\n\n"
            f"{text}"
        )
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful medical summarization assistant."},
                {"role": "user",   "content": prompt}
            ]
        }
        resp = requests.post(self.endpoint, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        # Extract the assistant’s reply
        return data["choices"][0]["message"]["content"].strip()
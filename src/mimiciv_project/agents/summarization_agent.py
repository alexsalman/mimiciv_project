# src/mimiciv_project/agents/summarization_agent.py

import unicodedata
import re
import requests

class SummarizationAgent:
    def __init__(self,
                 model: str = "mistral",
                 base_url: str = "http://127.0.0.1:11434/v1"):
        self.model    = model
        self.endpoint = f"{base_url}/chat/completions"

    def _normalize_query(self, text: str) -> str:
        """
        Normalize query text by stripping diacritics, mapping to ASCII,
        lowercasing, and removing punctuation (to preserve abbreviations).
        """
        nfkd = unicodedata.normalize('NFKD', text)
        ascii_str = nfkd.encode('ASCII', 'ignore').decode('ASCII')
        return re.sub(r"[^\w\s]", "", ascii_str.lower())

    def summarize(self, text: str, query: str = None) -> str:
        """
        Summarize the patient record. Use the vitals branch if the query
        explicitly asks for numeric vitals terms (spo2, hr, bp, rr, temp).
        """
        vitals_branch = False
        if query:
            norm_q = self._normalize_query(query)
            # Trigger only on exact vitals keywords
            if re.search(r"\b(?:spo2|hr|bp|rr|temp)\b", norm_q):
                vitals_branch = True

        if vitals_branch:
            prompt = (
                "📝 From the following ICU patient record, extract and report "
                "the patient's heart rate, blood pressure, respiratory rate, "
                "temperature, and SpO2 on admission:\n\n" + text
            )
            print("DEBUG: Summarize called (vitals_branch=True)")
        else:
            prompt = (
                "📝 Summarize the following ICU patient record into a concise, "
                "clinically relevant summary:\n\n" + text
            )
            print(f"DEBUG: Summarize called (vitals_branch={vitals_branch})")

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }
        resp = requests.post(self.endpoint, json=payload)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
# tests/conftest.py
import pytest

@pytest.fixture(autouse=True)
def stub_out_llm_calls(monkeypatch):
    """
    Automatically stub SummarizationAgent.summarize() and DiagnosisAgent.diagnose()
    so they return canned output instead of doing HTTP requests.
    """
    from mimiciv_project.agents.summarization_agent import SummarizationAgent
    from mimiciv_project.agents.diagnosis_agent     import DiagnosisAgent

    def fake_summarize(self, text: str) -> str:
        return "📝 [stub summary]"

    def fake_diagnose(self, summary: str) -> str:
        return "- **StubDx**: Explanation."

    monkeypatch.setattr(SummarizationAgent, "summarize", fake_summarize)
    monkeypatch.setattr(DiagnosisAgent,     "diagnose",  fake_diagnose)
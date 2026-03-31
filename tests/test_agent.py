from quantumthink.agent.core import QuantumThinkAgent
from quantumthink.config import AgentConfig


def test_agent_uses_tool(tmp_path) -> None:
    cfg = AgentConfig(memory_path=str(tmp_path / "memory.jsonl"), provider="mock")
    agent = QuantumThinkAgent.from_config(cfg)

    response = agent.respond("посчитай 6*7", session_id="t1")
    assert response.startswith("[calculator]")


def test_agent_uses_mock_llm(tmp_path) -> None:
    cfg = AgentConfig(memory_path=str(tmp_path / "memory.jsonl"), provider="mock")
    agent = QuantumThinkAgent.from_config(cfg)

    response = agent.respond("привет", session_id="t2")
    assert response.startswith("[MOCK]")

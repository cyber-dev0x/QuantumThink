from __future__ import annotations

from typing import Sequence

from quantumthink.types import Message


class MockLLMClient:
    """Fallback provider: no API calls, predictable output for local runs/tests."""

    def generate(
        self,
        messages: Sequence[Message],
        system_prompt: str,
        temperature: float = 0.2,
    ) -> str:
        _ = system_prompt, temperature
        last_user = next((m.content for m in reversed(messages) if m.role == "user"), "")
        return f"[MOCK] Понял запрос: {last_user}"

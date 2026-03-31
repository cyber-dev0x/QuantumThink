from __future__ import annotations

from typing import Protocol, Sequence

from quantumthink.types import Message


class LLMClient(Protocol):
    def generate(
        self,
        messages: Sequence[Message],
        system_prompt: str,
        temperature: float = 0.2,
    ) -> str:
        ...

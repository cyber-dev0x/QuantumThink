from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(slots=True)
class AgentConfig:
    provider: str = "mock"
    model: str = "gpt-4.1-mini"
    temperature: float = 0.2
    memory_path: str = ".data/memory.jsonl"
    system_prompt: str = "Ты QuantumThink — прагматичный AI-агент."

    @classmethod
    def from_yaml(cls, path: str | Path) -> "AgentConfig":
        cfg_path = Path(path)
        if not cfg_path.exists():
            return cls()

        raw = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
        return cls(
            provider=raw.get("provider", "mock"),
            model=raw.get("model", "gpt-4.1-mini"),
            temperature=float(raw.get("temperature", 0.2)),
            memory_path=raw.get("memory_path", ".data/memory.jsonl"),
            system_prompt=raw.get("system_prompt", "Ты QuantumThink — прагматичный AI-агент."),
        )

    @property
    def openai_api_key(self) -> str | None:
        return os.getenv("OPENAI_API_KEY")

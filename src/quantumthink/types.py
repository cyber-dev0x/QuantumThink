from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(slots=True)
class Message:
    role: str
    content: str
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict[str, str]:
        return {
            "role": self.role,
            "content": self.content,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, str]) -> "Message":
        return cls(
            role=payload.get("role", "user"),
            content=payload.get("content", ""),
            timestamp=payload.get("timestamp", datetime.now(timezone.utc).isoformat()),
        )

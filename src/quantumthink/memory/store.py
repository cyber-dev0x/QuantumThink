from __future__ import annotations

import json
from pathlib import Path

from quantumthink.types import Message


class JsonlMemoryStore:
    def __init__(self, path: str) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch(exist_ok=True)

    def append(self, session_id: str, message: Message) -> None:
        payload = {
            "session_id": session_id,
            **message.to_dict(),
        }
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")

    def history(self, session_id: str, limit: int = 20) -> list[Message]:
        messages: list[Message] = []
        if not self.path.exists():
            return messages

        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                payload = json.loads(line)
                if payload.get("session_id") != session_id:
                    continue
                messages.append(
                    Message.from_dict(
                        {
                            "role": payload.get("role", "user"),
                            "content": payload.get("content", ""),
                            "timestamp": payload.get("timestamp", ""),
                        }
                    )
                )
        return messages[-limit:]

from __future__ import annotations

from typing import Sequence

from quantumthink.types import Message


class OpenAIChatClient:
    def __init__(self, model: str, api_key: str | None = None) -> None:
        try:
            from openai import OpenAI
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("Package 'openai' is not installed") from exc

        self.model = model
        self.client = OpenAI(api_key=api_key)

    def generate(
        self,
        messages: Sequence[Message],
        system_prompt: str,
        temperature: float = 0.2,
    ) -> str:
        payload = [{"role": "system", "content": system_prompt}]
        payload.extend({"role": m.role, "content": m.content} for m in messages)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=payload,
            temperature=temperature,
        )
        text = response.choices[0].message.content
        return text.strip() if text else ""

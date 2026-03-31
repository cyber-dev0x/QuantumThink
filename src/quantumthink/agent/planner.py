from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(slots=True)
class PlannerDecision:
    tool_name: str
    tool_input: str


class SimplePlanner:
    _time_keywords = {
        "time",
        "date",
        "сейчас",
        "время",
        "дата",
        "который час",
        "today",
        "now",
    }

    _math_keywords = {
        "посчитай",
        "calculate",
        "сколько будет",
        "реши",
    }

    _math_pattern = re.compile(r"\d\s*[\+\-\*\/]\s*\d")

    def plan(self, user_input: str) -> PlannerDecision | None:
        text = user_input.lower()

        if any(token in text for token in self._time_keywords):
            return PlannerDecision(tool_name="datetime", tool_input=user_input)

        if any(token in text for token in self._math_keywords) or self._math_pattern.search(text):
            return PlannerDecision(tool_name="calculator", tool_input=user_input)

        return None

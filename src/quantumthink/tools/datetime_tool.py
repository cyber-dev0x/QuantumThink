from __future__ import annotations

from datetime import datetime


class DateTimeTool:
    name = "datetime"
    description = "Returns current date and time"

    def run(self, raw_input: str) -> str:
        _ = raw_input
        now_local = datetime.now().astimezone()
        return now_local.strftime("%Y-%m-%d %H:%M:%S %Z")

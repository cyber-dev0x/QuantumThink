from __future__ import annotations

from pathlib import Path

from quantumthink.agent.planner import SimplePlanner
from quantumthink.config import AgentConfig
from quantumthink.llm.base import LLMClient
from quantumthink.llm.mock import MockLLMClient
from quantumthink.llm.openai_client import OpenAIChatClient
from quantumthink.memory.store import JsonlMemoryStore
from quantumthink.tools.calculator import CalculatorTool
from quantumthink.tools.datetime_tool import DateTimeTool
from quantumthink.tools.registry import ToolRegistry
from quantumthink.types import Message


class QuantumThinkAgent:
    def __init__(
        self,
        config: AgentConfig,
        llm: LLMClient,
        memory: JsonlMemoryStore,
        planner: SimplePlanner,
        tools: ToolRegistry,
    ) -> None:
        self.config = config
        self.llm = llm
        self.memory = memory
        self.planner = planner
        self.tools = tools

    @classmethod
    def from_config(cls, config: AgentConfig) -> "QuantumThinkAgent":
        memory = JsonlMemoryStore(config.memory_path)
        planner = SimplePlanner()

        tools = ToolRegistry()
        tools.register(CalculatorTool())
        tools.register(DateTimeTool())

        llm: LLMClient
        if config.provider == "openai":
            llm = OpenAIChatClient(model=config.model, api_key=config.openai_api_key)
        else:
            llm = MockLLMClient()

        return cls(config=config, llm=llm, memory=memory, planner=planner, tools=tools)

    def respond(self, user_input: str, session_id: str = "default") -> str:
        user_message = Message(role="user", content=user_input)
        self.memory.append(session_id, user_message)

        decision = self.planner.plan(user_input)
        if decision:
            tool = self.tools.get(decision.tool_name)
            if tool is None:
                assistant_text = f"Инструмент '{decision.tool_name}' не найден"
            else:
                try:
                    result = tool.run(decision.tool_input)
                    assistant_text = f"[{decision.tool_name}] {result}"
                except Exception as exc:  # noqa: BLE001
                    assistant_text = f"Ошибка инструмента: {exc}"
        else:
            history = self.memory.history(session_id=session_id, limit=20)
            assistant_text = self.llm.generate(
                messages=history,
                system_prompt=self.config.system_prompt,
                temperature=self.config.temperature,
            )

        assistant_message = Message(role="assistant", content=assistant_text)
        self.memory.append(session_id, assistant_message)
        return assistant_text

    def ensure_runtime_dirs(self) -> None:
        Path(self.config.memory_path).parent.mkdir(parents=True, exist_ok=True)

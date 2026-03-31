from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from quantumthink.agent.core import QuantumThinkAgent
from quantumthink.config import AgentConfig

DEFAULT_CONFIG_PATH = Path("configs/agent.yaml")

app = typer.Typer(add_completion=False, help="QuantumThink AI Agent CLI")


def build_agent(config_path: Path) -> QuantumThinkAgent:
    config = AgentConfig.from_yaml(config_path)
    return QuantumThinkAgent.from_config(config)


@app.command()
def ask(
    prompt: Annotated[str, typer.Argument(help="Single prompt")],
    config: Annotated[Path, typer.Option("--config", "-c")] = DEFAULT_CONFIG_PATH,
    session: Annotated[str, typer.Option("--session", "-s")] = "default",
) -> None:
    """Run one request and exit."""
    agent = build_agent(config)
    response = agent.respond(prompt, session_id=session)
    typer.echo(response)


@app.command()
def chat(
    config: Annotated[Path, typer.Option("--config", "-c")] = DEFAULT_CONFIG_PATH,
    session: Annotated[str, typer.Option("--session", "-s")] = "default",
) -> None:
    """Interactive chat mode."""
    agent = build_agent(config)
    typer.echo("QuantumThink chat (exit/quit для выхода)")
    while True:
        try:
            user_input = typer.prompt("you")
        except (EOFError, KeyboardInterrupt):
            typer.echo("\nПока 👋")
            break

        if user_input.strip().lower() in {"exit", "quit", "q"}:
            typer.echo("Пока 👋")
            break

        answer = agent.respond(user_input, session_id=session)
        typer.echo(f"agent: {answer}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()

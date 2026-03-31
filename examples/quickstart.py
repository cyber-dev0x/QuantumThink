from quantumthink.agent.core import QuantumThinkAgent
from quantumthink.config import AgentConfig


def main() -> None:
    config = AgentConfig.from_yaml("configs/agent.yaml")
    agent = QuantumThinkAgent.from_config(config)

    print(agent.respond("посчитай 12 * (7 - 2)"))
    print(agent.respond("какая сейчас дата?"))
    print(agent.respond("придумай 3 идеи для SaaS"))


if __name__ == "__main__":
    main()

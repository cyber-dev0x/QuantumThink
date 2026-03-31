from quantumthink.agent.planner import SimplePlanner


def test_planner_datetime() -> None:
    planner = SimplePlanner()
    decision = planner.plan("какая сейчас дата?")
    assert decision is not None
    assert decision.tool_name == "datetime"


def test_planner_calculator() -> None:
    planner = SimplePlanner()
    decision = planner.plan("посчитай 10 / 2")
    assert decision is not None
    assert decision.tool_name == "calculator"

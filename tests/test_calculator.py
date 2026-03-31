from quantumthink.tools.calculator import CalculatorTool


def test_calculator_simple_expression() -> None:
    tool = CalculatorTool()
    result = tool.run("2 + 2 * 5")
    assert result.endswith("= 12")


def test_calculator_pow() -> None:
    tool = CalculatorTool()
    result = tool.run("2 ^ 3")
    assert result.endswith("= 8")

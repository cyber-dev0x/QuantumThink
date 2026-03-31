from __future__ import annotations

import ast
import re

_ALLOWED_BIN_OPS = {
    ast.Add: lambda a, b: a + b,
    ast.Sub: lambda a, b: a - b,
    ast.Mult: lambda a, b: a * b,
    ast.Div: lambda a, b: a / b,
    ast.FloorDiv: lambda a, b: a // b,
    ast.Mod: lambda a, b: a % b,
    ast.Pow: lambda a, b: a**b,
}
_ALLOWED_UNARY_OPS = {
    ast.UAdd: lambda x: +x,
    ast.USub: lambda x: -x,
}


class CalculatorTool:
    name = "calculator"
    description = "Safe arithmetic evaluator"

    def run(self, raw_input: str) -> str:
        expression = self._extract_expression(raw_input)
        value = self._safe_eval(expression)
        return f"{expression} = {value}"

    def _extract_expression(self, raw_input: str) -> str:
        match = re.search(r"[\d\s\+\-\*\/\(\)\.%\^]+", raw_input)
        if not match:
            raise ValueError("Не вижу математического выражения")

        expression = match.group(0).strip()
        expression = expression.replace("^", "**")
        if not expression:
            raise ValueError("Пустое выражение")
        return expression

    def _safe_eval(self, expression: str) -> float | int:
        node = ast.parse(expression, mode="eval")
        return self._eval_node(node.body)

    def _eval_node(self, node: ast.AST) -> float | int:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_BIN_OPS:
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            return _ALLOWED_BIN_OPS[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_UNARY_OPS:
            value = self._eval_node(node.operand)
            return _ALLOWED_UNARY_OPS[type(node.op)](value)

        raise ValueError("Недопустимое выражение")

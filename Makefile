.PHONY: dev test lint format run

dev:
	pip install -e .[dev]

test:
	pytest -q

lint:
	ruff check .

format:
	ruff format .

run:
	quantumthink chat

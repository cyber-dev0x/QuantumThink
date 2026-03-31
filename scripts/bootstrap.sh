#!/usr/bin/env bash
set -e
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .[dev]
cp -n .env.example .env || true
echo "Готово. Запусти: source .venv/bin/activate && quantumthink chat"

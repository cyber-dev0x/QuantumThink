# QuantumThink

Готовый стартовый репозиторий AI-агента на Python: CLI, память, планировщик, инструменты и интеграция с OpenAI.

## Что внутри

- `src/quantumthink` — ядро агента
- `configs/agent.yaml` — конфиг агента
- `tests/` — unit-тесты
- `docs/` — архитектура и roadmap
- `.github/workflows/ci.yml` — CI (lint + tests)

## Быстрый старт

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .[dev]
cp .env.example .env
```

Запуск REPL:

```bash
quantumthink chat
```

Один запрос:

```bash
quantumthink ask "посчитай 25 * (4 + 1)"
```

## Переключение на OpenAI

1. Установи OpenAI-зависимость:
   ```bash
   pip install -e .[openai]
   ```
   > Для OpenAI SDK лучше Python 3.11–3.14.
2. В `.env` добавь `OPENAI_API_KEY=...`
3. В `configs/agent.yaml` поставь:
   ```yaml
   provider: openai
   model: gpt-4.1-mini
   ```

## Команды

```bash
make dev      # установить dev-зависимости
make test     # запустить тесты
make lint     # линтер
make format   # автоформат
```

## Лицензия

MIT

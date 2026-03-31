# Архитектура QuantumThink

## Компоненты

1. **CLI** (`cli.py`) — интерфейс запуска (`ask` и `chat`).
2. **Agent Core** (`agent/core.py`) — orchestration: память → планировщик → tools/LLM.
3. **Planner** (`agent/planner.py`) — быстрый выбор, нужен ли инструмент.
4. **Tools** (`tools/*`) — локальные инструменты (калькулятор, дата/время).
5. **LLM Clients** (`llm/*`) — `mock` и `openai` провайдеры.
6. **Memory Store** (`memory/store.py`) — JSONL история по `session_id`.

## Поток запроса

`User input -> Planner -> (Tool? yes -> Tool output | no -> LLM) -> Memory -> Response`

## Почему так

- Просто расширять новыми инструментами
- Безопасный дефолт (`mock`) без внешних ключей
- Отдельные слои для тестируемости

# Agente de Memória Institucional

## Visão Geral

O Agente de Memória do Projeto Jason é responsável por preservar conhecimento institucional e fornecer acessos rápidos a fatos já registrados.

Ele é construído com dois componentes principais:

- `MemoryStore`: um repositório thread-safe de entradas de memória com persistência JSON opcional.
- `MemoryAgent`: um agente de alto nível que expõe comandos para lembrar, consultar, buscar, listar e esquecer dados.

## Funcionalidades

- Armazenar pares chave/valor com tags associadas.
- Recuperar uma entrada a partir da chave.
- Buscar entradas por texto nas chaves, valores ou tags.
- Listar chaves disponíveis.
- Esquecer entradas específicas.
- Manter persistência em arquivo JSON para continuidade entre execuções.

## Uso

Exemplo mínimo:

```python
from pathlib import Path
from src.memory_agent import MemoryAgent
from src.memory_store import MemoryStore

store = MemoryStore(storage_path=Path("data/memory.json"))
agent = MemoryAgent(store=store)

agent.run("remember", {"key": "projeto", "value": "Projeto Jason", "tags": ["plano", "memória"]})
entry = agent.run("recall", {"key": "projeto"})
print(entry.value)
```

## Contratos

- `Agent`: contrato base que define `name`, `description` e `run`.
- `MemoryStore`: API de persistência com métodos `remember`, `recall`, `search`, `forget`, `list_keys` e `all_entries`.
- `MemoryAgent`: adaptador de comando que implementa o contrato `Agent` e delega operações para `MemoryStore`.

## Testes

O comportamento do agente e da memória é coberto pelos seguintes testes automáticos:

- `tests/test_memory_store.py`
- `tests/test_memory_agent.py`

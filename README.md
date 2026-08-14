# Projeto Jason

> Plataforma de Inteligência Artificial da Central Newton.

---

# Visão Geral

O Projeto Jason é o núcleo de desenvolvimento da Central Newton.

Seu objetivo é criar uma plataforma de Inteligência Artificial modular, composta por agentes especializados capazes de colaborar entre si, compartilhar memória, executar tarefas complexas e evoluir continuamente.

---

# Objetivos

- Construir uma arquitetura modular baseada em agentes.
- Desenvolver memória compartilhada entre agentes.
- Automatizar processos.
- Integrar APIs e serviços externos.
- Documentar toda a evolução do projeto.
- Utilizar Git para controle de versões.

---

# Estrutura do Projeto


Projeto_Jason/
│
├── docs/
│   └── Documentação
│
├── src/
│   └── Código-fonte (agentes e módulos de memória)
│
├── tests/
│   └── Casos de teste automatizados
│
├── data/
│   └── Banco de dados
│
├── logs/
│   └── Registros do sistema
│
└── README.md


---

# Agente de Memória

O Projeto Jason agora inclui um módulo de memória institucional em `src/`, com:
- `MemoryStore`: armazenamento thread-safe de fatos, consultas e tags.
- `MemoryAgent`: interface para lembrar, consultar, buscar, listar e esquecer registros.

O agente pode ser estendido para integração com outros agentes e com persistência em arquivo JSON.

---

# Tecnologias

- Python
- Git
- Visual Studio Code

---

# Status

*Fase 1*
Estrutura inicial do ambiente de desenvolvimento.

---

# Autor

Newton Uzeda Couto

Projeto desenvolvido para a Central Newton.
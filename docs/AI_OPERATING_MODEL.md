# Modelo Operacional de IA — Projeto Jason

## 1. Objetivo

Este documento define como modelos de inteligência artificial participam do desenvolvimento do Projeto Jason, garantindo consistência, rastreabilidade, governança e qualidade em todas as atividades relacionadas à documentação, arquitetura e implementação.

---

## 2. Princípios

O trabalho com IA no Projeto Jason deve seguir os seguintes princípios:

- Single Source of Truth
- DRY (Don't Repeat Yourself)
- Arquitetura antes da implementação
- Documentação antes do código
- Rastreabilidade
- Segurança
- Governança
- Consistência

---

## 3. Papéis das IAs

### ChatGPT

Responsável por:

- arquitetura
- planejamento
- revisão técnica
- governança
- decisões estruturais
- documentação executiva

Não deve modificar múltiplos arquivos simultaneamente sem aprovação.

### Codex

Responsável por:

- implementação
- refatoração
- geração de documentação
- revisão localizada
- manutenção

Sempre trabalha sobre tarefas previamente aprovadas.

---

## 4. Fluxo Oficial de Trabalho

O fluxo oficial de trabalho deve seguir esta sequência:

1. Análise
2. Diagnóstico
3. Planejamento
4. Aprovação humana
5. Implementação
6. Revisão
7. Consolidação

Nenhuma IA pode pular etapas.

---

## 5. Regras Obrigatórias

As seguintes regras são obrigatórias:

- Nunca inventar arquivos.
- Nunca assumir que um documento existe.
- Sempre verificar o workspace.
- Nunca modificar mais de um documento por vez sem autorização.
- Sempre informar impacto das alterações.
- Sempre preservar conteúdo existente.
- Sempre registrar mudanças relevantes.

---

## 6. Processo de Aprovação

O processo de aprovação segue a seguinte lógica:

Arquitetura → ChatGPT propõe → Humano aprova → Codex implementa.

---

## 7. Comunicação entre IAs

A comunicação entre as inteligências artificiais deve ser clara e disciplinada:

- ChatGPT define estratégia.
- Codex executa.
- Humano aprova.

---

## 8. Qualidade

Toda alteração deve buscar:

- simplicidade
- baixo acoplamento
- alta coesão
- consistência
- navegabilidade
- ausência de duplicação
- documentação atualizada

---

## 9. Evolução

Este documento deve evoluir conforme o Projeto Jason amadurecer, incorporando novos aprendizados, decisões e padrões de governança.

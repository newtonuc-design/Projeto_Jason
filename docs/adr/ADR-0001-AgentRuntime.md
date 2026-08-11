# ADR-0001

## Title

Jason Runtime Pipeline

---

## Status

Accepted

---

## Context

Todo agente do Jason deverá executar tarefas utilizando um pipeline único.

Isso garante previsibilidade, auditoria, testes e evolução da plataforma.

---

## Pipeline

INPUT

?

Context Builder

?

Planner

?

Reasoner

?

Policy Engine

?

Executor

?

Observer

?

Memory

?

Reporter

---

## Responsabilidades

Context Builder
- monta o contexto

Planner
- cria plano

Reasoner
- decide estratégia

Policy Engine
- verifica regras

Executor
- executa

Observer
- coleta resultados

Memory
- registra memória

Reporter
- produz resposta

---

## Consequências

Todos os agentes utilizarão exatamente este pipeline.

Nenhum agente poderá executar ações fora dele.


# Concept Relation Writeback Apply Report

Generated: `2026-05-16T09:20:52Z`

> 写回边界：只写子卡 `up`；不手写 `down` / `children`；不把 `topic_family_review` 写入概念卡；不新增 Juggl 镜像字段。

## Summary

- planned: 13
- ready: 13
- applied: 13
- skipped: 0
- write_policy: small batch only; no topic_family_review and no down/children mirror fields

## Planned rows

| Source | Target | Status | Confidence | Rationale |
|---|---|---|---|---|
| [[Long-term Memory]] | [[Memory]] | ready | high | Long-term memory is the broader cross-session memory capability. |
| [[Microsoft Agent Framework]] | [[Agent Framework]] | ready | high | Microsoft Agent Framework is a named agent SDK/framework route. |
| [[Non-Parametric Memory]] | [[Memory]] | ready | high | Non-parametric memory is external retrievable memory outside model weights. |
| [[RAG Evaluation]] | [[Evaluation]] | ready | high | RAG Evaluation is a subtype of evaluation focused on retrieval/context/citation/answer quality. |
| [[Self-RAG]] | [[RAG]] | ready | high | Self-RAG is a RAG method family with adaptive retrieval/generation/critique. |
| [[Semantic Memory]] | [[Memory]] | ready | high | Semantic memory is a subtype of memory for stable facts/preferences/concepts. |
| [[Tool Calling]] | [[Tool Use]] | ready | high | Tool Calling is a structured form of tool use. |
| [[Trajectory Evaluation]] | [[Evaluation]] | ready | high | Trajectory Evaluation is evaluation of an agent's action process rather than only final output. |
| [[Computer Use]] | [[Tool Use]] | ready | medium | Computer Use is a tool-use mode where the agent operates browser/desktop/terminal surfaces. |
| [[Data-first Agent Framework]] | [[Agent Framework]] | ready | medium | Data-first Agent Framework is explicitly a framework route centered on data/RAG primitives. |
| [[Graph Construction Evaluation]] | [[Evaluation]] | ready | medium | Graph Construction Evaluation is a subtype of evaluation for graph/RAG construction quality. |
| [[Multi-agent Orchestration]] | [[Agent Workflow]] | ready | medium | Multi-agent orchestration is a workflow/coordination pattern for multiple agents. |
| [[Parametric Memory]] | [[Memory]] | ready | medium | Parametric memory is memory encoded inside model parameters. |

## Applied rows

| Source | Target | Result |
|---|---|---|
| [[Long-term Memory]] | [[Memory]] | applied |
| [[Microsoft Agent Framework]] | [[Agent Framework]] | applied |
| [[Non-Parametric Memory]] | [[Memory]] | applied |
| [[RAG Evaluation]] | [[Evaluation]] | applied |
| [[Self-RAG]] | [[RAG]] | applied |
| [[Semantic Memory]] | [[Memory]] | applied |
| [[Tool Calling]] | [[Tool Use]] | applied |
| [[Trajectory Evaluation]] | [[Evaluation]] | applied |
| [[Computer Use]] | [[Tool Use]] | applied |
| [[Data-first Agent Framework]] | [[Agent Framework]] | applied |
| [[Graph Construction Evaluation]] | [[Evaluation]] | applied |
| [[Multi-agent Orchestration]] | [[Agent Workflow]] | applied |
| [[Parametric Memory]] | [[Memory]] | applied |

# Concept Relation Writeback Apply Report

Generated: `2026-05-21T04:48:12Z`

> 写回边界：只写子卡 `up`；不手写 `down` / `children`；不把 `topic_family_review` 写入概念卡；不新增 Juggl 镜像字段。

## Summary

- planned: 2
- ready: 2
- applied: 2
- skipped: 0
- write_policy: small batch only; no topic_family_review and no down/children mirror fields

## Planned rows

| Source | Target | Status | Confidence | Rationale |
|---|---|---|---|---|
| [[Agent Evaluation Benchmark]] | [[Benchmark]] | ready | high | Agent Evaluation Benchmark is a benchmark subtype focused on agent/assistant action tasks, environments, tools, and scoring protocols. |
| [[BFCL]] | [[Agent Evaluation Benchmark]] | ready | high | BFCL is a function/tool-calling benchmark and a representative member of the Agent Evaluation Benchmark family. |

## Applied rows

| Source | Target | Result |
|---|---|---|
| [[Agent Evaluation Benchmark]] | [[Benchmark]] | applied |
| [[BFCL]] | [[Agent Evaluation Benchmark]] | applied |

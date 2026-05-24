# Concept Relation Writeback Apply Report

Generated: `2026-05-24T09:21:09Z`

> 写回边界：只写子卡 `up`；不手写 `down` / `children`；不把 `topic_family_review` 写入概念卡；不新增 Juggl 镜像字段。

## Summary

- planned: 6
- ready: 6
- applied: 6
- skipped: 0
- write_policy: small batch only; no topic_family_review and no down/children mirror fields

## Planned rows

| Source | Target | Status | Confidence | Rationale |
|---|---|---|---|---|
| [[Approximate Nearest Neighbor Search]] | [[Vector Search Algorithm]] | ready | high | Approximate Nearest Neighbor Search is a vector-search algorithm family that uses approximate indexing to speed up nearest-neighbor lookup. |
| [[Embedding Evaluation Benchmark]] | [[Benchmark]] | ready | high | Embedding Evaluation Benchmark is a benchmark subtype focused on text embedding model evaluation tasks and reporting protocols. |
| [[Embedding Quantization]] | [[Embedding Optimization]] | ready | high | Embedding Quantization is an embedding optimization route for reducing vector precision, storage, and retrieval cost. |
| [[HNSW]] | [[Approximate Nearest Neighbor Search]] | ready | high | HNSW is a concrete graph-index algorithm in the Approximate Nearest Neighbor Search family. |
| [[MTEB]] | [[Embedding Evaluation Benchmark]] | ready | high | MTEB is a concrete text embedding benchmark/leaderboard in the Embedding Evaluation Benchmark family. |
| [[Matryoshka Embeddings]] | [[Embedding Optimization]] | ready | high | Matryoshka Embeddings are an embedding optimization route for reducing effective vector dimensionality under controlled quality tradeoffs. |

## Applied rows

| Source | Target | Result |
|---|---|---|
| [[Approximate Nearest Neighbor Search]] | [[Vector Search Algorithm]] | applied |
| [[Embedding Evaluation Benchmark]] | [[Benchmark]] | applied |
| [[Embedding Quantization]] | [[Embedding Optimization]] | applied |
| [[HNSW]] | [[Approximate Nearest Neighbor Search]] | applied |
| [[MTEB]] | [[Embedding Evaluation Benchmark]] | applied |
| [[Matryoshka Embeddings]] | [[Embedding Optimization]] | applied |

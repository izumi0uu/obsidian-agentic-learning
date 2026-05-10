---
type: source
source_type: docs
title: "Agent Engineering Infrastructure Primary Sources"
url:
author: multiple
site: multiple
topic:
  - agent
  - frontier
  - infrastructure
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-10
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Agent 工程基础设施主源]]"
  - "[[Vector Database]]"
  - "[[Document Ingestion]]"
  - "[[LLM Gateway]]"
  - "[[Code Execution Sandbox]]"
  - "[[OpenTelemetry GenAI]]"
  - "[[Agent Lifecycle Hook]]"
---

# Agent 工程基础设施主源

## 为什么收

之前前沿收集偏论文方法和显性 Agent 概念，容易漏掉像 [[Neo4j]] 这种“不一定是方法名，但工程上非常关键”的基础设施。这里集中记录这类主源，作为 [[Agent 工程基础设施主源]] 的证据层。

## RAG / 检索基础设施

- Pinecone docs: <https://docs.pinecone.io/>
- Weaviate search docs: <https://docs.weaviate.io/weaviate/concepts/search>
- Qdrant docs: <https://qdrant.tech/documentation/overview/>
- Neo4j GraphRAG docs: <https://neo4j.com/developer/genai-ecosystem/>
- Ragas docs: <https://docs.ragas.io/>
- DeepEval docs: <https://deepeval.com/docs/introduction>

## 文档解析和 ingestion

- LlamaParse docs: <https://developers.api.llamaindex.ai/cloud/llamaparse>
- LlamaIndex LlamaParse guide: <https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/llama_parse/>
- Docling docs: <https://www.docling.ai/>
- Unstructured docs: <https://docs.unstructured.io/welcome>
- Firecrawl docs: <https://docs.firecrawl.dev/>

## Agent 框架和编排

- LangChain agents docs: <https://docs.langchain.com/oss/python/langchain/agents>
- LangGraph docs: <https://docs.langchain.com/oss/python/langgraph>
- LlamaIndex workflows docs: <https://docs.llamaindex.ai/>
- Semantic Kernel Agent API: <https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-api>
- AutoGen stable docs: <https://microsoft.github.io/autogen/stable/index.html>
- CrewAI docs: <https://docs.crewai.com/introduction>
- Pydantic AI docs: <https://pydantic.dev/docs/ai/overview/>
- Mastra docs: <https://mastra.ai/>
- Vercel AI SDK agents docs: <https://vercel.com/docs/agents>

## 执行、沙箱和 durable execution

- E2B docs: <https://www.e2b.dev/docs>
- Daytona sandboxes docs: <https://www.daytona.io/docs/en/sandboxes/>
- Modal sandboxes docs: <https://modal.com/docs/guide/sandboxes>
- Temporal docs: <https://docs.temporal.io/>
- Restate docs: <https://docs.restate.dev/>
- Inngest docs: <https://www.inngest.com/docs/>

## 观测、评测、安全

- OpenTelemetry GenAI semantic conventions: <https://opentelemetry.io/docs/specs/semconv/gen-ai/>
- Arize Phoenix docs: <https://arize.com/docs/phoenix>
- Arize Phoenix LLM traces: <https://arize.com/docs/phoenix/tracing/llm-traces>
- OpenInference / Phoenix docs: <https://phoenix.arize.com/>
- Langfuse OpenTelemetry docs: <https://langfuse.com/integrations/native/opentelemetry>
- OpenAI Agents SDK tracing: <https://openai.github.io/openai-agents-python/tracing/>
- Claude Code hooks: <https://code.claude.com/docs/en/hooks>
- Promptfoo red teaming docs: <https://www.promptfoo.dev/docs/guides/llm-redteaming/>
- NVIDIA NeMo Guardrails docs: <https://docs.nvidia.com/nemo/guardrails/latest/index.html>
- OpenAI Agents SDK guardrails: <https://openai.github.io/openai-agents-python/guardrails/>

## 工具生态和模型网关

- Official MCP Registry: <https://registry.modelcontextprotocol.io/>
- MCP Registry repo: <https://github.com/modelcontextprotocol/registry>
- Docker MCP Gateway: <https://docs.docker.com/ai/mcp-gateway/>
- LiteLLM docs: <https://docs.litellm.ai/>
- Portkey AI Gateway docs: <https://portkey.ai/docs/product/ai-gateway>
- Vercel AI Gateway docs: <https://vercel.com/docs/ai-gateway/>
- OpenRouter docs: <https://openrouter.ai/docs/api-reference/overview>

## 本次判断

高优先级不是因为这些名字“热”，而是因为它们代表 Agent 系统从 demo 到 production 时必须面对的工程层：检索、解析、运行、状态、沙箱、观测、评测、权限和模型路由。

---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "project-expression"
  - "agent"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/05_%E9%A1%B9%E7%9B%AE%E8%A1%A8%E8%BE%BE/02_%E4%BA%A4%E6%98%93Agent%E4%B8%8E%E9%A3%8E%E6%8E%A7%E5%B9%B3%E5%8F%B0/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/05_项目表达/02_交易Agent与风控平台/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "05_项目表达"
category: "02_交易Agent与风控平台"
last_checked: 2026-05-09
freshness: watch
sha256: b81ed7a485da6da5ab2a26d58ced2d05ae51a16805d08d56c1b5afd1002c40b2
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Reranking]]"
  - "[[Retriever]]"
  - "[[Chunking]]"
  - "[[Document Ingestion]]"
  - "[[RAG]]"
  - "[[RAG 主题]]"
---

# 如何做 RAG，文档切片怎么设计，如何评估效果？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/05_项目表达/02_交易Agent与风控平台/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/05_%E9%A1%B9%E7%9B%AE%E8%A1%A8%E8%BE%BE/02_%E4%BA%A4%E6%98%93Agent%E4%B8%8E%E9%A3%8E%E6%8E%A7%E5%B9%B3%E5%8F%B0/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`05_项目表达` / `02_交易Agent与风控平台`  
条目类型：`question`  
父级题组：你最该准备的 12 道题
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Reranking]]
- [[Retriever]]
- [[Chunking]]
- [[Document Ingestion]]
- [[RAG]]
- [[RAG 主题]]

## 题目正文

**4. 如何做 [[RAG]]，文档切片怎么设计，如何评估效果？**
这是现在 AI 工程方向的通用高频题。你至少要能回答：[[Chunking|chunk]] 大小、overlap、metadata、hybrid retrieval、MMR 去重、[[Reranking|重排序]]、离线评估与线上指标。牛客整理的 2026 Java/AI 工程题里，把 RAG 架构、[[Retriever|检索]]优化、长上下文处理和效果评估都列成高频点。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。

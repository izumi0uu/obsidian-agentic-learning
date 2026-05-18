# Agentic Learning Obsidian Wiki

这是一个用 Obsidian + LLM 维护的 Agent 学习知识库。它的目标不是收藏资料，而是把 Agent、LLM、RAG、Memory、Evaluation、Tool Use、MCP、Computer Use、GraphRAG、Agentic RAG 等概念，从零散链接变成可以持续复习、追问和实验的 wiki。

一句话：Obsidian 是阅读和浏览界面，Codex/LLM 是维护者，Markdown 文件是可以被 Git 版本化的知识资产。

## 这个仓库解决什么问题

普通学习路径很容易变成这样：

- 看到前沿文章，先收藏。
- 看到论文，先下载 PDF。
- 看到 GitHub 项目，先 star。
- 问 AI 一个问题，得到一次性回答。
- 过几天忘了来源，也忘了自己当时理解到哪一步。

这个仓库采用 LLM Wiki 思路：资料先进 `raw/`，LLM 再把稳定理解写入 `wiki/`，术语表、问题池、页面目录和健康检查放在 `maps/`。这样每次 ingest、query、lint 都会沉淀到文件里，而不是消失在聊天记录里。

## 核心结构

```text
.
├── AGENTS.md
├── README.md
└── agentic learning/
    ├── index.md
    ├── log.md
    ├── raw/
    ├── wiki/
    ├── maps/
    ├── templates/
    └── .obsidian/
```

### `AGENTS.md`

给 Codex/LLM 看的项目规则。它定义：

- 这个仓库是 Obsidian vault，不是普通文档堆。
- `raw/`、`wiki/`、`maps/` 三层分别负责什么。
- ingest、query、lint 三种主要操作怎么执行。
- 概念卡必须保留“一句话 / 解决什么问题 / 它不是什么 / 最小例子 / 常见误解 / 相关链接”。

这是整个 LLM Wiki 的“维护协议”。没有它，LLM 很容易只做总结；有了它，LLM 才会维护一个长期增长的知识系统。

### `agentic learning/index.md`

Vault 的首页。用 Obsidian 打开后建议从这里进入。

它提供：

- 快速入口。
- 当前核心概念 Dataview 表。
- 待整理来源列表。
- 最近更新列表。
- 问题驱动复习入口。

### `agentic learning/raw/`

来源证据层。这里回答“这个说法从哪里来？”

子目录包括：

- `articles/`：文章、报告、实践指南。
- `docs/`：官方文档，例如 LangGraph、OpenAI Agents SDK、MCP、Neo4j GraphRAG。
- `papers/`：论文来源笔记。
- `papers/extracted/`：PDF 解析后的 Markdown 文本，可进 Git。
- `repos/`：GitHub 项目和示例仓库笔记。
- `inbox/`：临时收集，还没整理的内容。

注意：PDF 原文件放在 `raw/papers/assets/`，但被 `.gitignore` 忽略。仓库保留来源笔记和抽取文本，不提交大体积二进制资料。

### `agentic learning/wiki/`

结构化理解层。这里回答“我现在怎么理解？”

子目录包括：

- `concepts/`：一张卡只讲一个概念，例如 `Agent.md`、`Agent Loop.md`、`GraphRAG.md`、`Neo4j.md`。
- `topics/`：主题聚合页，例如 Agent、LLM、RAG。
- `projects/`：项目或工具教程，例如 oh-my-codex。

概念卡不是摘抄，而是可复习的理解单元。每张卡最好有边界说明，尤其是“它不是什么”，避免把相近概念混在一起。

### `agentic learning/maps/`

导航和维护层。这里回答“下一步去哪？”

核心页面：

- `01 术语表.md`：术语入口。
- `02 问题池.md`：还没弄清的问题。
- `03 前沿追踪.md`：前沿概念和主源追踪。
- `04 页面目录.md`：静态页面目录。
- `05 Query 写回队列.md`：值得沉淀但还没写入 wiki 的问答。
- `06 Wiki 健康检查.md`：缺链接、证据、过期、矛盾的维护记录。
- `LLM Wiki 工作流.md`：本 vault 的操作流程。
- `字段规范.md`：frontmatter 字段标准。
- `插件配置.md`：Obsidian 插件和本地 Codex skill 配置说明。

### `agentic learning/templates/`

Obsidian 模板：

- `概念卡.md`
- `网页剪藏.md`
- `阅读笔记.md`
- `前沿追踪.md`
- `实验记录.md`

新页面尽量从模板开始，避免字段和结构漂移。

### `agentic learning/log.md`

追加式维护日志。每次重要 ingest、query 写回、lint、结构调整都应该追加记录。

它的价值不是“记流水账”，而是让未来的 LLM 和你自己知道：这个 vault 为什么变成现在这样。

## Obsidian 使用方式

1. 打开 Obsidian。
2. 选择 `Open folder as vault`。
3. 选择本仓库里的 `agentic learning/` 文件夹。
4. 从 `index.md` 开始浏览。
5. 打开 Graph View 查看概念之间的连接。

建议启用：

- Obsidian Web Clipper：收集网页到 `raw/inbox/`。
- Dataview：渲染首页和知识地图中的动态表格。
- Templater：新建概念卡、阅读笔记、实验记录时自动填字段。

插件包本身不提交到 Git。换机器时按 `maps/插件配置.md` 重新安装即可。

## Codex / LLM 维护方式

本机已配置过一个 Codex skill：

```text
~/.codex/skills/obsidian-llm-wiki
```

常用指令：

```text
用 obsidian-llm-wiki ingest [[某篇 raw source]]
用 obsidian-llm-wiki query：Agentic RAG 和 GraphRAG 有什么区别？
用 obsidian-llm-wiki lint 这个 vault
```

工作边界：

- raw 是证据，尽量不改写。
- wiki 是理解，可以持续更新。
- maps 是导航，不塞长篇摘抄。
- durable answer 要写回 wiki 或 `05 Query 写回队列.md`。
- 不懂的问题写入 `02 问题池.md`，比制造一个模糊答案更有价值。

## 公开搜索索引

仓库根目录的 `search-index.json` 是给 GitHub 公开浏览、外部静态搜索或轻量检索工具使用的 Markdown 搜索索引。它由 `scripts/build_search_index.py` 从仓库内可提交的 Markdown 生成，包含标题、路径、GitHub URL、frontmatter 摘要字段、heading、excerpt 和截断正文。

更新方式：

```bash
python3 scripts/build_search_index.py
python3 scripts/build_search_index.py --check
```

GitHub Actions 会在 push / pull request 时运行 `--check`，防止 Markdown 已更新但搜索索引忘记同步。这个索引是公开消费文件，不是本地向量库；`.qdrant/`、`.chroma/`、SQLite、parquet 等本地检索缓存仍然不进入 Git。

## 推荐学习循环

1. 收集：文章、论文、文档、repo 先进入 `raw/`。
2. 消化：让 LLM 从 raw 生成或更新 concept cards。
3. 连接：把新卡接入 topic、术语表、问题池或知识地图。
4. 追问：学完一个概念后，让 Codex 生成问题，自己用费曼方式解释。
5. 写回：把卡住的点写回 `02 问题池.md`，把值得长期保留的解释写回 `05 Query 写回队列.md` 或概念卡。
6. 维护：每周 lint 一次，查孤立页、缺证据、过期资料和重复概念。

## Git 与资源策略

这个仓库适合提交：

- Markdown 笔记。
- Obsidian 基础配置。
- 模板。
- 抽取后的文本。
- LLM 维护规则。

这个仓库不提交：

- PDF 原文。
- 图片、音频、视频。
- Obsidian 插件包和主题包。
- 本地 workspace 状态。
- `.env`、密钥、数据库、向量索引、缓存。

原因很简单：GitHub 应该保存可审查、可 diff、可协作的知识结构；大体积和机器相关资源留在本地或另放对象存储。

## 参考

- [Karpathy: llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：启发了本项目的核心模式，也就是 raw source、wiki、schema/AGENTS 共同组成一个可持续维护的知识系统。
- [知乎文章](https://zhuanlan.zhihu.com/p/2024270745056937793)：作为中文语境下理解 LLM Wiki / Obsidian 第二大脑工作流的参考入口。

## 当前边界

这个 vault 不是“已经学会 Agent”的证明。它只是把资料、概念和问题放到了一个可维护的系统里。

真正学会的标准仍然是：你能不用照着卡片，用自己的话解释一个概念，并能说清它解决什么、不解决什么、在工程里怎么用。

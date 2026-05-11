---
type: concept
topic:
  - coding-agent
  - agent
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[AGENTS.md and Codex Agent Loop]]"
evidence:
  - "[[AGENTS.md and Codex Agent Loop#为什么收]]"
related:
  - "[[Coding Agent]]"
  - "[[Repo Context]]"
  - "[[Sandbox Workspace]]"
  - "[[Agent Harness]]"
---

# AGENTS.md

## 一句话

AGENTS.md 是给代码 Agent 读取的仓库级操作说明。

## 它解决什么问题

代码 Agent 进入一个 repo 时，不知道项目惯例、测试命令、禁止操作、目录职责、提交规范和验证边界。AGENTS.md 把这些信息写成 Agent 可读的上下文，减少它乱猜。

## 它不是什么

AGENTS.md 不是 README。

README 面向人类用户和开发者；AGENTS.md 更像给 Agent 的“本仓库工作规程”。它应该清楚告诉 Agent 如何探索、修改、测试、避免破坏用户改动。

## 最小例子

一个 AGENTS.md 可以写：

- 改代码前先读 `maps/字段规范.md`。
- raw source 不要删除。
- 修改概念卡必须保留“它不是什么”。
- 追加 log，不重写历史。

## 常见误解 / 风险

- 写太长会让 Agent 忽略重点。
- 指令冲突会让行为不可预测。
- 多层 AGENTS.md 要注意作用范围。
- 不要把机密信息写进 AGENTS.md。

## 边界细节

AGENTS.md 的边界由文件所在目录决定：越靠近被编辑文件的 AGENTS.md 越具体，系统 / developer / user prompt 仍然比仓库文件优先。它适合写稳定工作规程，不适合写临时任务状态或本地运行缓存。

在这个 vault 里，项目 `AGENTS.md` 是 Obsidian 学习库的 durable guidance，不应被 OMX runtime installer 噪音覆盖；OMX / Codex 的本地运行状态应放在 `.omx/`、`.codex/` 或全局 Codex 配置中。

## 现代性状态

AGENTS.md 是当前 coding-agent 工程实践中的 repo-context 约定，但不是统一行业标准协议。它的概念价值稳定；具体读取规则、优先级和文件名语义依赖 Codex / coding-agent 产品实现，所以本卡保持 seed-lite，不强行扩写成协议卡。

## 复习触发

- 为什么 AGENTS.md 不等于 README？
- 多层 AGENTS.md 冲突时，为什么更深层文件通常更具体？
- 在本项目里，为什么不能让 OMX setup 覆盖学习 vault 的 AGENTS.md？

## 证据锚点

- Evidence type: source note — [[AGENTS.md and Codex Agent Loop]]。
- Boundary: 当前卡只解释 AGENTS.md 作为 coding-agent repo guidance 的学习边界；不同 coding-agent 产品对文件发现和优先级的实现需看各自文档。
- Engineering synthesis: “项目 durable guidance 与 OMX runtime artifact 分离”来自本 vault 的协作规则。
- Confidence: medium。

## 相关链接

- [[Coding Agent]]
- [[Repo Context]]
- [[Sandbox Workspace]]
- [[Agent Harness]]

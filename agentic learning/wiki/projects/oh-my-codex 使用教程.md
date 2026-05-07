---
type: project-index
topic:
  - agent
  - coding-agent
  - workflow
  - tools
status: active
created: 2026-05-06
updated: 2026-05-07
source:
  - "[[Oh My Codex Repo]]"
related:
  - "[[Oh My Codex (OMX)]]"
  - "[[Agent Harness]]"
  - "[[Coding Agent]]"
  - "[[Sandbox Workspace]]"
  - "[[Trace]]"
  - "[[AGENTS.md]]"
---

# oh-my-codex 使用教程

这份教程按“零基础但能动手”的方式写。目标不是背完所有命令，而是知道什么时候该用 OMX、怎么安全启动、怎么用核心 workflow、出了问题先查哪里。

## 0. 先建立心智模型

OMX 不是新模型。

```text
Codex CLI = 执行 Agent
OMX = Codex 外面的 workflow + harness + team runtime + state/logs/hooks
```

你可以把它理解成：

- Codex 负责读代码、写代码、跑命令。
- OMX 负责让 Codex 先澄清、再计划、再执行、再验证。
- `.omx/` 负责保存计划、日志、状态和部分记忆。
- tmux 负责让多个 worker 同时跑。
- git worktree 负责隔离 worker 的文件修改。
- hooks/HUD 负责观察会话状态。

## 1. 什么时候值得用 OMX

适合：

- 中大型代码任务。
- 需要先澄清需求的任务。
- 需要计划、验证、回滚或审计的任务。
- 可以拆成多个子任务并行的任务。
- 需要长期执行、断点恢复、日志和状态追踪的任务。

不适合：

- 一句命令能完成的小事。
- 你只是想问一个概念。
- 仓库很危险，里面有生产凭据或不可逆脚本。
- 任务边界极不清楚，且你不愿意先回答澄清问题。

## 2. 安装前提

推荐环境：

- macOS 或 Linux。
- Node.js 20+。
- 已安装 OpenAI Codex CLI。
- 已完成 Codex 登录。
- 已安装 tmux，尤其是要用 `$team` 时。
- 当前 shell 能访问同一个 `~/.codex` 或 `CODEX_HOME`。

安装 tmux：

```bash
# macOS
brew install tmux

# Ubuntu / Debian
sudo apt install tmux
```

## 3. 安装和更新

安装：

```bash
npm install -g @openai/codex oh-my-codex
```

安装后手动初始化：

```bash
omx setup
```

更新：

```bash
npm install -g oh-my-codex
omx setup
```

或者：

```bash
omx update
```

## 4. 第一次启动前必须检查

先检查 OMX 自己：

```bash
omx doctor
```

再检查 Codex 登录状态：

```bash
codex login status
```

再跑真实模型调用 smoke test：

```bash
omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"
```

边界：`omx doctor` 只能说明本地安装形状看起来正常，不等于 Codex 账号、环境变量、base URL、模型调用一定正常。

## 4.1 中转站 API Key / 本地 Codex 账号配置

OMX 本身不需要单独配置一份中转站 API key。

OMX 的核心行为是启动或包装 Codex CLI，所以它默认遵循当前 shell 里的 Codex 配置：

```text
CODEX_HOME 未设置 -> 使用 ~/.codex
~/.codex/config.toml -> 决定 model_provider / base_url / MCP
~/.codex/auth.json 或环境变量 -> 决定认证信息
```

也就是说，如果普通 Codex 已经切换到中转站成功，OMX 一般会自动跟随。

检查当前 Codex 账号：

```bash
codex login status
```

检查当前 provider：

```bash
rg -n "model_provider|\\[model_providers|base_url|wire_api|requires_openai_auth" ~/.codex/config.toml
```

典型配置形状：

```toml
model = "gpt-5.5"
model_provider = "gettoken"

[model_providers.gettoken]
name = "GetToken"
base_url = "https://your-relay.example/v1"
wire_api = "responses"
requires_openai_auth = true
```

只要你不设置另一个 `CODEX_HOME`，OMX 就会读取同一份 `~/.codex/config.toml`。

用 OMX 做一次真实 smoke test：

```bash
omx exec --skip-git-repo-check -C . "Reply with exactly OMX-RELAY-OK"
```

如果普通 `codex` 可以用中转站，但 `omx` 不行，优先检查：

```bash
echo "${CODEX_HOME:-<unset>}"
which codex
which omx
codex login status
rg -n "model_provider|base_url" ~/.codex/config.toml
```

常见原因：

- 在另一个 shell 里设置了不同的 `CODEX_HOME`。
- 通过 GUI/IDE 启动时没有继承终端里的环境变量。
- project scope 的 `.codex/config.toml` 覆盖了部分配置。
- 中转站只兼容某种 `wire_api`，例如 `responses` 或 chat completions，和 Codex 当前配置不匹配。

边界：如果你为了隔离 OMX 设置 `CODEX_HOME=~/.codex-omx`，那账户、provider、MCP、skills 都会变成另一套，需要重新同步。这通常不推荐。

## 4.2 Project Scope 弹出 Codex 登录页

如果启动 OMX 后出现 Codex 登录选择页：

```text
Sign in with ChatGPT
Sign in with Device Code
Provide your own API key
```

常见原因是：你用的是 project scope。OMX 会把 Codex home 切到当前项目的 `./.codex`，而这个目录没有你的全局登录态。

```text
普通 Codex: ~/.codex/auth.json
Project-scope OMX: ./.codex/auth.json
```

如果你已经在普通 Codex 里成功切到中转站，不要急着重新登录 ChatGPT。先退出这个界面，然后选下面一种方式。

### 方式 A：临时共享全局 Codex 配置

适合：只想快速跑一次，继续使用 `~/.codex` 里的账号、provider、MCP。

```bash
cd /path/to/project
CODEX_HOME="$HOME/.codex" omx --high
```

如果这样不再弹登录页，说明问题就是 project-scope `.codex` 没有 auth/provider。

### 方式 B：让当前项目的 `.codex` 复用全局 auth

适合：你想保留 project scope 的 OMX prompts/skills/hooks，同时复用全局登录态。

```bash
cd /path/to/project
mkdir -p .codex
ln -sf "$HOME/.codex/auth.json" .codex/auth.json
test -f "$HOME/.codex/.cockpit_codex_auth.json" && ln -sf "$HOME/.codex/.cockpit_codex_auth.json" .codex/.cockpit_codex_auth.json
```

然后确认 `.codex/config.toml` 里也有和全局一致的 `model_provider` 与 `[model_providers.<name>]` 配置。不要把 relay API key 写进会提交的文件；project scope 默认会 ignore `.codex/config.toml`，但仍然要自己确认。

检查：

```bash
rg -n "model_provider|\\[model_providers|base_url|wire_api|requires_openai_auth" .codex/config.toml ~/.codex/config.toml
```

### 什么时候选登录页里的 3

只有当你想让这个项目拥有独立 API key 时，才选：

```text
3. Provide your own API key
```

如果你想沿用已经配置好的中转站账号，优先用方式 A 或方式 B。

## 4.5 手动合并 AGENTS.md

如果 `omx setup` 问：

```text
Overwrite existing AGENTS.md at "/Users/idah/.codex/AGENTS.md"? [y/N]:
```

默认选 `N`。`~/.codex/AGENTS.md` 是全局 Codex 指令，直接覆盖会影响所有项目。

想预览 OMX 要生成什么，可以用 project scope：

```bash
mkdir -p /tmp/omx-setup-preview
cd /tmp/omx-setup-preview
omx setup
```

选择：

```text
Scope: 2 project
```

注意：project scope 生成的是：

```text
/tmp/omx-setup-preview/AGENTS.md
```

不是：

```text
/tmp/omx-setup-preview/.codex/AGENTS.md
```

正确 diff：

```bash
diff -u ~/.codex/AGENTS.md /tmp/omx-setup-preview/AGENTS.md
```

不建议把临时文件整份复制到 `~/.codex/AGENTS.md`。OMX 生成的全量 AGENTS 很强，会改变全局 Codex 行为。更稳的做法是在全局文件末尾只追加一个薄规则：

```md
## Oh My Codex / OMX

When using oh-my-codex, prefer clarify -> plan -> execute -> verify for non-trivial work.

Use OMX workflows only when explicitly invoked or clearly useful:
- `$deep-interview` for unclear requirements.
- `$plan` / `$ralplan` for planning and tradeoff review.
- `$ralph` for owner-style execution with verification.
- `$team` for parallel work with clearly separated scopes.
- `$ultragoal` for long multi-stage goals.

For team work, keep worker ownership boundaries clear, avoid overlapping writes, preserve user changes, and verify integration before considering the task complete.

Do not treat OMX as a replacement for tests, review, sandboxing, or human approval.
```

## 4.6 按需启用方案

如果目标是“平时不用 OMX，只有某些项目需要时再启用”，推荐这样分层：

```text
Codex 账户 / API key / 普通 MCP / 自己的 skills：继续共享 ~/.codex
OMX 程序本体：保留 npm 全局 omx 命令
OMX prompts / skills / hooks / MCP / AGENTS：只装到需要的项目
```

不要为了隔离 OMX 轻易改 `CODEX_HOME`。那会把账户、config、skills、MCP 都隔离开，反而更麻烦。

在某个项目里按需启用：

```bash
cd /path/to/project
omx setup --scope project
omx doctor
```

project scope 会生成：

```text
AGENTS.md
.codex/
.omx/
```

其中：

- `AGENTS.md` 是项目级 OMX orchestration brain。
- `.codex/` 放项目级 prompts、skills、agents、hooks/config。
- `.omx/` 放 runtime state、plans、logs、HUD 配置等。

如果曾经误跑了 user scope，想恢复到“按需启用”状态：

```bash
omx uninstall
```

它会清理全局 `~/.codex` 里的 OMX 注入，包括 OMX hooks、OMX MCP、OMX prompts、OMX skills、OMX native agents 和 OMX config block，但不会卸载 npm 里的 `omx` 命令，也不会删除 Codex 登录。

清理后看到：

```bash
omx doctor
```

报告 user-scope 缺 prompts、skills、MCP，是正常的，因为你选择的是“项目按需安装”。

确认普通 Codex 账户还在：

```bash
codex login status
```

确认全局没有 OMX 注入：

```bash
rg -n "oh-my-codex|omx_|OMX|codex-native-hook|notify-hook" ~/.codex/config.toml ~/.codex/AGENTS.md
test -f ~/.codex/hooks.json && echo "hooks exists" || echo "no global hooks"
```

临时预览目录可以直接删：

```bash
rm -rf /tmp/omx-setup-preview
```

## 5. 推荐启动方式

官方推荐的强启动方式：

```bash
omx --madmax --high
```

更保守的学习启动方式：

```bash
omx --high
```

不想让 OMX 管 tmux/HUD，只想一次性直接启动：

```bash
omx --direct --yolo
```

长期偏好 direct：

```bash
OMX_LAUNCH_POLICY=direct omx --yolo
```

恢复默认：

```bash
unset OMX_LAUNCH_POLICY
```

## 6. 最重要的 5 个入口

### `$deep-interview`

用途：需求不清楚时，先让 Codex 问你问题。

```text
$deep-interview "我要重构登录系统，但还没想清边界，请先访谈我"
```

适合：

- 需求模糊。
- 风险不清。
- 成功标准不清。
- 不知道该不该拆任务。

### `$ralplan`

用途：把澄清后的需求变成计划，并审查取舍。

```text
$ralplan "给登录重构做计划，列出风险、验证方式和不做什么"
```

适合：

- 大改动前。
- API、数据库、安全、架构变化前。
- 你想先看计划再让 Agent 动手。

底层机制：

```text
$ralplan
-> prompt routing 进入 planning workflow
-> .omx/state/.../ralplan-state.json 记录 phase
-> .omx/plans/prd-*.md 和 test-spec-*.md 保存计划产物
-> stop hook 防止计划未完成就静默停止
```

边界：`$ralplan` 不负责实现。它的产物是 approved plan / handoff，后续再交给 `$ralph` 或 `$team`。

### `$ralph`

用途：让一个 owner 持续执行直到验证完成。

```text
$ralph "按已批准计划修复登录 bug，跑测试并修到通过"
```

适合：

- 任务边界清楚。
- 需要持续 debug。
- 不一定需要并行。

### `$team`

用途：让多个 worker 并行处理任务。

```text
$team 3:executor "并行完成 API、前端和测试更新"
```

适合：

- 任务能清楚拆分。
- 每个 worker 写不同区域。
- 有测试或验收标准。

不适合：

- 文件高度重叠。
- 需求还没澄清。
- 你不想处理 integration report 或合并结果。

### `$ultragoal`

用途：把大目标拆成 durable goals，让长任务跨多个 Codex goal 继续推进。

```text
$ultragoal "把这个发布任务拆成可验证的连续目标"
```

适合：

- 多阶段发布。
- 研究 + 实现 + 验证。
- 一次会话完成不了的大目标。

## 7. 推荐日常流程

### 模糊需求

```text
$deep-interview "先问清这个功能需求"
$ralplan "基于访谈结果制定计划"
$ralph "执行计划并验证"
```

### 中型功能

```text
$deep-interview "澄清功能边界和非目标"
$ralplan "制定实现计划，列验收标准"
$team 3:executor "并行实现计划中可拆的部分"
$ralph "整合、修复、跑测试直到通过"
```

### bug 修复

```text
$ralplan "分析失败原因，给出最小修复计划"
$ralph "实现修复并跑测试"
```

### 只读探索

```bash
omx explore --prompt "找出这个项目的登录流程入口"
```

### shell 检查

```bash
omx sparkshell git status
omx sparkshell "npm test"
```

## 8. Team 模式怎么工作

核心流程：

```text
leader workspace
  -> omx team
  -> worker-1 worktree
  -> worker-2 worktree
  -> worker-3 worktree
  -> leader incremental integration
```

关键目录：

```text
.omx/team/<team-name>/worktrees/worker-N
.omx/state/team/<team-name>/
.omx/state/team/<team-name>/integration-report.md
```

常用命令：

```bash
omx team 3:executor "fix failing tests with verification"
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

强制关闭死掉的 team：

```bash
omx team shutdown <team-name> --force --confirm-issues
omx cancel
omx doctor --team
```

只在你确认 team 已经死掉或要放弃时用 force。

## 9. 用 `$team` 前的安全清单

启动前检查：

- 当前 leader workspace 是否干净。
- 是否已经 commit 或 stash 你的手工改动。
- 任务是否能拆成不同区域。
- 是否有明确验收标准。
- 是否有测试命令。
- 是否没有生产凭据、真实数据库或不可逆脚本暴露给 worker。

Worker 完成时最好显式 commit：

```bash
git add -A
git commit -m "task: <subject>"
```

如果 worker 忘记，OMX 可能自动 commit，但显式 commit 更好审查。

## 10. `.omx/` 里有什么

常见内容：

```text
.omx/state/      # 模式、team、runtime 状态
.omx/logs/       # 审计日志
.omx/plans/      # 计划文档
.omx/wiki/       # OMX 本地 markdown-first wiki
.omx/notepad.md  # 可跨上下文保留的工作记忆
```

另外还会涉及：

```text
.codex/hooks.json   # Codex native hook 注册
.omx/hooks/*.mjs    # OMX hook plugin
AGENTS.md           # 项目级 Agent 指令
```

边界：`.omx/` 是运行状态，不等于你的产品代码。不要把里面所有东西都当成稳定文档，也不要盲目提交敏感日志。

## 11. Hooks / HUD / Notifications

Hooks 处理会话生命周期，比如 session start、tool use 前后、idle、stop、ask user question。

HUD 用来观察当前会话状态：

```bash
omx hud --watch
omx hud --json
```

通知可以接 Telegram、Discord、Slack 或 generic webhook。适合长任务等待时提醒你“需要输入”或“任务结束”。

最小原则：

- 先不要配通知。
- 先让安装、smoke test、普通 workflow 跑通。
- 等你真的跑长任务，再配 Telegram/Slack。

## 12. 常见问题

### `omx doctor` 绿了，但启动失败

先跑：

```bash
codex login status
omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"
```

如果这里失败，优先查：

- 当前 shell 的 `HOME`。
- 当前 shell 的 `CODEX_HOME`。
- `~/.codex/config.toml`。
- API key 或登录态。
- 是否用了本地 OpenAI-compatible proxy。

### tmux 里快捷键异常

先确认你是从 OMX 推荐路径启动，而不是在奇怪的嵌套 tmux/终端里启动。

可以临时用：

```bash
omx --direct --yolo
```

### Team 卡住

先看状态：

```bash
omx team status <team-name>
```

再看：

```text
.omx/state/team/<team-name>/integration-report.md
```

确认 team 死掉后再 force shutdown。

### Windows 能用吗

官方默认推荐 macOS/Linux + tmux。Windows 原生路径不是主体验；如果是 Windows，优先考虑 WSL2 + tmux。

## 13. 安全边界

OMX 让 Codex 更会“跑流程”，但也可能让错误执行得更快。

尤其注意：

- `--madmax` / `--yolo` 会降低审批摩擦。
- Worktree 只隔离文件，不隔离外部服务。
- Hooks 可能处理敏感上下文，别随便装不可信 hook。
- 通知 webhook 不要泄露密钥。
- 真实数据库、生产账号、付费 API、删除命令都应该加人类确认。

## 14. 我建议你的 7 天练习路线

### Day 1：只安装和 smoke test

目标：确认 `omx doctor`、`codex login status`、`omx exec` 都能过。

### Day 2：用 `$deep-interview`

拿一个模糊需求，让它只问问题，不写代码。

### Day 3：用 `$ralplan`

让它把 Day 2 的答案变成计划，重点看“它不做什么”。

### Day 4：用 `$ralph`

选择一个小 bug 或小文档任务，让它持续做到验证通过。

### Day 5：用 `$team`

只选可以拆分的任务，比如“文档、测试、类型修复”三块。

### Day 6：读 `.omx/`

看 state、logs、plans、team worktrees，理解 Agent Harness 是怎么落地的。

### Day 7：复盘到 Obsidian

写一张自己的卡：

```text
OMX 对我来说解决了什么？
它不是什么？
我什么时候不该用它？
我最容易误用哪个命令？
```

## 15. 最小命令速查

```bash
# 安装
npm install -g @openai/codex oh-my-codex

# 初始化
omx setup

# 健康检查
omx doctor
codex login status
omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"

# 启动
omx --high
omx --madmax --high
omx --direct --yolo

# 恢复
omx resume

# 探索和检查
omx explore --prompt "find where auth is implemented"
omx sparkshell git status
omx hud --watch

# 团队
omx team 3:executor "fix failing tests"
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

## 16. 学习边界

先会用这几个就够了：

- `omx setup`
- `omx doctor`
- `omx exec`
- `omx --high`
- `$deep-interview`
- `$ralplan`
- `$ralph`
- `$team`

其余命令等你真的遇到对应问题再学。OMX 的正确使用方式不是“把所有命令背下来”，而是把任务放进合适的工作流。

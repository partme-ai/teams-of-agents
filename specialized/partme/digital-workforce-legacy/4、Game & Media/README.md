# Game team agents

Workspace templates for the **game** multi-agent team: Game Master (orchestrator), Game Designer, Game Architect, and Game Developer. Aligned with the terminology in [README_EN.md](../README_EN.md).

## Roles

| Directory            | Agent id        | Role            | Description |
|----------------------|-----------------|-----------------|-------------|
| `1-game-master/`     | `game-master`   | Game Master     | 游戏主持人 — facilitator and orchestrator; vision, sessions, coordination |
| `2-game-designer/`   | `game-designer` | Game Designer   | 游戏策划 — gameplay, rules, systems, levels, narrative (industry-standard role) |
| `3-game-architect/`  | `game-architect`| Game Architect  | 游戏架构师 — overall game architecture and system design (senior, technical) |
| `4-game-developer/`  | `game-developer`| Game Developer  | 游戏开发/程序开发 — client, server, tools implementation; programming (程序开发) |

## Config fragment

Use `config/openclaw-game-fragment.json`: merge its `agents`, `bindings`, and `tools.agentToAgent` into `~/.openclaw/openclaw.json`. Default agent is `game-master`; it can delegate to `game-designer`, `game-architect`, and `game-developer` via agent-to-agent.

## Quick start

```bash
openclaw agents add game-master
openclaw agents add game-designer
openclaw agents add game-architect
openclaw agents add game-developer
# Merge config/openclaw-game-fragment.json into ~/.openclaw/openclaw.json
# Copy this repo's game/* into your workspace-game/<agentId> paths
```

## 初始化命令（与 company 同规则）

以下命令在 OpenClaw 配置已就绪的前提下执行；`--workspace` 使用片段中的路径，需先将本仓库 `game/<N-xxx>/` 复制或链接到对应 workspace 目录。

### 1. 查看当前智能体列表

```bash
openclaw agents list
```

### 2. 添加游戏团队智能体（5 个）

```bash
openclaw agents add game-master     --workspace ~/.openclaw/workspace-game/game-master
openclaw agents add game-designer   --workspace ~/.openclaw/workspace-game/game-designer
openclaw agents add game-architect  --workspace ~/.openclaw/workspace-game/game-architect
openclaw agents add game-developer  --workspace ~/.openclaw/workspace-game/game-developer
openclaw agents add game-ops        --workspace ~/.openclaw/workspace-game/game-ops
```

### 3. 查看当前绑定

```bash
openclaw agents bindings
```

### 4. 按渠道绑定智能体（示例）

片段默认将 telegram、discord 路由到 game-master；若需用 CLI 显式绑定：

```bash
openclaw agents bind --agent game-master --bind telegram:game-master
openclaw agents bind --agent game-master --bind discord:game-master
```

合并 `config/openclaw-game-fragment.json` 后，其 `bindings` 与 `tools.agentToAgent` 会一并生效；上述 bind 命令可与片段二选一或互补使用。

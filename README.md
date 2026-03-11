# OpenClaw Agents

OpenClaw 多智能体配置说明与示例，遵循 [OpenClaw Multi-Agent](https://docs.openclaw.ai/concepts/multi-agent) 官方约定：在一个网关实例中运行多个隔离智能体（独立 workspace、agentDir、sessions），通过 bindings 路由入站消息。

> **官方文档**  
> - [Multi-Agent Routing](https://docs.openclaw.ai/concepts/multi-agent)（路径、单/多智能体、Agent helper、路由规则）

---

## 两件必知的事

### 如何快速把智能体配置加到 OpenClaw

1. **确认 OpenClaw 已安装**（未安装见 [§1 系统要求与安装](#1-系统要求与安装)）。
2. **准备配置**  
   若你使用本仓库提供的 **config 片段**：用任意文本编辑器打开片段，将其中占位路径（如 `<REPO_ROOT>`）**全部**替换为你的实际路径（**绝对路径**，例如 `~/.openclaw` 或 `/home/you/openclaw-agents`）。**it 软件开发团队**请使用 `config/openclaw-it-fragment.json`：workspace 使用无编号路径（如 `~/.openclaw/workspace-it/technical-director`），与 agent id 一致；须设置 `tools.agentToAgent.enabled: true` 并将 technical-director 及 12 个子角色 id 列入 `allow`；多 profile 时 it 实例的 `OPENCLAW_CONFIG_PATH`、`OPENCLAW_STATE_DIR` 与端口需独立（见 §3 多网关）。
3. **合并并重启**  
   把片段中的 `agents`、`bindings`、`tools.agentToAgent` 合并进 `~/.openclaw/openclaw.json`（若已有同名键，将 `agents.list` 与现有 list 合并，其余按需覆盖）。执行 `openclaw gateway restart`（或 `openclaw gateway` 启动）。
4. **验证**  
   `openclaw agents list --bindings`、`openclaw channels status --probe`。

以上过程不依赖任何本地或私有目录名；路径以你本机为准，与 [官方路径约定](https://docs.openclaw.ai/concepts/multi-agent#paths-quick-map) 一致（Config、State dir、Workspace、Agent dir、Sessions）。

### 如何添加新的智能体

- **方式一（推荐，与官方一致）**：执行 `openclaw agents add <agentId>`（如 `openclaw agents add work`）。向导会创建独立 workspace（如 `~/.openclaw/workspace-work`）、`agentDir`（如 `~/.openclaw/agents/work/agent`）和 session 存储。再在 `~/.openclaw/openclaw.json` 中为该智能体设置 `workspace`（**绝对路径**）、`agentDir`（**禁止**与其它智能体共用），并按需添加 `bindings` 做路由。
- **方式二**：手动创建目录 `~/.openclaw/workspace-<agentId>`，放入 SOUL.md、AGENTS.md、可选 USER.md 等；创建 `~/.openclaw/agents/<agentId>/agent` 与 `sessions`；在 `agents.list` 中增加一项，填写 `id`、`workspace`、`agentDir`。
- 详细步骤与字段说明见 [§6 创建智能体](#6-创建智能体) 和 [§7 配置智能体](#7-配置智能体)。

---

## 目录

- **[OpenClaw 使用系列](docs/README.md)** — 实战场景文章（如 [Claw + Obsidian 复工外脑](docs/01-claw-obsidian-复工外脑.md)）

1. [系统要求与安装](#1-系统要求与安装)
2. [快速开始与首次配置](#2-快速开始与首次配置)
3. [多网关（同一主机多组智能体）](#3-多网关同一主机多组智能体)
4. [智能体组（单网关内多智能体与路由）](#4-智能体组单网关内多智能体与路由)
5. [什么是「一个智能体」](#5-什么是「一个智能体」)
6. [创建智能体](#6-创建智能体)
7. [配置智能体](#7-配置智能体)
8. [完整配置示例](#8-完整配置示例)
9. [垂直领域示例：独立实例与智能体配置](#9-垂直领域示例独立实例与智能体配置)
10. [路径与部署](#10-路径与部署)
11. [模板与智能体对照](#11-模板与智能体对照)
12. [Multi-Agent 约束说明](#12-multi-agent-约束说明)
13. [故障排查](#13-故障排查)
14. [相关链接](#14-相关链接)

---

## 1. 系统要求与安装

### 系统要求

| 组件 | 最低要求 | 推荐 |
|------|----------|------|
| **操作系统** | macOS 12+ / Linux (Ubuntu 20.04+) / Windows 11 (WSL2) | macOS 14+ / Ubuntu 22.04+ |
| **Node.js** | 18.0.0+ | 20.0.0+ LTS |
| **内存** | 4GB RAM | 8GB+ RAM |
| **磁盘** | 2GB 可用空间 | 10GB+ SSD |
| **网络** | 稳定互联网连接 | - |

### 安装方式

**方式一：官方安装脚本（推荐）**

```bash
# macOS / Linux
curl -fsSL https://openclaw.ai/install.sh | bash
# 或
wget -qO- https://openclaw.ai/install.sh | bash

source ~/.bashrc   # 或 ~/.zshrc
```

**方式二：npm**

```bash
npm install -g openclaw
# 或使用 npx
npx openclaw@latest
```

**方式三：Homebrew（macOS/Linux）**

```bash
brew tap openclaw/tap
brew install openclaw
brew upgrade openclaw   # 更新
```

**方式四：从源码安装**

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw && npm install && npm run build && npm link
```

### 验证安装

```bash
openclaw --version
openclaw --help
openclaw doctor
```

---

## 2. 快速开始与首次配置

### 首次运行

```bash
# 初始化配置与工作区
openclaw setup
# 或交互式引导（网关、工作区、技能、渠道等）
openclaw onboard
```

官方 CLI 使用 `setup` / `onboard`（无 `init` 命令）。向导会引导：配置目录、默认模型、API Key、渠道登录（可选）。

### 手动创建基础配置

```bash
mkdir -p ~/.openclaw
mkdir -p ~/.openclaw/workspace ~/.openclaw/agents/main/agent
```

`~/.openclaw/openclaw.json` 最小示例：

```json5
{
  "agents": {
    "list": [
      {
        "id": "main",
        "default": true,
        "workspace": "~/.openclaw/workspace",
        "agentDir": "~/.openclaw/agents/main/agent"
      }
    ]
  }
}
```

### 配置 API Key

- **环境变量**：`ANTHROPIC_API_KEY`、`OPENAI_API_KEY`、`DEEPSEEK_API_KEY` 等，写入 `~/.bashrc` 或 `~/.zshrc` 后 `source`。
- **配置文件**：在 `~/.openclaw/agents/main/agent/auth-profiles.json` 中配置 profiles（name + apiKey），并执行 `chmod 600` 保护。

### 启动网关

```bash
openclaw gateway              # 前台
openclaw gateway --port 8080  # 指定端口
# 后台：安装为服务后启动（openclaw gateway install && openclaw gateway start），或 nohup openclaw gateway &
```

---

## 3. 多网关（同一主机多组智能体）

### 为何需要多网关

一个 OpenClaw Gateway 实例即可承载**多路消息连接**和**多个智能体**（通过 bindings 路由）。若你需要在**同一台主机**上跑**多组彼此隔离的智能体组**（例如：主业务一组、救援/调试一组，或不同团队/环境各一组），则应运行**多个 Gateway 实例**，即「多网关」。典型场景包括：

- **隔离与冗余**：主机器人一组、救援机器人一组；主宕机时用救援实例调试或改配置。
- **多环境/多团队**：同一台机器上，不同 profile 对应不同配置、工作区与端口，互不干扰。
- **资源与端口隔离**：每组智能体使用独立配置、状态目录、工作区与端口，避免配置竞争和端口冲突。

以下为 OpenClaw 官方文档 [Multiple Gateways (same host)](https://docs.openclaw.ai/gateway/multiple-gateways) 的要点与操作说明。

### 隔离检查清单（必需）

每个网关实例必须独立以下项，否则会出现配置竞争和端口冲突：

- **`OPENCLAW_CONFIG_PATH`** — 每个实例一份配置文件
- **`OPENCLAW_STATE_DIR`** — 每个实例的会话、凭证、缓存
- **`agents.defaults.workspace`** — 每个实例的工作区根目录（若使用）
- **`gateway.port`（或 `--port`）** — 每个实例端口唯一
- **派生端口（浏览器/画布/CDP）** — 不得重叠

### 推荐：使用配置文件（`--profile`）

`--profile` 会按实例自动限定 `OPENCLAW_STATE_DIR` 与 `OPENCLAW_CONFIG_PATH`，并为服务名称加后缀。

```bash
# 主实例
openclaw --profile main setup
openclaw --profile main gateway --port 18789

# 另一组（例如救援）
openclaw --profile rescue setup
openclaw --profile rescue gateway --port 19001
```

按 profile 安装为系统服务：

```bash
openclaw --profile main gateway install
openclaw --profile rescue gateway install
```

### 救援机器人指南

在同一主机上运行第二个 Gateway，需独立：profile/配置、状态目录、工作区、基础端口（及派生端口）。这样主机器人宕机时，救援实例仍可调试或应用配置更改。

**端口间距**：两个实例的基础端口之间至少间隔 **20**，以免派生的浏览器/画布/CDP 端口冲突（例如 18789 与 19001，或 18789 与 19789）。

```bash
# 主实例（默认，不带 --profile）
openclaw onboard
openclaw gateway install

# 救援实例（独立 profile + 端口）
openclaw --profile rescue onboard
# 说明：工作区名称默认带 -rescue 后缀；端口建议 ≥ 18789+20，如 19789
openclaw --profile rescue gateway install
```

### 端口映射（派生）

- **基础端口** = `gateway.port`（或 `OPENCLAW_GATEWAY_PORT` / `--port`）
- 浏览器控制服务端口 = 基础 + 2（仅 loopback）
- Canvas 在 Gateway HTTP 同端口提供；部分部署中 `canvasHost.port = 基础 + 4`
- 浏览器 CDP 端口从 `browser.controlPort + 9 .. + 108` 自动分配

若在配置或环境中覆盖上述任一项，需保证每个实例取值唯一。

### 浏览器/CDP 注意事项（常见陷阱）

- **不要**在多个实例上把 `browser.cdpUrl` 配成相同值。
- 每个实例需自己的浏览器控制端口和 CDP 范围（由该实例的 gateway 端口派生）。
- 若需显式 CDP 端口，按实例设置 `browser.profiles.<name>.cdpPort`。
- 远程 Chrome：使用 `browser.profiles.<name>.cdpUrl`（按 profile、按实例）。

### 手动环境变量示例

```bash
OPENCLAW_CONFIG_PATH=~/.openclaw/main.json \
OPENCLAW_STATE_DIR=~/.openclaw-main \
openclaw gateway --port 18789

OPENCLAW_CONFIG_PATH=~/.openclaw/rescue.json \
OPENCLAW_STATE_DIR=~/.openclaw-rescue \
openclaw gateway --port 19001
```

### 快速检查

```bash
openclaw --profile main status
openclaw --profile rescue status
openclaw --profile rescue browser status
```

---

## 4. 智能体组（单网关内多智能体与路由）

**智能体组**指在**同一个 Gateway 实例**内配置的多个智能体（`agents.list`），通过 **bindings** 将入站消息路由到不同智能体。本节说明单网关内多智能体与路由规则。

### 路由规则（最具体优先）

1. `peer` 匹配（精确 DM/群组/渠道 ID）
2. `parentPeer` 匹配（线程继承）
3. `guildId + roles`（Discord 角色）
4. `guildId`（Discord）
5. `teamId`（Slack）
6. 渠道的 `accountId` 匹配
7. 渠道级别匹配（`accountId: "*"`）
8. 回退到默认智能体（`default: true` 或列表首项）

### 绑定示例

```json5
{
  bindings: [
    { agentId: "deep-work", match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551234567" } } },
    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },
    { agentId: "main", match: { channel: "telegram" } },
  ]
}
```

### 匹配字段说明

| 字段 | 说明 | 示例 |
|------|------|------|
| `channel` | 渠道类型 | `whatsapp`, `telegram`, `discord` |
| `accountId` | 渠道账号标识 | `personal`, `biz`, `default` |
| `peer.kind` | 对话类型 | `direct`（私聊）, `group`（群组） |
| `peer.id` | 对话唯一标识 | 手机号、群组 ID、频道 ID |
| `guildId` | Discord 服务器 ID | `"123456789012345678"` |

---

## 5. 什么是「一个智能体」

每个**智能体（Agent）**是独立范围的「大脑」，拥有自己的：

| 组件 | 描述 | 路径 |
|------|------|------|
| **工作空间（Workspace）** | 文件、AGENTS.md/SOUL.md/USER.md、本地笔记、角色规则 | `~/.openclaw/workspace-<agentId>` 或配置的路径 |
| **状态目录（agentDir）** | 认证、模型注册表、智能体专属配置 | `~/.openclaw/agents/<agentId>/agent` |
| **会话存储** | 聊天历史与路由状态 | `~/.openclaw/agents/<agentId>/sessions` |

**单智能体模式（默认）**：不配置多智能体时，`agentId` 默认为 `main`，工作空间为 `~/.openclaw/workspace`，状态为 `~/.openclaw/agents/main/agent`。

---

## 6. 创建智能体

### 方法一：使用向导（推荐）

```bash
openclaw agents add
openclaw agents add work
openclaw agents add personal
```

向导会引导：命名、工作空间路径、状态目录路径、渠道绑定（可选）。

### 方法二：手动创建

```bash
mkdir -p ~/.openclaw/workspace-work
cd ~/.openclaw/workspace-work
touch AGENTS.md SOUL.md USER.md

mkdir -p ~/.openclaw/agents/work/agent
mkdir -p ~/.openclaw/agents/work/sessions

vim ~/.openclaw/openclaw.json
```

在 `agents.list` 中新增：

```json5
{
  id: "work",
  name: "Work",
  workspace: "~/.openclaw/workspace-work",
  agentDir: "~/.openclaw/agents/work/agent",
}
```

### 方法三：复制现有智能体

```bash
cp -r ~/.openclaw/workspace ~/.openclaw/workspace-copy
cp -r ~/.openclaw/agents/main ~/.openclaw/agents/copy
# 在 openclaw.json 中增加 copy 的 list 项，并修改 id/workspace/agentDir
```

### 方法四：按 IT 片段用 openclaw agents add 添加智能体（与官方一致）

与 [OpenClaw Multi-Agent](https://docs.openclaw.ai/concepts/multi-agent) 的 **Agent helper**、**Quick start** 一致：先用 `openclaw agents add <agentId>` 为每个角色创建独立 workspace、agentDir 和会话存储，再合并本仓库的配置片段得到 bindings 与 agent-to-agent。

**1. 用向导逐个添加 IT 团队 13 个智能体**

片段中的 `agentId` 与官方要求一致，可直接作为 `openclaw agents add` 的参数：

```bash
openclaw agents add technical-director
openclaw agents add project-manager
openclaw agents add product-manager
openclaw agents add system-architect
openclaw agents add domain-expert
openclaw agents add ux-designer
openclaw agents add ui-designer
openclaw agents add backend-engineer
openclaw agents add database-engineer
openclaw agents add frontend-engineer
openclaw agents add mobile-engineer
openclaw agents add qa-engineer
openclaw agents add ops-engineer
```

向导会为每个 id 创建 `~/.openclaw/workspace-<agentId>`、`~/.openclaw/agents/<agentId>/agent` 和 sessions；若希望统一放在 `workspace-it` 目录下，可在向导里填 `~/.openclaw/workspace-it/<agentId>`，或添加后再在配置里把 `workspace` 改为片段中的路径。

**2. 合并片段中的 agents、bindings、tools.agentToAgent**

将 `config/openclaw-it-fragment.json` 中的 `agents`（含 `defaults` 与 `list`）、`bindings`、`tools.agentToAgent` 合并进 `~/.openclaw/openclaw.json`。若已有 `agents.list`，把片段的 list 与现有 list 合并（按 id 去重或替换），并保留片段的 `bindings` 和 `tools.agentToAgent`，使 Telegram/Discord 入站路由到 technical-director、且编排者可委派到上述 12 个子角色。

**3. 可选：使用本仓库 it/ 下的角色工作空间**

本仓库 `it/` 目录下有针对各角色的 AGENTS.md、SOUL.md 等模板。可将对应子目录复制或链接到上述 workspace 路径，例如：

```bash
# 示例：技术总监工作空间指向仓库 it 目录
cp -r /path/to/openclaw-agents/it/technical-director/* ~/.openclaw/workspace-it/technical-director/
```

**4. 重启并验证**

```bash
openclaw gateway restart
openclaw agents list --bindings
openclaw channels status --probe
```

---

## 7. 配置智能体

### 配置文件位置

主配置：`~/.openclaw/openclaw.json`（支持 JSON5）。可通过 `OPENCLAW_CONFIG_PATH` 覆盖。

### 智能体配置字段

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | string | 是 | 唯一标识，用于路由 |
| `name` | string | 否 | 显示名称 |
| `default` | boolean | 否 | 是否为默认智能体（回退路由） |
| `workspace` | string | 是 | 工作空间**绝对路径** |
| `agentDir` | string | 是 | 状态目录，**禁止**多智能体共用 |
| `model` | string | 否 | 默认模型 |

### 智能体列表说明（以 openclaw-it-fragment 为例）

本仓库 `config/openclaw-it-fragment.json` 定义了一个**软件开发团队**：1 个编排者 + 12 个子角色，共用同一 Gateway，通过 **bindings** 将入站渠道路由到默认入口，再经 **agent-to-agent** 委派到具体角色。

**agents.defaults**（可选）：为所有智能体设置默认模型与压缩策略，例如：

```json
"defaults": {
  "model": { "primary": "anthropic/claude-sonnet-4-5" },
  "compaction": { "mode": "safeguard" }
}
```

**agents.list**：每个智能体一项，必填 `id`、`workspace`、`agentDir`；`default: true` 表示未匹配到更具体 binding 时的回退智能体。用 CLI 逐个添加这 13 个智能体的步骤见 [§6 方法四：按 IT 片段用 openclaw agents add 添加智能体](#方法四按-it-片段用-openclaw-agents-add-添加智能体与官方一致)。IT 片段中 13 个智能体如下：

| id | name | 说明 |
|----|------|------|
| technical-director | 技术总监 | 默认入口，编排者，可委派子角色 |
| project-manager | 项目经理 | 项目管理、排期 |
| product-manager | 产品经理 | 需求与产品 |
| system-architect | 系统架构师 | 架构设计 |
| domain-expert | 领域专家 | 业务与领域知识 |
| ux-designer | UED设计师 | 体验设计 |
| ui-designer | UI设计师 | 界面设计 |
| backend-engineer | 后端工程师 | 后端开发 |
| database-engineer | 数据库工程师 | 数据库与存储 |
| frontend-engineer | 前端工程师 | 前端开发 |
| mobile-engineer | 移动开发工程师 | 移动端开发 |
| qa-engineer | 测试工程师 | 测试与质量 |
| ops-engineer | 运维工程师 | 部署与运维 |

**agent-to-agent**：IT 团队需编排者向子角色委派任务，故片段中设置 `tools.agentToAgent.enabled: true`，`allow` 列出 technical-director 及上述 12 个 id。详见 [OpenClaw Multi-Agent](https://docs.openclaw.ai/concepts/multi-agent)、[Channel routing](https://docs.openclaw.ai/channels/channel-routing)。

### 工作空间文件说明

| 文件 | 用途 | 修改建议 |
|------|------|----------|
| `AGENTS.md` | 智能体定义、工具、约束 | 修改角色与能力 |
| `SOUL.md` | 个性、语气、行为风格 | 修改回复风格 |
| `USER.md` | 用户偏好、上下文 | 修改用户设置 |
| `BOOTSTRAP.md` | 启动行为、初始化 | 修改初始化逻辑 |
| `HEARTBEAT.md` | 定时任务、周期行为 | 修改周期行为 |
| `TOOLS.md` | 工具使用说明 | 修改工具配置 |
| `IDENTITY.md` | 身份信息 | 可选 |

**语言约定**：智能体描述文件（`AGENTS.md`、`SOUL.md`、`IDENTITY.md`）以**英文**为准，便于 OpenClaw 系统提示词注入与模型遵循。可选在智能体目录下提供 `zh-CN/` 子目录，其中放置同名中文版（`AGENTS.md`、`SOUL.md`、`IDENTITY.md` 等），不参与注入，便于团队阅读及整目录拷贝到业务使用。参见 [OpenClaw System Prompt](https://docs.openclaw.ai/concepts/system-prompt)。

### 修改渠道绑定

在 `bindings` 中按 `channel`、`accountId`、`peer` 等配置；见 [§4 智能体组（单网关内多智能体与路由）](#4-智能体组单网关内多智能体与路由)。

### Channel 配置说明

**渠道（Channel）** 即消息来源（WhatsApp、Telegram、Discord 等）。OpenClaw 通过 `channels` 配置登录与白名单，通过 **bindings** 将「某渠道 / 某账号 / 某会话」路由到指定智能体。参考 [OpenClaw Channel routing](https://docs.openclaw.ai/channels/channel-routing)、[Configuration examples](https://docs.openclaw.ai/gateway/configuration-examples)。

**1. 配置渠道本身（channels）**

在 `openclaw.json` 的 `channels` 下按渠道类型配置账号与权限，例如多账号 WhatsApp、Telegram 白名单：

```json5
{
  "channels": {
    "whatsapp": {
      "allowFrom": ["+15555550123"],
      "accounts": {
        "personal": {},
        "biz": { "authDir": "~/.openclaw/credentials/whatsapp/biz" }
      }
    },
    "telegram": { "allowFrom": ["123456789"] },
    "discord": {}
  }
}
```

- **allowFrom**：允许触发机器人的用户/群 ID 白名单，不配则按渠道默认策略。
- **accounts**：多账号时每账号一个 key（如 personal、biz），对应一次 `openclaw channels login --channel whatsapp --account biz`。
- 会话存储位于状态目录下 `agents/<agentId>/sessions/`，见 [Channel routing - Session storage](https://docs.openclaw.ai/channels/channel-routing)。

**2. 将渠道路由到智能体（bindings）**

`bindings` 数组每一项为 `{ agentId, match }`。`match` 最具体优先；常见写法：

| 场景 | match 示例 | 说明 |
|------|------------|------|
| 某渠道全部进一个智能体 | `{ channel: "telegram" }` | IT 片段中 Telegram/Discord 均进 technical-director |
| 多账号分智能体 | `{ channel: "whatsapp", accountId: "personal" }` | 按登录账号路由 |
| 指定会话/群 | `{ channel: "whatsapp", peer: { kind: "direct", id: "+15551234567" } }` | 精确到会话 ID |

**3. 验证渠道与绑定**

```bash
openclaw channels status          # 渠道连接状态
openclaw channels status --probe  # 含探针（Telegram/Discord 等）
openclaw agents list --bindings  # 智能体列表及绑定关系
```

### 修改渠道配置

```json5
{
  channels: {
    whatsapp: {
      accounts: {
        biz: {
          authDir: "~/.custom-credentials/whatsapp/biz",  // 覆盖默认凭据路径
        }
      }
    }
  }
}
```

### 配置热重载与验证

- **校验与健康检查**：`openclaw doctor`（含配置与网关检查）。配置热重载由网关监听配置文件自动完成，或通过 `openclaw gateway restart` 重启生效。
- **查看智能体与绑定**：`openclaw agents list --bindings`；**渠道连通性**：`openclaw channels status --probe`。

### 删除智能体

```bash
openclaw agents delete work
# 非交互式需加 --force；会从配置中移除并清理工作区与状态
# openclaw agents delete work --force
```

### 备份与恢复

```bash
# 备份
tar czf work-backup.tar.gz ~/.openclaw/workspace-work
tar czf work-agent-backup.tar.gz ~/.openclaw/agents/work
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup

# 恢复：解压并恢复配置
tar xzf work-backup.tar.gz -C ~/
tar xzf work-agent-backup.tar.gz -C ~/
cp ~/.openclaw/openclaw.json.backup ~/.openclaw/openclaw.json
```

---

## 8. 完整配置示例

### WhatsApp 多账号（私人 + 工作）

```bash
openclaw channels login --channel whatsapp --account personal
openclaw channels login --channel whatsapp --account biz
```

```json5
{
  agents: {
    list: [
      { id: "home", default: true, name: "Home", workspace: "~/.openclaw/workspace-home", agentDir: "~/.openclaw/agents/home/agent" },
      { id: "work", name: "Work", workspace: "~/.openclaw/workspace-work", agentDir: "~/.openclaw/agents/work/agent" },
    ],
  },
  bindings: [
    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },
  ],
  channels: { whatsapp: { accounts: { personal: {}, biz: {} } } },
}
```

### 按渠道分流（WhatsApp 日常 + Telegram 深度）

```json5
{
  agents: {
    list: [
      { id: "chat", name: "Everyday", workspace: "~/.openclaw/workspace-chat", model: "anthropic/claude-sonnet-4-5" },
      { id: "opus", name: "Deep Work", workspace: "~/.openclaw/workspace-opus", model: "anthropic/claude-opus-4-6" },
    ],
  },
  bindings: [
    { agentId: "chat", match: { channel: "whatsapp" } },
    { agentId: "opus", match: { channel: "telegram" } },
  ],
}
```

---

## 9. 垂直领域示例：独立实例与智能体配置

本仓库除通用 `main/` 与 `it/`（技术团队 13 角色）外，还提供 **7 个垂直领域** 的智能体模板，对应目录与用途如下。

| 领域 | 本仓库路径 | 说明 |
|------|------------|------|
| education | `education/` | 教育助手、学科助手、评语、家校沟通 |
| wecom-kf | `wecom-kf/` | 企微客服：售前、售后、技术 |
| partner | `partner/` | 陪伴：主入口、提醒、故事、成长报告 |
| product | `product/` | 项目：PM、需求、架构、测试、文档、运维、商务、报表 |
| game | `game/` | 小游戏主持 |
| it | `it/` | 技术总监等 13 角色（软件开发团队）；目录编号 `1-`…`13-` 仅表示顺序，OpenClaw workspace 路径使用无编号名称 |
| scrm | `scrm/` | SCRM 运营：引流、获客、客资、建联、客服（复用 wecom-kf）、私域；6 阶段对应 partme-docs |
| web3 | `web3/` | 链上分析、DeFi、风险、组合；扩展见 partme-docs |

**it 软件开发团队**：技术总监为编排者（orchestrator），可经 OpenClaw **agent-to-agent**（sessions_spawn）委派 12 个子角色。使用时需启用 `tools.agentToAgent.enabled: true` 并将 technical-director 与全部子角色 id 列入 `allow`；建议使用本仓库 **config/openclaw-it-fragment.json** 片段，默认入口为 `technical-director`。

**两种用法**：① **单网关多 Agent** — 同一 OpenClaw 实例内，用 [§4 智能体组](#4-智能体组单网关内多智能体与路由) 的 bindings 按 channel/accountId 等路由到不同领域 Agent；② **多网关多实例** — 每领域独立 `--profile`，配置/端口/工作区完全隔离，见 [§3 多网关](#3-多网关同一主机多组智能体)。

**创建独立实例（多网关）**：使用 `openclaw --profile <领域名> setup` 初始化，再 `openclaw --profile <领域名> gateway --port <端口>` 启动（端口与主实例错开 ≥20，如 education 用 18809）。`OPENCLAW_CONFIG_PATH` 与 `OPENCLAW_STATE_DIR` 按 profile 隔离，详见 §3。

**配置智能体**：将本仓库对应目录复制或链接到 OpenClaw 工作区（如 `~/.openclaw/workspace-education/edu-assistant`），在 `openclaw.json` 的 `agents.list` 中配置 `id`、`workspace`、`agentDir`，并在 `bindings` 中按 channel 或业务规则路由。详见 [§6 创建智能体](#6-创建智能体)、[§7 配置智能体](#7-配置智能体)。

**汇总表（示例）**

| 领域 | profile | 建议端口 | 代表 agentId | 工作区路径示例 |
|------|---------|----------|--------------|----------------|
| education | education | 18809 | edu-assistant | `~/.openclaw/workspace-education/edu-assistant` |
| wecom-kf | wecom-kf | 18819 | presale | `~/.openclaw/workspace-wecom-kf/presale` |
| partner | partner | 18839 | companion | `~/.openclaw/workspace-partner/companion` |
| product | product | 18849 | pm-assistant | `~/.openclaw/workspace-product/pm-assistant` |
| game | game | 18859 | game-host | `~/.openclaw/workspace-game/game-host` |
| it | it | 18829 | technical-director | `~/.openclaw/workspace-it/technical-director` |
| scrm | scrm | 18819 | scrm-orchestrator | `~/.openclaw-scrm/workspace-scrm/lead-gen`（或 scrm-orchestrator） |
| web3 | web3 | 18869 | chain-analyst | `~/.openclaw-web3/workspace-web3/chain-analyst` |

it 工作区路径使用**无编号**名称（与 agent id 一致）；部署时可将仓库 `it/1-technical-director` 复制或链接到 `~/.openclaw/workspace-it/technical-director`，其余角色同理（如 `it/2-project-manager` → `workspace-it/project-manager`）。

**OpenClaw 官方文档与运维**：完整文档索引 [docs.openclaw.ai/llms.txt](https://docs.openclaw.ai/llms.txt)；若访问受限可改用 [GitHub 镜像](https://github.com/openclaw/openclaw/tree/main/docs)。多 profile 时带 `--profile <name>` 执行 `openclaw status`、`openclaw doctor`、`openclaw health --json` 等。记忆与技能见 [Memory](https://docs.openclaw.ai/concepts/memory)、[Skills](https://docs.openclaw.ai/tools/skills)；故障排除见 [Updating / If you're stuck](https://docs.openclaw.ai/install/updating)、[Discord](https://discord.gg/clawd)。

**深入阅读**：各领域技术方案与智能体职责见仓库 `partme-docs/OpenClaw-垂直领域应用分析` 下对应文档。

### 三组并存启动与验证（IT 研发 + SCRM 运营 + Web3）

同一主机跑三组智能体时：**默认 Gateway** = IT 研发（合并 openclaw-it-fragment.json），**profile scrm** = SCRM 运营，**profile web3** = Web3 团队。每组独立配置、状态目录与端口，端口间距 ≥20。

**启动示例**：

```bash
# 1）IT 研发（默认，端口 18789）
openclaw onboard
openclaw gateway --port 18789
# 或安装为服务：openclaw gateway install && openclaw gateway start

# 2）SCRM 运营（profile scrm，端口 18819）
openclaw --profile scrm setup
openclaw --profile scrm gateway --port 18819

# 3）Web3（profile web3，端口 18869）
openclaw --profile web3 setup
openclaw --profile web3 gateway --port 18869
```

**验证**：

```bash
# 各 profile 状态与诊断
openclaw status
openclaw --profile scrm status
openclaw --profile web3 status

# 各实例内智能体与绑定
openclaw agents list --bindings
openclaw --profile scrm agents list --bindings
openclaw --profile web3 agents list --bindings

# Gateway 健康（需对应实例已启动）
openclaw health --json
openclaw --profile scrm health --json
openclaw --profile web3 health --json
```

合并配置片段前，将各片段中的路径占位符替换为实际路径（SCRM 使用 `~/.openclaw-scrm`，Web3 使用 `~/.openclaw-web3`）；详见 [config/README.md](config/README.md)。

---

## 10. 路径与部署

### 路径速查表

| 路径 | 环境变量 | 默认值 | 说明 |
|------|----------|--------|------|
| 配置文件 | `OPENCLAW_CONFIG_PATH` | `~/.openclaw/openclaw.json` | 主配置 |
| 状态目录 | `OPENCLAW_STATE_DIR` | `~/.openclaw` | 所有状态数据 |
| 工作空间 | `OPENCLAW_WORKSPACE` / `OPENCLAW_PROFILE` | `~/.openclaw/workspace` | 默认工作空间 |
| 智能体目录 | - | `~/.openclaw/agents/<agentId>/agent` | 智能体状态 |
| 会话存储 | - | `~/.openclaw/agents/<agentId>/sessions` | 聊天历史 |
| 全局技能 | - | `~/.openclaw/skills` | 共享技能目录 |

### 目录结构

```
~/.openclaw/
├── openclaw.json
├── workspace/                 # 默认工作空间 (main)
│   ├── AGENTS.md, SOUL.md, USER.md, BOOTSTRAP.md, HEARTBEAT.md
│   └── skills/
├── workspace-<agentId>/
├── agents/
│   ├── main/
│   │   ├── agent/            # auth-profiles.json, config.json
│   │   └── sessions/
│   └── <agentId>/
├── credentials/               # 渠道凭据
└── skills/                    # 全局共享技能
```

### 环境变量部署

```bash
# 开发
export OPENCLAW_CONFIG_PATH="$HOME/.openclaw/openclaw.dev.json"
export OPENCLAW_STATE_DIR="$HOME/.openclaw-dev"

# 生产
export OPENCLAW_CONFIG_PATH="/etc/openclaw/openclaw.json"
export OPENCLAW_STATE_DIR="/var/lib/openclaw"
```

### systemd（Linux）

```ini
# /etc/systemd/system/openclaw.service
[Unit]
Description=OpenClaw Gateway
After=network.target
[Service]
Type=simple
User=your-user
Environment="OPENCLAW_CONFIG_PATH=/home/your-user/.openclaw/openclaw.json"
ExecStart=/usr/local/bin/openclaw gateway
Restart=on-failure
RestartSec=5
[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable openclaw && sudo systemctl start openclaw
sudo systemctl status openclaw
```

### Docker

```bash
docker pull openclaw/openclaw:latest
docker run -d --name openclaw \
  -v ~/.openclaw:/root/.openclaw \
  -e ANTHROPIC_API_KEY=your-api-key \
  -p 8080:8080 \
  openclaw/openclaw:latest
```

### 权限与备份

```bash
chmod 700 ~/.openclaw
chmod 600 ~/.openclaw/openclaw.json
chmod 600 ~/.openclaw/agents/*/agent/auth-profiles.json
```

定时备份示例：备份 `openclaw.json`、`workspace*`、`agents` 到带日期的 tar.gz，并保留最近 N 份。

---

## 11. 模板与智能体对照

### 智能体工作空间文件结构

```
<agent-name>/
├── AGENTS.md      # 智能体定义、工具、约束
├── SOUL.md        # 个性、语气、行为风格
├── USER.md        # 用户偏好、上下文
├── BOOTSTRAP.md   # 启动行为、初始化
├── HEARTBEAT.md   # 定时任务、周期行为
├── IDENTITY.md    # 身份信息（可选）
└── TOOLS.md       # 工具使用说明（可选）
```

垂直领域模板位于本仓库 `education/`、`wecom-kf/`、`partner/`、`product/`、`game/`、`web3/`，it 模板位于 `it/`；见 [§9 垂直领域示例](#9-垂直领域示例独立实例与智能体配置)。

**共享项目目录（本机路径）**：本仓库 `it/` 下的 AGENTS.md 为**通用模板**，不包含本机专属的「共享项目目录」绝对路径。若需指定团队代码库路径（如 `/path/to/workspace-partme-ai`），应在**各智能体实际工作空间**（`~/.openclaw/workspace-<agentId>/AGENTS.md`）中单独添加或维护「Workspace & project directory」小节，便于不同机器使用不同路径。

### 智能体类型示例（以官方路径为准）

以下为**概念示例**，路径均采用 [官方约定](https://docs.openclaw.ai/concepts/multi-agent#paths-quick-map)（`~/.openclaw/workspace-<agentId>`、`~/.openclaw/agents/<agentId>/agent`）：

| 工作空间路径（示例） | 用途说明 |
|----------------------|----------|
| `~/.openclaw/workspace` | 默认主智能体 (main)，通用对话 |
| `~/.openclaw/workspace-work` | 工作场景 |
| `~/.openclaw/workspace-personal` | 个人场景 |
| `~/.openclaw/workspace-coding` | 编程辅助 |
| `~/.openclaw/workspace-social` | 社交/内容 |

每个智能体需独立 `agentDir`（如 `~/.openclaw/agents/work/agent`），不可共用。

### 使用已有目录创建智能体

```bash
# 若你已有工作空间目录（如从某处复制或自己创建）
mkdir -p ~/.openclaw/workspace-coding
# 放入 AGENTS.md、SOUL.md、USER.md 等（参见上文「工作空间文件结构」）

# 在 openclaw.json 的 agents.list 中增加一项，例如：
# id: "coding", workspace: "~/.openclaw/workspace-coding", agentDir: "~/.openclaw/agents/coding/agent"
```

---

## 12. Multi-Agent 约束说明

### 隔离性

| 资源 | 隔离级别 | 说明 |
|------|----------|------|
| 工作空间 | ✅ 完全隔离 | 每个智能体独立目录 |
| 认证配置 | ✅ 完全隔离 | `auth-profiles.json` 按智能体 |
| 会话存储 | ✅ 完全隔离 | 会话键含 `agentId` |
| 模型配置 | ✅ 完全隔离 | 每智能体可独立配置 |
| 全局技能 | ⚠️ 只读共享 | `~/.openclaw/skills` 所有智能体可读 |
| 渠道连接 | ⚠️ 共享连接 | 连接池共享，消息路由隔离 |

### 重要约束

1. **禁止共享 agentDir**  
   多个智能体使用同一 `agentDir` 会导致认证冲突、会话混乱、配置覆盖。每个智能体必须使用独立的 `agentDir`（如 `~/.openclaw/agents/<id>/agent`）。

2. **认证不自动共享**  
   主智能体的凭据不会自动给其他智能体；需单独登录或手动复制 `auth-profiles.json`。

3. **DM 访问控制是渠道全局的**  
   配对/白名单在 `channels.<channel>` 下配置，对整个渠道生效，不是按智能体。

4. **智能体间通信需显式启用**  
   ```json5
   {
     tools: {
       agentToAgent: {
         enabled: false,
         allow: ["home", "work"],
       },
     },
   }
   ```

### 性能与限制

| 指标 | 建议值 | 说明 |
|------|--------|------|
| 智能体数量 | 5–10 个 | 单网关实例 |
| 并发会话 | 每智能体 10–20 | 视模型与硬件而定 |
| 内存占用 | 每智能体约 100MB | 工作空间 + 会话缓存 |
| 启动时间 | 每智能体约 +2–5s | 视工作空间大小而定 |

### 安全与最佳实践

- 工作空间为默认 cwd，但非硬沙盒；绝对路径可访问主机其他位置；如需严格隔离可启用 `sandbox`。
- 敏感文件权限：`chmod 600` 用于 `openclaw.json` 和 `auth-profiles.json`。
- 配置可纳入版本控制，但需将 `agents/*/agent/auth-profiles.json` 和 `credentials/**` 加入 `.gitignore`。

---

## 13. 故障排查

### 常见问题

| 现象 | 处理 |
|------|------|
| 路由错误 | `openclaw agents list --bindings` 检查绑定；`openclaw gateway --verbose` 看路由日志 |
| 认证失败 | 检查 `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` 是否存在；`openclaw channels login` 重新登录 |
| 会话混乱 | `rm -rf ~/.openclaw/agents/<agentId>/sessions/*` 后重启网关 |
| 配置不生效 | `openclaw doctor` 检查；`openclaw gateway restart` 重启网关使配置生效 |

### 调试命令

```bash
openclaw gateway --verbose
openclaw channels status --probe
openclaw agents list --bindings
openclaw doctor
```

### 安装与启动问题

- **安装失败**：确认 Node.js ≥ 18（`node --version`）、npm 权限、必要时 `npm cache clean --force`。
- **启动失败**：检查端口占用（如 `lsof -i :8080`）、配置校验、详细日志。

### 更新与卸载

```bash
# 更新
curl -fsSL https://openclaw.ai/install.sh | bash
# 或 npm update -g openclaw / brew upgrade openclaw

# 卸载
curl -fsSL https://openclaw.ai/uninstall.sh | bash
# 或 npm uninstall -g openclaw；谨慎：rm -rf ~/.openclaw
```

---

## 14. 相关链接

- **[OpenClaw 使用系列](docs/README.md)** — 场景化实战（Claw + Obsidian 外脑等）
- [OpenClaw 官方文档](https://docs.openclaw.ai)
- [CLI Reference](https://docs.openclaw.ai/cli) — 命令与全局选项（`--profile`、`--dev`、`gateway`、`agents`、`channels` 等）
- [Multi-Agent Routing](https://docs.openclaw.ai/concepts/multi-agent)
- [Multiple Gateways（同一主机多网关）](https://docs.openclaw.ai/gateway/multiple-gateways) — 官方多网关说明（本仓库镜像：`research/claw-ecosystem/openclaw/docs/gateway/multiple-gateways.md`、`docs/zh-CN/gateway/multiple-gateways.md`）
- [渠道配置](https://docs.openclaw.ai/channels)
- [文档索引 llms.txt](https://docs.openclaw.ai/llms.txt)

---

**最后更新**: 2026-02-20

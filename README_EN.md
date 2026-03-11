# OpenClaw Agents

OpenClaw multi-agent configuration guide and examples, following the [OpenClaw Multi-Agent](https://docs.openclaw.ai/concepts/multi-agent) docs: run multiple isolated agents (separate workspace, agentDir, sessions) in one gateway and route inbound messages via bindings.

> **Official docs**  
> - [Multi-Agent Routing](https://docs.openclaw.ai/concepts/multi-agent) (paths, single/multi-agent, Agent helper, routing rules)

---

## Two things to know

### How to quickly add agent config to OpenClaw

1. **Ensure OpenClaw is installed** (see [§1 System Requirements & Installation](#1-system-requirements--installation) if not).
2. **Prepare config**  
   If you use a **config fragment** from this repo: open the fragment in an editor and replace any placeholder path (e.g. `<REPO_ROOT>`) with your **absolute path** (e.g. `~/.openclaw` or `/home/you/openclaw-agents`). For the **it software dev team**, use `config/openclaw-it-fragment.json`: workspace paths are unnumbered (e.g. `~/.openclaw/workspace-it/technical-director`), matching agent id; set `tools.agentToAgent.enabled: true` and list technical-director plus all 12 sub-role ids in `allow`; with multiple profiles, the it instance needs its own `OPENCLAW_CONFIG_PATH`, `OPENCLAW_STATE_DIR`, and port (§3).
3. **Merge and restart**  
   Merge the fragment’s `agents`, `bindings`, and `tools.agentToAgent` into `~/.openclaw/openclaw.json` (merge `agents.list` with existing list if keys already exist). Run `openclaw gateway restart` (or `openclaw gateway`).
4. **Verify**  
   `openclaw agents list --bindings`, `openclaw channels status --probe`.

No local or product-specific paths are required; use paths that match the [official path map](https://docs.openclaw.ai/concepts/multi-agent#paths-quick-map) (Config, State dir, Workspace, Agent dir, Sessions).

### How to add a new agent

- **Option 1 (recommended, matches official docs)**  
  Run `openclaw agents add <agentId>` (e.g. `openclaw agents add work`). The wizard creates a dedicated workspace (e.g. `~/.openclaw/workspace-work`), `agentDir` (e.g. `~/.openclaw/agents/work/agent`), and session store. In `~/.openclaw/openclaw.json` set `workspace` (absolute path) and `agentDir` (must not be shared with other agents), and add `bindings` as needed for routing.
- **Option 2**  
  Manually create `~/.openclaw/workspace-<agentId>` with SOUL.md, AGENTS.md, optional USER.md, etc.; create `~/.openclaw/agents/<agentId>/agent` and `sessions`; add an entry to `agents.list` with `id`, `workspace`, `agentDir`.
- For more detail and fields, see [§6 Creating agents](#6-creating-agents) and [§7 Configuring agents](#7-configuring-agents).

---

## Contents

1. [System Requirements & Installation](#1-system-requirements--installation)
2. [Quick Start & First-Time Setup](#2-quick-start--first-time-setup)
3. [Multiple Gateways (same host, multiple agent groups)](#3-multiple-gateways-same-host-multiple-agent-groups)
4. [Agent groups (multi-agent and routing in one gateway)](#4-agent-groups-multi-agent-and-routing-in-one-gateway)
5. [What Is "One Agent"](#5-what-is-one-agent)
6. [Creating Agents](#6-creating-agents)
7. [Configuring Agents](#7-configuring-agents)
8. [Full Configuration Examples](#8-full-configuration-examples)
9. [Vertical domains: independent instances and agent configuration](#9-vertical-domains-independent-instances-and-agent-configuration)
10. [Paths & Deployment](#10-paths--deployment)
11. [Templates & Agent Mapping](#11-templates--agent-mapping)
12. [Multi-Agent Constraints](#12-multi-agent-constraints)
13. [Troubleshooting](#13-troubleshooting)
14. [Links](#14-links)

---

## 1. System Requirements & Installation

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | macOS 12+ / Linux (Ubuntu 20.04+) / Windows 11 (WSL2) | macOS 14+ / Ubuntu 22.04+ |
| **Node.js** | 18.0.0+ | 20.0.0+ LTS |
| **Memory** | 4GB RAM | 8GB+ RAM |
| **Disk** | 2GB free | 10GB+ SSD |
| **Network** | Stable internet | - |

### Installation

**Option 1: Official install script (recommended)**

```bash
# macOS / Linux
curl -fsSL https://openclaw.ai/install.sh | bash
# or
wget -qO- https://openclaw.ai/install.sh | bash

source ~/.bashrc   # or ~/.zshrc
```

**Option 2: npm**

```bash
npm install -g openclaw
# or
npx openclaw@latest
```

**Option 3: Homebrew (macOS/Linux)**

```bash
brew tap openclaw/tap
brew install openclaw
brew upgrade openclaw
```

**Option 4: From source**

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw && npm install && npm run build && npm link
```

### Verify installation

```bash
openclaw --version
openclaw --help
openclaw doctor
```

---

## 2. Quick Start & First-Time Setup

### First run

```bash
# Initialize config and workspace
openclaw setup
# Or interactive wizard (gateway, workspace, skills, channels)
openclaw onboard
```

The official CLI uses `setup` / `onboard` (there is no `init` command). The wizard guides you through: config directory, default model, API keys, channel login (optional).

### Manual minimal config

```bash
mkdir -p ~/.openclaw
mkdir -p ~/.openclaw/workspace ~/.openclaw/agents/main/agent
```

Minimal `~/.openclaw/openclaw.json`:

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

### API keys

- **Environment**: Set `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `DEEPSEEK_API_KEY`, etc. in `~/.bashrc` or `~/.zshrc`, then `source` it.
- **Config file**: Put profiles (name + apiKey) in `~/.openclaw/agents/main/agent/auth-profiles.json` and `chmod 600` it.

### Start gateway

```bash
openclaw gateway              # foreground
openclaw gateway --port 8080  # custom port
# Background: install as service then start (openclaw gateway install && openclaw gateway start), or nohup openclaw gateway &
```

---

## 3. Multiple Gateways (same host, multiple agent groups)

### Why run multiple gateways

A single OpenClaw Gateway instance can handle **multiple messaging connections** and **multiple agents** (routed via bindings). When you need **multiple isolated agent groups on the same host** (e.g. main vs rescue, or different teams/environments), run **multiple Gateway instances** (“multiple gateways”). Typical cases:

- **Isolation and redundancy**: one group for the main bot, one for a rescue bot; use the rescue instance to debug or change config when the main one is down.
- **Multiple environments/teams**: different profiles with different config, workspace, and ports on the same machine.
- **Resource and port isolation**: each group uses its own config, state dir, workspace, and ports to avoid config races and port conflicts.

The following summarizes the official docs [Multiple Gateways (same host)](https://docs.openclaw.ai/gateway/multiple-gateways) .

### Isolation checklist (required)

Each gateway instance must have its own:

- **`OPENCLAW_CONFIG_PATH`** — config file per instance
- **`OPENCLAW_STATE_DIR`** — sessions, credentials, caches per instance
- **`agents.defaults.workspace`** — workspace root per instance (if used)
- **`gateway.port` (or `--port`)** — unique port per instance
- **Derived ports (browser/canvas/CDP)** — must not overlap

If any of these are shared, you will get config races and port conflicts.

### Recommended: profiles (`--profile`)

`--profile` auto-scopes `OPENCLAW_STATE_DIR` and `OPENCLAW_CONFIG_PATH` and suffixes service names.

```bash
# main
openclaw --profile main setup
openclaw --profile main gateway --port 18789

# rescue (or second group)
openclaw --profile rescue setup
openclaw --profile rescue gateway --port 19001
```

Install per-profile services:

```bash
openclaw --profile main gateway install
openclaw --profile rescue gateway install
```

### Rescue-bot guide

Run a second Gateway on the same host with its own profile/config, state dir, workspace, and base port (plus derived ports). That keeps the rescue bot isolated so it can debug or apply config when the primary is down.

**Port spacing**: leave at least **20** ports between base ports so derived browser/canvas/CDP ports never collide (e.g. 18789 and 19001, or 18789 and 19789).

```bash
# Main (default, no --profile)
openclaw onboard
openclaw gateway install

# Rescue (isolated profile + port)
openclaw --profile rescue onboard
# Workspace name is postfixed with -rescue by default; port should be at least 18789+20, e.g. 19789
openclaw --profile rescue gateway install
```

### Port mapping (derived)

- **Base port** = `gateway.port` (or `OPENCLAW_GATEWAY_PORT` / `--port`)
- Browser control service port = base + 2 (loopback only)
- Canvas is served on the Gateway HTTP server (same port); in some setups `canvasHost.port = base + 4`
- Browser CDP ports auto-allocate from `browser.controlPort + 9 .. + 108`

If you override any of these in config or env, keep them unique per instance.

### Browser/CDP notes (common footgun)

- Do **not** pin `browser.cdpUrl` to the same values on multiple instances.
- Each instance needs its own browser control port and CDP range (derived from its gateway port).
- For explicit CDP ports, set `browser.profiles.<name>.cdpPort` per instance.
- Remote Chrome: use `browser.profiles.<name>.cdpUrl` (per profile, per instance).

### Manual env example

```bash
OPENCLAW_CONFIG_PATH=~/.openclaw/main.json \
OPENCLAW_STATE_DIR=~/.openclaw-main \
openclaw gateway --port 18789

OPENCLAW_CONFIG_PATH=~/.openclaw/rescue.json \
OPENCLAW_STATE_DIR=~/.openclaw-rescue \
openclaw gateway --port 19001
```

### Quick checks

```bash
openclaw --profile main status
openclaw --profile rescue status
openclaw --profile rescue browser status
```

---

## 4. Agent groups (multi-agent and routing in one gateway)

An **agent group** is the set of agents (`agents.list`) in **one Gateway instance**, with **bindings** routing inbound messages to different agents. This section covers multi-agent and routing rules inside a single gateway.

1. `peer` match (exact DM/group/channel ID)
2. `parentPeer` match (thread inheritance)
3. `guildId + roles` (Discord roles)
4. `guildId` (Discord)
5. `teamId` (Slack)
6. Channel `accountId` match
7. Channel-level match (`accountId: "*"`)
8. Fallback to default agent (`default: true` or first in list)

### Binding examples

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

### Match fields

| Field | Description | Example |
|-------|-------------|---------|
| `channel` | Channel type | `whatsapp`, `telegram`, `discord` |
| `accountId` | Channel account ID | `personal`, `biz`, `default` |
| `peer.kind` | Conversation type | `direct`, `group` |
| `peer.id` | Conversation ID | Phone number, group ID, channel ID |
| `guildId` | Discord server ID | `"123456789012345678"` |

---

## 5. What Is "One Agent"

Each **agent** is an isolated "brain" with its own:

| Component | Description | Path |
|------------|-------------|------|
| **Workspace** | Files, AGENTS.md/SOUL.md/USER.md, notes, persona rules | `~/.openclaw/workspace-<agentId>` or configured path |
| **agentDir** | Auth, model registry, per-agent config | `~/.openclaw/agents/<agentId>/agent` |
| **Session store** | Chat history and routing state | `~/.openclaw/agents/<agentId>/sessions` |

**Single-agent mode (default)**: With no multi-agent config, `agentId` defaults to `main`, workspace to `~/.openclaw/workspace`, state to `~/.openclaw/agents/main/agent`.

---

## 6. Creating Agents

### Method 1: Wizard (recommended)

```bash
openclaw agents add
openclaw agents add work
openclaw agents add personal
```

The wizard guides: name, workspace path, state directory path, channel bindings (optional).

### Method 2: Manual

```bash
mkdir -p ~/.openclaw/workspace-work
cd ~/.openclaw/workspace-work
touch AGENTS.md SOUL.md USER.md

mkdir -p ~/.openclaw/agents/work/agent
mkdir -p ~/.openclaw/agents/work/sessions

vim ~/.openclaw/openclaw.json
```

Add to `agents.list`:

```json5
{
  id: "work",
  name: "Work",
  workspace: "~/.openclaw/workspace-work",
  agentDir: "~/.openclaw/agents/work/agent",
}
```

### Method 3: Copy existing agent

```bash
cp -r ~/.openclaw/workspace ~/.openclaw/workspace-copy
cp -r ~/.openclaw/agents/main ~/.openclaw/agents/copy
# Add a new list entry for "copy" in openclaw.json and set id/workspace/agentDir
```

### Method 4: Add IT team agents via openclaw agents add (matches official docs)

This follows the [OpenClaw Multi-Agent](https://docs.openclaw.ai/concepts/multi-agent) **Agent helper** and **Quick start**: use `openclaw agents add <agentId>` for each role to create workspace, agentDir, and session store, then merge this repo’s config fragment for bindings and agent-to-agent.

**1. Add all 13 IT agents with the wizard**

The fragment’s `agentId` values are valid CLI arguments:

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

**Game team roles (game/)** — Terminology:

- **Game Master** （游戏主持人）：Facilitator and orchestrator; runs sessions, holds vision, coordinates Game Designer and Game Architect.
- **Game Designer** （游戏策划）：Industry-standard role for core design — gameplay, rules, systems, levels, narrative. Widely used in hiring and international teams.
- **Game Developer**（游戏开发）：此处指**程序开发**角色（写代码的程序员），而非泛指策划、美术、程序等所有岗位。In this doc, “game development” means programming/coding (程序开发), not the entire game team.
- **Game Architect** （游戏架构师）：Senior role for overall game architecture and system design; technical and top-level.

**Add all 4 Game agents with the wizard**

Fragment `agentId` values are valid CLI arguments:

```bash
openclaw agents add game-master
openclaw agents add game-designer
openclaw agents add game-architect
openclaw agents add game-developer
```

Merge `agents`, `bindings`, and `tools.agentToAgent` from `config/openclaw-game-fragment.json` into `~/.openclaw/openclaw.json`. To use a shared workspace, set `workspace` to e.g. `~/.openclaw/workspace-game/<agentId>`. Copy or link this repo’s `game/` role templates:

```bash
cp -r /path/to/openclaw-agents/game/1-game-master/*    ~/.openclaw/workspace-game/game-master/
cp -r /path/to/openclaw-agents/game/2-game-designer/*  ~/.openclaw/workspace-game/game-designer/
cp -r /path/to/openclaw-agents/game/3-game-architect/* ~/.openclaw/workspace-game/game-architect/
cp -r /path/to/openclaw-agents/game/4-game-developer/* ~/.openclaw/workspace-game/game-developer/
```

---

The wizard creates `~/.openclaw/workspace-<agentId>`, `~/.openclaw/agents/<agentId>/agent`, and sessions. To use a shared `workspace-it` dir, enter `~/.openclaw/workspace-it/<agentId>` in the wizard or set `workspace` in config to match the fragment.

**2. Merge fragment into openclaw.json**

Merge `agents` (including `defaults` and `list`), `bindings`, and `tools.agentToAgent` from `config/openclaw-it-fragment.json` into `~/.openclaw/openclaw.json`. If you already have `agents.list`, merge the fragment list (by id) and keep the fragment’s `bindings` and `tools.agentToAgent` so Telegram/Discord route to technical-director and the orchestrator can delegate to the 12 roles.

**3. Optional: use this repo’s it/ workspace templates**

The repo’s `it/` directory has AGENTS.md, SOUL.md, etc. per role. Copy or link into your workspace paths, e.g.:

```bash
cp -r /path/to/openclaw-agents/it/technical-director/* ~/.openclaw/workspace-it/technical-director/
```

**4. Restart and verify**

```bash
openclaw gateway restart
openclaw agents list --bindings
openclaw channels status --probe
```

---

## 7. Configuring Agents

### Config file location

Main config: `~/.openclaw/openclaw.json` (JSON5). Override with `OPENCLAW_CONFIG_PATH`.

### Agent fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for routing |
| `name` | string | No | Display name |
| `default` | boolean | No | Default agent for fallback routing |
| `workspace` | string | Yes | **Absolute** workspace path |
| `agentDir` | string | Yes | State directory; **must not** be shared across agents |
| `model` | string | No | Default model |

### Agent list (openclaw-it-fragment example)

The repo’s `config/openclaw-it-fragment.json` defines a **software dev team**: one orchestrator plus 12 roles, all on the same gateway. Inbound traffic is routed to the default agent via **bindings**, then **agent-to-agent** is used to delegate to specific roles.

**agents.defaults** (optional): shared default model and compaction for all agents, e.g.:

```json
"defaults": {
  "model": { "primary": "anthropic/claude-sonnet-4-5" },
  "compaction": { "mode": "safeguard" }
}
```

**agents.list**: one entry per agent with required `id`, `workspace`, `agentDir`. The entry with `default: true` is the fallback when no binding matches. To add these 13 agents via CLI, see [§6 Method 4: Add IT team agents via openclaw agents add](#method-4-add-it-team-agents-via-openclaw-agents-add-matches-official-docs). The IT fragment defines 13 agents:

| id | name | Role |
|----|------|------|
| technical-director | Technical Director | Default entry; orchestrator; delegates to roles below |
| project-manager | Project Manager | Project and schedule |
| product-manager | Product Manager | Requirements and product |
| system-architect | System Architect | Architecture |
| domain-expert | Domain Expert | Business/domain |
| ux-designer | UX Designer | Experience design |
| ui-designer | UI Designer | Interface design |
| backend-engineer | Backend Engineer | Backend dev |
| database-engineer | Database Engineer | DB and storage |
| frontend-engineer | Frontend Engineer | Frontend dev |
| mobile-engineer | Mobile Engineer | Mobile dev |
| qa-engineer | QA Engineer | Test and quality |
| ops-engineer | Ops Engineer | Deploy and ops |

**agent-to-agent**: The IT team needs the orchestrator to delegate to these roles, so the fragment sets `tools.agentToAgent.enabled: true` and `allow` lists technical-director plus the 12 ids above. See [OpenClaw Multi-Agent](https://docs.openclaw.ai/concepts/multi-agent) and [Channel routing](https://docs.openclaw.ai/channels/channel-routing).

### Workspace files

| File | Purpose | When to edit |
|------|---------|--------------|
| `AGENTS.md` | Role, tools, constraints | Change role and capabilities |
| `SOUL.md` | Personality, tone, style | Change reply style |
| `USER.md` | User preferences, context | Change user settings |
| `BOOTSTRAP.md` | Startup behavior | Change init logic |
| `HEARTBEAT.md` | Periodic tasks | Change periodic behavior |
| `TOOLS.md` | Tool usage | Change tool config |
| `IDENTITY.md` | Identity | Optional |

**Language**: Agent description files (`AGENTS.md`, `SOUL.md`, `IDENTITY.md`) are in **English** for OpenClaw system prompt injection. Optional Chinese versions live in a `zh-CN/` subdirectory with the same filenames (`AGENTS.md`, `SOUL.md`, `IDENTITY.md`, etc.) for team reading and for copying the whole directory into business workspaces. See [OpenClaw System Prompt](https://docs.openclaw.ai/concepts/system-prompt).

### Changing channel bindings

Configure `bindings` by `channel`, `accountId`, `peer`, etc.; see [§4 Agent groups](#4-agent-groups-multi-agent-and-routing-in-one-gateway).

### Channel configuration

**Channels** are message sources (WhatsApp, Telegram, Discord, etc.). OpenClaw uses `channels` for login and allowlists, and **bindings** to route “which channel / account / conversation” to which agent. See [OpenClaw Channel routing](https://docs.openclaw.ai/channels/channel-routing) and [Configuration examples](https://docs.openclaw.ai/gateway/configuration-examples).

**1. Configuring channels**

Under `channels` in `openclaw.json`, configure per-channel accounts and allowlists, e.g. multi-account WhatsApp or Telegram allowlist:

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

- **allowFrom**: Allowlist of user/group IDs that can trigger the bot; omit for channel default.
- **accounts**: For multiple accounts, one key per account (e.g. personal, biz); each corresponds to a `openclaw channels login --channel whatsapp --account biz`.
- Session store lives under the state dir at `agents/<agentId>/sessions/`; see [Channel routing - Session storage](https://docs.openclaw.ai/channels/channel-routing).

**2. Routing channels to agents (bindings)**

Each entry in `bindings` is `{ agentId, match }`. Most specific match wins. Examples:

| Scenario | match example | Notes |
|----------|----------------|-------|
| Whole channel to one agent | `{ channel: "telegram" }` | IT fragment: Telegram and Discord both go to technical-director |
| Per-account routing | `{ channel: "whatsapp", accountId: "personal" }` | Route by logged-in account |
| Specific conversation/group | `{ channel: "whatsapp", peer: { kind: "direct", id: "+15551234567" } }` | Exact peer ID |

**3. Verifying channels and bindings**

```bash
openclaw channels status          # Channel connection status
openclaw channels status --probe  # With probe (Telegram, Discord, etc.)
openclaw agents list --bindings  # Agent list and bindings
```

### Changing channel config

```json5
{
  channels: {
    whatsapp: {
      accounts: {
        biz: {
          authDir: "~/.custom-credentials/whatsapp/biz",
        }
      }
    }
  }
}
```

### Hot reload and validation

- **Validation and health**: `openclaw doctor` (includes config and gateway checks). Config hot reload is done by the gateway watching the config file, or run `openclaw gateway restart` to apply changes.
- **Agents and bindings**: `openclaw agents list --bindings`; **channel connectivity**: `openclaw channels status --probe`.

### Removing an agent

```bash
openclaw agents delete work
# Non-interactive: add --force; removes from config and prunes workspace/state
# openclaw agents delete work --force
```

### Backup and restore

```bash
# Backup
tar czf work-backup.tar.gz ~/.openclaw/workspace-work
tar czf work-agent-backup.tar.gz ~/.openclaw/agents/work
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup

# Restore: extract and restore config
tar xzf work-backup.tar.gz -C ~/
tar xzf work-agent-backup.tar.gz -C ~/
cp ~/.openclaw/openclaw.json.backup ~/.openclaw/openclaw.json
```

---

## 8. Full Configuration Examples

### WhatsApp multi-account (personal + work)

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

### Route by channel (WhatsApp daily + Telegram deep work)

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

## 9. Vertical domains: independent instances and agent configuration

Besides the generic `main/` and `it/` (13 technical roles), this repo provides templates for **7 vertical domains**. Directory mapping:

| Domain | Repo path | Description |
|--------|-----------|-------------|
| education | `education/` | Edu assistant, subject helpers, comments, parent liaison |
| wecom-kf | `wecom-kf/` | WeCom support: presale, aftersale, tech |
| partner | `partner/` | Companion: main entry, reminder, storyteller, growth reporter |
| product | `product/` | Project: PM, requirements, architecture, test, docs, DevOps, business, reports |
| game | `game/` | Game host |
| it | `it/` | 13 roles (software dev team); directory numbers `1-`…`13-` are for ordering only—OpenClaw workspace paths use unnumbered names |
| web3 | `web3/` | Chain analyst, DeFi, risk, portfolio; extensions see partme-docs |

**it software dev team**: The Technical Director is the orchestrator and can delegate to 12 sub-roles via OpenClaw **agent-to-agent** (sessions_spawn). Enable `tools.agentToAgent.enabled: true` and list technical-director and all sub-role ids in `allow`. Use **config/openclaw-it-fragment.json**; default entry agent is `technical-director`.

**Two usage modes**: ① **Single gateway, multiple agents** — same OpenClaw instance, use [§4 Agent groups](#4-agent-groups-multi-agent-and-routing-in-one-gateway) bindings to route by channel/accountId. ② **Multiple gateways** — one `--profile` per domain for full isolation (config, port, workspace); see [§3 Multiple gateways](#3-multiple-gateways-same-host-multiple-agent-groups).

**Create an independent instance**: Run `openclaw --profile <domain> setup`, then `openclaw --profile <domain> gateway --port <port>` (use a port offset ≥20 from the main instance, e.g. 18809 for education). Config and state are isolated per profile (§3).

**Configure agents**: Copy or link the repo directory into your OpenClaw workspace (e.g. `~/.openclaw/workspace-education/edu-assistant`), then set `id`, `workspace`, `agentDir` in `agents.list` and add `bindings` for routing. See [§6 Creating agents](#6-creating-agents) and [§7 Configuring agents](#7-configuring-agents).

**Summary table (example)**

| Domain | profile | Suggested port | Representative agentId | Workspace path example |
|--------|---------|----------------|------------------------|-------------------------|
| education | education | 18809 | edu-assistant | `~/.openclaw/workspace-education/edu-assistant` |
| wecom-kf | wecom-kf | 18819 | presale | `~/.openclaw/workspace-wecom-kf/presale` |
| partner | partner | 18839 | companion | `~/.openclaw/workspace-partner/companion` |
| product | product | 18849 | pm-assistant | `~/.openclaw/workspace-product/pm-assistant` |
| game | game | 18859 | game-host | `~/.openclaw/workspace-game/game-host` |
| it | it | 18829 | technical-director | `~/.openclaw/workspace-it/technical-director` |
| web3 | web3 | 18869 | chain-analyst | `~/.openclaw/workspace-web3/chain-analyst` |

For it, workspace paths use **unnumbered** names (matching agent id). When deploying, copy or link e.g. repo `it/1-technical-director` to `~/.openclaw/workspace-it/technical-director`, and similarly for other roles (`it/2-project-manager` → `workspace-it/project-manager`, etc.).

**OpenClaw docs and ops**: Full index [docs.openclaw.ai/llms.txt](https://docs.openclaw.ai/llms.txt); if unreachable, use [GitHub mirror](https://github.com/openclaw/openclaw/tree/main/docs). With multiple profiles, run `openclaw status`, `openclaw doctor`, `openclaw health --json` with `--profile <name>`. Memory and skills: [Memory](https://docs.openclaw.ai/concepts/memory), [Skills](https://docs.openclaw.ai/tools/skills). Troubleshooting: [Updating / If you're stuck](https://docs.openclaw.ai/install/updating), [Discord](https://discord.gg/clawd).

**Further reading**: Domain design and agent roles are documented under `partme-docs/OpenClaw-垂直领域应用分析` in the repo.

---

## 10. Paths & Deployment

### Path reference

| Path | Env var | Default | Description |
|------|----------|--------|-------------|
| Config | `OPENCLAW_CONFIG_PATH` | `~/.openclaw/openclaw.json` | Main config |
| State root | `OPENCLAW_STATE_DIR` | `~/.openclaw` | All state |
| Workspace | `OPENCLAW_WORKSPACE` / `OPENCLAW_PROFILE` | `~/.openclaw/workspace` | Default workspace |
| Agent dir | - | `~/.openclaw/agents/<agentId>/agent` | Agent state |
| Sessions | - | `~/.openclaw/agents/<agentId>/sessions` | Chat history |
| Global skills | - | `~/.openclaw/skills` | Shared skills |

### Directory layout

```
~/.openclaw/
├── openclaw.json
├── workspace/                 # default (main)
│   ├── AGENTS.md, SOUL.md, USER.md, BOOTSTRAP.md, HEARTBEAT.md
│   └── skills/
├── workspace-<agentId>/
├── agents/
│   ├── main/
│   │   ├── agent/            # auth-profiles.json, config.json
│   │   └── sessions/
│   └── <agentId>/
├── credentials/
└── skills/
```

### Environment-based deployment

```bash
# Dev
export OPENCLAW_CONFIG_PATH="$HOME/.openclaw/openclaw.dev.json"
export OPENCLAW_STATE_DIR="$HOME/.openclaw-dev"

# Prod
export OPENCLAW_CONFIG_PATH="/etc/openclaw/openclaw.json"
export OPENCLAW_STATE_DIR="/var/lib/openclaw"
```

### systemd (Linux)

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

### Permissions and backup

```bash
chmod 700 ~/.openclaw
chmod 600 ~/.openclaw/openclaw.json
chmod 600 ~/.openclaw/agents/*/agent/auth-profiles.json
```

Use a scheduled job to back up `openclaw.json`, `workspace*`, and `agents` to dated tar.gz and retain the last N backups.

---

## 11. Templates & Agent Mapping

### Workspace file layout

```
<agent-name>/
├── AGENTS.md      # Role, tools, constraints
├── SOUL.md        # Personality, tone, style
├── USER.md        # User preferences, context
├── BOOTSTRAP.md   # Startup behavior
├── HEARTBEAT.md   # Periodic tasks
├── IDENTITY.md    # Identity (optional)
└── TOOLS.md       # Tool usage (optional)
```

Vertical-domain templates live in this repo under `education/`, `wecom-kf/`, `partner/`, `product/`, `game/`, `web3/`; it templates under `it/`. See [§9 Vertical domains](#9-vertical-domains-independent-instances-and-agent-configuration).

### Agent type examples (official paths only)

Conceptual examples using the [official path convention](https://docs.openclaw.ai/concepts/multi-agent#paths-quick-map) (`~/.openclaw/workspace-<agentId>`, `~/.openclaw/agents/<agentId>/agent`):

| Workspace path (example) | Purpose |
|--------------------------|---------|
| `~/.openclaw/workspace` | Default main agent, general chat |
| `~/.openclaw/workspace-work` | Work context |
| `~/.openclaw/workspace-personal` | Personal context |
| `~/.openclaw/workspace-coding` | Coding assistant |
| `~/.openclaw/workspace-social` | Social / content |

Each agent must have its own `agentDir` (e.g. `~/.openclaw/agents/work/agent`); do not share it.

### Creating an agent from an existing directory

```bash
# If you already have a workspace directory (e.g. copied or created by hand)
mkdir -p ~/.openclaw/workspace-coding
# Add AGENTS.md, SOUL.md, USER.md, etc. (see "Workspace file layout" above)

# Add an entry to agents.list in openclaw.json, e.g.:
# id: "coding", workspace: "~/.openclaw/workspace-coding", agentDir: "~/.openclaw/agents/coding/agent"
```

---

## 12. Multi-Agent Constraints

### Isolation

| Resource | Level | Notes |
|----------|-------|-------|
| Workspace | ✅ Isolated | Per-agent directory |
| Auth | ✅ Isolated | `auth-profiles.json` per agent |
| Sessions | ✅ Isolated | Session key includes `agentId` |
| Model config | ✅ Isolated | Per-agent |
| Global skills | ⚠️ Read-only shared | `~/.openclaw/skills` |
| Channel connection | ⚠️ Shared | Connection pool shared; routing per agent |

### Critical constraints

1. **Do not share agentDir**  
   Multiple agents using the same `agentDir` causes auth/session/config conflicts. Each agent must have its own (e.g. `~/.openclaw/agents/<id>/agent`).

2. **Auth is not shared automatically**  
   Main agent credentials are not given to other agents; log in per agent or copy `auth-profiles.json` manually.

3. **DM access control is per channel**  
   Pairing/allowlist is configured under `channels.<channel>` and applies to the whole channel, not per agent.

4. **Agent-to-agent must be enabled explicitly**  
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

### Performance and limits

| Metric | Suggested | Notes |
|--------|-----------|-------|
| Agent count | 5–10 | Per gateway instance |
| Concurrent sessions | 10–20 per agent | Depends on model and hardware |
| Memory | ~100MB per agent | Workspace + session cache |
| Startup | +2–5s per agent | Depends on workspace size |

### Security and best practices

- Workspace is the default cwd but not a hard sandbox; absolute paths can access the host. Enable `sandbox` for strict isolation.
- Use `chmod 600` for `openclaw.json` and `auth-profiles.json`.
- You can version-control config but add `agents/*/agent/auth-profiles.json` and `credentials/**` to `.gitignore`.

---

## 13. Troubleshooting

### Common issues

| Symptom | Action |
|---------|--------|
| Wrong routing | `openclaw agents list --bindings`; `openclaw gateway --verbose` for routing logs |
| Auth failure | Check `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`; `openclaw channels login` to re-login |
| Session mix-up | `rm -rf ~/.openclaw/agents/<agentId>/sessions/*` then restart gateway |
| Config not applied | `openclaw doctor` to check; `openclaw gateway restart` to apply config |

### Debug commands

```bash
openclaw gateway --verbose
openclaw channels status --probe
openclaw agents list --bindings
openclaw doctor
```

### Install and startup

- **Install fails**: Ensure Node.js ≥ 18 (`node --version`), npm permissions, and if needed `npm cache clean --force`.
- **Startup fails**: Check port (e.g. `lsof -i :8080`), config validation, and verbose logs.

### Update and uninstall

```bash
# Update
curl -fsSL https://openclaw.ai/install.sh | bash
# or npm update -g openclaw / brew upgrade openclaw

# Uninstall
curl -fsSL https://openclaw.ai/uninstall.sh | bash
# or npm uninstall -g openclaw; optionally rm -rf ~/.openclaw (destructive)
```

---

## 14. Links

- [OpenClaw docs](https://docs.openclaw.ai)
- [CLI Reference](https://docs.openclaw.ai/cli) — commands and global options (`--profile`, `--dev`, `gateway`, `agents`, `channels`, etc.)
- [Multi-Agent Routing](https://docs.openclaw.ai/concepts/multi-agent)
- [Multiple Gateways (same host)](https://docs.openclaw.ai/gateway/multiple-gateways) — official multi-gateway guide (repo: `research/claw-ecosystem/openclaw/docs/gateway/multiple-gateways.md`, `docs/zh-CN/gateway/multiple-gateways.md`)
- [Channels](https://docs.openclaw.ai/channels)
- [Docs index llms.txt](https://docs.openclaw.ai/llms.txt)

---

**Last updated**: 2026-02-20

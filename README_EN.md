# Claw Agents

This repository is a workspace library for the `OctoClaw / OpenClaw` ecosystem. It provides reusable agent definitions, domain orchestration layouts, channel operation pipelines, and skill selection documents.

The top-level layout now aligns with the [agency-agents](https://github.com/msitarzewski/agency-agents) taxonomy (for example `engineering/`, `marketing/`, `specialized/`). Standard roster agents live under the matching category. PartMe-specific agents and legacy channel docs live under `specialized/partme/` (including former IM channel notes, per-platform Content Ops READMEs, and software-delivery remnants).

> `OctoClaw` focuses on zero-trust execution, streaming responses, talk-while-executing, and enterprise-grade safety. The agent definitions and skill docs in this repo can be used directly as business workspaces for OctoClaw, while remaining compatible with OpenClaw-style workspace organization.  
> References: `../octoclaw/README.md`, `../octoclaw/README_CN.md`

---

## Contents

1. [Repository Overview](#1-repository-overview)
2. [Recommended Installation](#2-recommended-installation)
3. [Quick Start for an Agent Group](#3-quick-start-for-an-agent-group)
4. [Taxonomy and Representative Agents](#4-taxonomy-and-representative-agents)
5. [Skills System and Installation Strategy](#5-skills-system-and-installation-strategy)
6. [Agent Documentation Standard](#6-agent-documentation-standard)
7. [Configuration and Deployment Guidance](#7-configuration-and-deployment-guidance)
8. [Typical Adoption Scenarios](#8-typical-adoption-scenarios)
9. [Documentation Entry Points](#9-documentation-entry-points)

---

## 1. Repository Overview

### Top-level structure

```text
claw-agents/
├── academic/
├── design/
├── engineering/
├── game-development/
├── marketing/
├── paid-media/
├── product/
├── project-management/
├── sales/
├── spatial-computing/
├── specialized/
│   └── partme/
├── strategy/
├── support/
├── testing/
├── config/
├── docs/
└── scripts/
```

### Layout

| Layer | Description |
|-------|-------------|
| Agency-aligned categories | Same names as `research/agency-agents`; agent folders use kebab-case slugs. `AGENTS.md` / `IDENTITY.md` / `SOUL.md` from the OpenClaw export are merged into these folders where applicable. |
| `specialized/partme/` | Non-roster or legacy assets (`im-channels/`, `content-ops/`, `digital-workforce-legacy/`, etc.). Duplicate roster paths are kept under `specialized/partme/roster-collision/` for traceability. |

Bulk migration is implemented in `scripts/migrate_to_agency_layout.py` (supports `--dry-run`). Historical docs may still mention old paths; trust the current tree.

---

## 2. Recommended Installation

### 2.1 Runtime installation

This repository is best used with `OctoClaw`. If you are still running an `OpenClaw`-style workspace layout, the same workspace structure still applies.

**OctoClaw (recommended for enterprise-grade streaming execution)**

```bash
git clone https://github.com/octoclaw-labs/octoclaw.git
cd octoclaw
cargo build --release
cargo run -p octoclaw-cli -- chat
```

**Config locations**

- OctoClaw: `~/.octoclaw/config.toml`
- OpenClaw-compatible workspace layout: typically still uses `~/.openclaw/...` for workspace and agent state

See `../octoclaw/README.md` and `../octoclaw/README_CN.md` for runtime positioning and architecture.

### 2.2 Skill installation CLIs

This repo follows a two-source skill strategy:

1. `ClawHub / SkillHub` first
2. `skills.sh` as supplement

For mainland-friendly installation, install SkillHub CLI first:

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

Then install skills with:

```bash
skillhub install <slug>
```

If you use ClawHub directly:

```bash
clawhub install <slug> --workdir ~/.openclaw;
```

If you use skills.sh:

```bash
npx skills add <owner/repo> --skill <skill-name> -y -g;
```

### 2.3 Skill directory rules

Your installed skill directory must match the actual runtime loading directory:

| Type | Typical path |
|------|--------------|
| Global skills | `~/.openclaw/skills/` |
| Workspace skills | `<workspace>/.openclaw/skills/` |

Since `npx skills add` does not always install into the same directory structure used by OpenClaw/OctoClaw workspaces:

- Prefer `clawhub install` / `skillhub install` when possible
- If you use `npx skills add`, copy or symlink the skill into the actual runtime skill directory

See `docs/SKILLS-MASTER.md` for the full explanation.

---

## 3. Quick Start for an Agent Group

### Option 1: reuse repo folders as workspace templates

1. Pick a directory, for example:
   - `specialized/partme/software-delivery/`
   - `specialized/partme/web3/`
   - `specialized/partme/content-ops/xiaohongshu/`
2. Copy or symlink the target role directory into the runtime workspace
3. Register `agentId`, `workspace`, and `agentDir` in runtime config
4. Enable bindings and agent-to-agent delegation as needed

### Option 2: create the runtime agent first, then overlay this repo's definition

If you already have agent management commands, create the agent first and then overlay the workspace files from this repo:

```bash
mkdir -p ~/.openclaw/workspace-technical-director
mkdir -p ~/.openclaw/agents/technical-director/agent
mkdir -p ~/.openclaw/agents/technical-director/sessions
```

Then copy the role definition:

```bash
cp -R "/path/to/claw-agents/specialized/partme/software-delivery/1-technical-director/"* \
  ~/.openclaw/workspace-technical-director/
```

### Minimal config example

```json5
{
  "agents": {
    "list": [
      {
        "id": "technical-director",
        "default": true,
        "workspace": "~/.openclaw/workspace-technical-director",
        "agentDir": "~/.openclaw/agents/technical-director/agent"
      }
    ]
  }
}
```

### Verification

```bash
openclaw agents list --bindings
openclaw channels status --probe
openclaw doctor
```

If you use OctoClaw, apply the same principles using its own CLI and config model:

- one workspace per agent
- one state directory per agent
- skill directories must match runtime loading paths
- risky write actions should default to approval gates

---

## 4. Taxonomy and Representative Agents

### 4.1 Agency-aligned examples

- Engineering & delivery: `engineering/frontend-developer`, `engineering/backend-architect`, `engineering/code-reviewer`
- Growth & content: `marketing/douyin-strategist`, `marketing/xiaohongshu-specialist`, `marketing/zhihu-strategist`
- Games: `game-development/unity-architect`, `game-development/godot-gameplay-scripter`
- Sales & ads: `sales/outbound-strategist`, `paid-media/ppc-campaign-strategist`

### 4.2 PartMe extensions (`specialized/partme/`)

- IM scenarios: `specialized/partme/im-channels/discord/`, `telegram/`, etc.
- Channel ops docs: `specialized/partme/content-ops/douyin/`, `xiaohongshu/`, etc.
- Delivery & Web3 remnants: `specialized/partme/software-delivery/`, `specialized/partme/web3/`; full legacy tree under `specialized/partme/digital-workforce-legacy/`

---

## 5. Skills System and Installation Strategy

### 5.1 Where skill docs live

**Root-level overview**

- `docs/SKILLS-MASTER.md`: global skills index, install path guidance, Baoyu master list

**Group-level READMEs**

- `specialized/partme/im-channels/README.md`
- `specialized/partme/digital-workforce-legacy/README.md`
- `specialized/partme/content-ops/README.md`

**Channel/domain-level skill docs**

Most mature domains now include:

- `README.md`
- `CLAWHUB-SKILLS.md`
- `SKILLS-SH-SKILLS.md`
- `SKILLS-EVALUATION.md`

For example:

- `specialized/partme/content-ops/xiaohongshu/README.md`
- `specialized/partme/content-ops/xiaohongshu/CLAWHUB-SKILLS.md`
- `specialized/partme/content-ops/xiaohongshu/SKILLS-SH-SKILLS.md`
- `specialized/partme/content-ops/xiaohongshu/SKILLS-EVALUATION.md`

Software delivery has its own domain-specific variant:

- `specialized/partme/software-delivery/README.md`
- `specialized/partme/software-delivery/IT-SKILLS.md`
- `specialized/partme/software-delivery/SKILLS-EVALUATION-IT.md`

### 5.2 Global selection rules

The repository consistently follows these rules:

1. Check whether `ClawHub / SkillHub` already provides a high-quality platform-specific skill
2. Use `skills.sh` and `Baoyu` skills to fill the gaps for formatting, crawling, illustration, compression, and publishing
3. Keep one best-in-class skill per capability whenever possible to avoid redundant installs

### 5.3 Standard capability model for Content Ops

For a content platform pipeline, the skill stack usually spans these layers:

| Capability layer | Typical use | Typical source |
|------------------|-------------|----------------|
| Platform connection | search, publish, comments, account operations | ClawHub / SkillHub |
| Crawling and conversion | URL to Markdown, article extraction | skills.sh / Baoyu |
| Structured output | daily reports, breakdown reports, formatted Markdown | skills.sh / Baoyu |
| Illustration generation | covers, inline visuals, infographics, comics | skills.sh / Baoyu |
| Pre-publish processing | image compression, HTML conversion | skills.sh / Baoyu |
| Analytics and review | reports, trend summaries, feedback loops | platform skills + Markdown formatting skills |

### 5.4 High-frequency Baoyu skills

The root README does not need every install command inline, but these are the most important cross-channel building blocks:

- `baoyu-url-to-markdown`
- `baoyu-format-markdown`
- `baoyu-cover-image`
- `baoyu-article-illustrator`
- `baoyu-xhs-images`
- `baoyu-compress-image`
- `baoyu-markdown-to-html`
- `baoyu-post-to-wechat`
- `baoyu-post-to-x`
- `baoyu-translate`

See `docs/SKILLS-MASTER.md` for the full table and installation guidance.

---

## 6. Agent Documentation Standard

The current repository standard is a “7 files + `zh-CN` mirror” structure.

### Standard file set

```text
<agent-dir>/
├── AGENTS.md
├── BOOTSTRAP.md
├── HEARTBEAT.md
├── IDENTITY.md
├── SOUL.md
├── TOOLS.md
├── USER.md
└── zh-CN/
    ├── AGENTS.md
    ├── BOOTSTRAP.md
    ├── HEARTBEAT.md
    ├── IDENTITY.md
    ├── SOUL.md
    ├── TOOLS.md
    └── USER.md
```

### What each file is for

| File | Purpose |
|------|---------|
| `AGENTS.md` | role definition, boundaries, behavior rules, delegation structure |
| `SOUL.md` | personality, tone, values, communication style |
| `IDENTITY.md` | identity card, self-introduction, invocation scenarios |
| `TOOLS.md` | tools, deliverables, and operating workflows |
| `USER.md` | information about the people or business this agent serves |
| `BOOTSTRAP.md` | first-run guidance and initialization tasks |
| `HEARTBEAT.md` | recurring tasks, monitoring, and proactive actions |

### Language convention

- English files are used as the primary runtime-facing definitions
- `zh-CN/` is for team reading, operational handoff, and business-side maintenance
- New or updated agents should ideally keep English and Chinese versions aligned

---

## 7. Configuration and Deployment Guidance

### Workspace mapping principles

Whether you use OctoClaw or an OpenClaw-style layout, follow these rules:

- one workspace per agent
- one `agentDir` per agent
- isolated session storage
- skill directories must match the actual runtime loading path

### Multi-agent deployment guidance

If you are deploying a team rather than a single role:

- configure one entry role as `default: true`
- route channel entrypoints to that role via `bindings`
- enable `agent-to-agent` only for the required downstream roles
- put approval gates in front of publishing, outreach, and comment-reply write actions

### Ports and isolation

If you deploy multiple agent groups on the same machine:

- isolate config files
- isolate state directories
- isolate workspaces
- isolate base ports
- avoid overlap in browser / CDP / canvas derived ports

That was already true in old OpenClaw multi-gateway setups and remains true for OctoClaw deployments.

---

## 8. Typical Adoption Scenarios

### Software delivery team

Start with `specialized/partme/software-delivery/` (and roster agents under `engineering/`, etc.):

- use `technical-director` as the entry orchestrator
- use project, product, architecture, frontend, backend, QA, and ops roles as executors
- add `code-reviewer`, `backend-architect`, and similar specialists as enhancements

### Content operations team

Start with `specialized/partme/content-ops/<channel>` and deploy the channel pipeline:

- first monitoring, breakdown, writing/rewrite, publishing
- then analytics assistant and comment management
- choose skills from the channel `README.md` and `SKILLS-EVALUATION.md`

### Community and IM operations

Start with `specialized/partme/im-channels/<channel>` and split responsibilities into bot development, community operations, and support.

---

## 9. Documentation Entry Points

### Recommended reading order

1. `docs/README.md`
2. `docs/SKILLS-MASTER.md`
3. group-level READMEs
4. specific domain/channel `README.md`
5. `CLAWHUB-SKILLS.md` / `SKILLS-SH-SKILLS.md` / `SKILLS-EVALUATION*.md`

### Quick links

- global skills index: `docs/SKILLS-MASTER.md`
- IM channels overview: `specialized/partme/im-channels/README.md`
- digital workforce overview: `specialized/partme/digital-workforce-legacy/README.md`
- content ops overview: `specialized/partme/content-ops/README.md`
- full Xiaohongshu example: `specialized/partme/content-ops/xiaohongshu/README.md`

---

**Last updated**: 2026-04-12

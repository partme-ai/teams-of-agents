# Telegram 专用智能体 (Telegram Agents)

> 基于 [ClawHub telegram 技能](https://clawhub.ai/skills?sort=downloads&q=telegram) 与 [skills.sh telegram](https://skills.sh/?q=telegram)（含 [telegram-bot-builder](https://skills.sh/sickn33/antigravity-awesome-skills/telegram-bot-builder)）的 Telegram Bot API 技能，为 Telegram 渠道提供三类专用智能体：机器人开发、社区运营、客服/答疑。与 openclaw-agents 其他领域（discord / wechat-article / company 等）并列，单独目录便于按渠道绑定与扩展。

## 技能来源区分

| 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|----------|--------------|----------|
| **ClawHub** | [clawhub.ai/skills?q=telegram](https://clawhub.ai/skills?sort=downloads&q=telegram) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug>` |
| **skills.sh** | [skills.sh/?q=telegram](https://skills.sh/?q=telegram) | 见下方技能表与安装方式 | `npx skills add <owner/repo> --skill <名>` |

## 智能体清单

| 序号 | Agent id               | 展示名             | 目录                     | 职责摘要 |
|------|------------------------|--------------------|---------------------------|----------|
| 1    | telegram-bot-developer | Telegram 机器人开发 | 1-telegram-bot-developer  | 架构、命令、Inline 键盘、回调、Webhook、可选变现；在 TOOLS.md 备注下开发 |
| 2    | telegram-community     | Telegram 社区运营   | 2-telegram-community      | 公告、群组/频道管理、引导与互动流程；不制定政策 |
| 3    | telegram-support       | Telegram 客服       | 3-telegram-support        | FAQ、支持分流、Inline 菜单、转人工；仅按文档回答，有疑问升级 |

## 预设技能（默认安装）

**ClawHub 技能一览**见 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)，**skills.sh 技能与安装**见下方。各智能体在配置片段中已绑定 Telegram 相关技能。合并 `config/openclaw-telegram-fragment.json` 后，OpenClaw 会按 `agents.list[].skills` 加载对应技能；当前默认使用 **telegram-bot-builder**（skills.sh），可改为 ClawHub 的 `telegram` 或 `telegram-api`，安装后目录名与 config 中 `skills` 一致即可。

| Agent id               | 默认技能列表         | 用途说明 |
|------------------------|----------------------|----------|
| telegram-bot-developer  | telegram-bot-builder | Bot 架构、Telegraf/grammY/python-telegram-bot/aiogram、命令、键盘、回调、Webhook、变现 |
| telegram-community      | telegram-bot-builder | 发消息、Inline 键盘、公告与社区流程 |
| telegram-support        | telegram-bot-builder | 回复模式、FAQ 菜单、非阻塞流程与分流 |

### 安装方式（按来源区分）

**来源：ClawHub** — 安装后目录名与 config 中 `skills` 一致。

```bash
clawhub search telegram
clawhub install <slug>
```

**来源：skills.sh** — 安装：`npx skills add <owner/repo> --skill <名>`；默认 telegram-bot-builder（[sickn33/antigravity-awesome-skills](https://skills.sh/sickn33/antigravity-awesome-skills/telegram-bot-builder)）；完整列表可查 [skills.sh/?q=telegram](https://skills.sh/?q=telegram)。可选 Baoyu 技能（配图/排版/多平台发帖等）见 skills.sh Baoyu 系列。

```bash
npx skills add sickn33/antigravity-awesome-skills --skill telegram-bot-builder
# 或
npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill telegram-bot-builder
```

若 OpenClaw 从 `~/.openclaw/skills` 或项目内 `skills/` 加载，也可将仓库中对应技能目录复制到该路径下，保证目录名为 `telegram-bot-builder`。若使用 `npx skillsadd`（无空格），格式以 skills.sh 文档为准。

**环境变量：** 使用前在运行环境中配置 `BOT_TOKEN`（在 [@BotFather](https://t.me/BotFather) 创建 Bot 后获取）。不要在 TOOLS.md 或配置文件中写入 Token。

## 配置说明

- **Workspace：** 各智能体 workspace 指向本目录下对应子目录（如 `<REPO_ROOT>/openclaw-agents/telegram/1-telegram-bot-developer`），或部署时复制/链接到 `~/.openclaw/workspace-telegram-bot-developer` 等。
- **Config 片段：** 见仓库 `config/openclaw-telegram-fragment.json`，可合并进主 openclaw 配置；将 `<REPO_ROOT>` 替换为 openclaw-agents 实际路径。
- **路由：** 通过 bindings 将 Telegram 渠道（或按群组/会话）路由到对应 agent id。

## 初始化命令示例

```bash
# 添加 Telegram 智能体（3 个）
openclaw agents add telegram-bot-developer --workspace ~/.openclaw/workspace-telegram-bot-developer;
openclaw agents add telegram-community     --workspace ~/.openclaw/workspace-telegram-community;
openclaw agents add telegram-support       --workspace ~/.openclaw/workspace-telegram-support;

# 绑定 Telegram 渠道到开发（或按需绑定 community / support）
openclaw agents bind --agent telegram-bot-developer --bind telegram:telegram-bot-developer
```

## 文件结构（每智能体）

与 discord / wechat-article 一致：`AGENTS.md`、`zh-CN/AGENTS.md`、`SOUL.md`、`zh-CN/SOUL.md`、`IDENTITY.md`、`zh-CN/IDENTITY.md`、`TOOLS.md`、`zh-CN/TOOLS.md`、`BOOTSTRAP.md`、`zh-CN/BOOTSTRAP.md`、`USER.md`、`HEARTBEAT.md`、`zh-CN/HEARTBEAT.md`。

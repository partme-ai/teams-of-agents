# Discord 专用智能体 (Discord Agents)

> 基于 [ClawHub discord 技能](https://clawhub.ai/skills?sort=downloads&q=discord) 与 [skills.sh discord](https://skills.sh/?q=discord)（含 [vm0-ai/vm0-skills/discord](https://github.com/vm0-ai/vm0-skills/tree/HEAD/discord)）的 Discord Bot API 技能，为 Discord 服务器提供三类专用智能体：审核、社区运营、客服/答疑。与 openclaw-agents 其他领域（company / it / game 等）并列，单独目录便于按渠道绑定与扩展。

## 技能来源区分

| 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|----------|--------------|----------|
| **ClawHub** | [clawhub.ai/skills?q=discord](https://clawhub.ai/skills?sort=downloads&q=discord) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug>` |
| **skills.sh** | [skills.sh/?q=discord](https://skills.sh/?q=discord) | 见下方技能表与安装方式 | `npx skills add <owner/repo> --skill <名>` |

## 智能体清单

| 序号 | Agent id           | 展示名           | 目录                   | 职责摘要 |
|------|--------------------|------------------|------------------------|----------|
| 1    | discord-mod        | Discord 审核     | 1-discord-mod          | 删消息、加反应、规则提醒、频道/服务器/成员查询；在 TOOLS.md 规则下执行 |
| 2    | discord-community  | Discord 社区运营 | 2-discord-community   | 公告、Embed、频道/Webhook 创建、氛围与活动；不制定政策 |
| 3    | discord-support    | Discord 客服     | 3-discord-support     | 频道内答疑、FAQ、反应、转人工；仅按文档回答，有疑问升级 |

## 预设技能（默认安装）

**ClawHub 技能一览**见 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)，**skills.sh 技能与安装**见下方。各智能体在配置片段中已绑定 Discord 相关技能。合并 `config/openclaw-discord-fragment.json` 后，OpenClaw 会按 `agents.list[].skills` 加载对应技能；当前默认使用 **discord**（可来自 ClawHub 或 skills.sh vm0-ai/steipete），安装后目录名与 config 中 `skills` 一致即可。

| Agent id          | 默认技能列表   | 用途说明 |
|-------------------|----------------|----------|
| discord-mod       | discord        | Discord Bot API：删消息、反应、频道/服务器/成员 |
| discord-community | discord        | 发消息、Embed、创建 Webhook/文本频道 |
| discord-support   | discord        | 读/发消息、反应、频道/服务器信息 |

### 安装方式（按来源区分）

**来源：ClawHub** — 安装后目录名与 config 中 `skills` 一致。

```bash
clawhub search discord
clawhub install <slug>
```

**来源：skills.sh** — 安装：`npx skills add <owner/repo> --skill <名>`；可选 vm0-ai/vm0-skills（discord、discord-webhook）、steipete/clawdis（discord）、sickn33/antigravity-awesome-skills（discord-bot-architect、discord-automation）；完整列表可查 [skills.sh/?q=discord](https://skills.sh/?q=discord)。可选 Baoyu 技能（配图/排版/多平台发帖等）见 skills.sh Baoyu 系列。

```bash
npx skills add vm0-ai/vm0-skills --skill discord
# 或 pnpm
pnpm dlx add-skill https://github.com/vm0-ai/vm0-skills/tree/HEAD/discord
```

若 OpenClaw 从 `~/.openclaw/skills` 或项目内 `skills/` 加载，也可将对应仓库中的 `discord` 目录复制到该路径下。若使用 `npx skillsadd`（无空格），格式以 skills.sh 文档为准。

**环境变量：** 使用前在运行环境中配置 `DISCORD_BOT_TOKEN`（在 [Discord Developer Portal](https://discord.com/developers/applications) 创建应用并添加 Bot 后获取）。不要在 TOOLS.md 或配置文件中写入 Token。

## 配置说明

- **Workspace：** 各智能体 workspace 指向本目录下对应子目录（如 `<REPO_ROOT>/openclaw-agents/discord/1-discord-mod`），或部署时复制/链接到 `~/.openclaw/workspace-discord-mod` 等。
- **Config 片段：** 见仓库 `config/openclaw-discord-fragment.json`，可合并进主 openclaw 配置；将 `<REPO_ROOT>` 替换为 openclaw-agents 实际路径。
- **路由：** 通过 bindings 将 Discord 渠道（或按 guildId/roles）路由到对应 agent id。

## 初始化命令示例

```bash
# 添加 Discord 智能体（3 个）
openclaw agents add discord-mod       --workspace ~/.openclaw/workspace-discord-mod;
openclaw agents add discord-community --workspace ~/.openclaw/workspace-discord-community;
openclaw agents add discord-support  --workspace ~/.openclaw/workspace-discord-support;

# 绑定 Discord 渠道到审核（或按需绑定 community / support）
openclaw agents bind --agent discord-mod --bind discord:discord-mod
```

## 文件结构（每智能体）

与 company 等一致：`AGENTS.md`、`zh-CN/AGENTS.md`、`SOUL.md`、`zh-CN/SOUL.md`、`IDENTITY.md`、`zh-CN/IDENTITY.md`、`TOOLS.md`、`zh-CN/TOOLS.md`、`BOOTSTRAP.md`、`zh-CN/BOOTSTRAP.md`、`USER.md`、`HEARTBEAT.md`、`zh-CN/HEARTBEAT.md`。平台格式：在 Discord 回复时不用 markdown 表格、用列表；多链接用 `<>` 包住以免嵌入。

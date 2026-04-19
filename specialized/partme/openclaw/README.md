# OpenClaw 智能体 (OpenClaw Agents)

> 面向 OpenClaw **运维**与**插件开发**的智能体集合，与 openclaw-agents 其他领域并列；按子目录区分角色，便于在 Gateway 中绑定不同 `agentId`。

## 智能体清单

| 序号 | Agent id | 展示名 | 目录 | 职责摘要 |
|------|----------|--------|------|----------|
| 1 | `openclaw-assistant` | OpenClaw 运维助手 | `openclaw-assistant/` | 以 [OpenClaw 官方文档](https://docs.openclaw.ai/) 与 `llms.txt` 为据，协助**安装、配置、通道、Gateway、模型、节点、插件运行时、自动化与排障**；权限受限：不执行高危命令、不读取系统环境变量；**只给步骤，用户自行执行** |
| 2 | `openclaw-engineer` | OpenClaw 开发工程师 | `openclaw-engineer/` | 以官方 **Plugin SDK**（`plugins/*`、`tools/plugin`）为据，协助 **OpenClaw 插件/扩展开发**——`openclaw.plugin.json`、渠道/Provider/Harness、构建测试、迁移与工具注册；**与运维助手分工**：本角色侧重**工程与 SDK**，不替代生产 incident 处置流程 |

### 分工说明

| 场景 | 优先智能体 |
|------|------------|
| Gateway 起不来、渠道无响应、`doctor`/`logs`、白名单/配对、`openclaw.json` 运维向问题 | `openclaw-assistant` |
| 新建/重构插件、SDK API、manifest、渠道插件代码、Provider 插件、单测与打包 | `openclaw-engineer` |
| 两者交叉（如插件装不上被安全扫描拦截） | 先 `openclaw-engineer` 看清 SDK/安装约定，再结合运维文档排环境 |

## 配置说明

- **Workspace**：将对应子目录设为智能体 workspace，例如复制或链接到 `~/.openclaw/workspace-openclaw-assistant`、`~/.openclaw/workspace-openclaw-engineer`。
- **路由**：按渠道或场景绑定不同 `agentId`（如飞书运维入口 → `openclaw-assistant`，内部插件开发群 → `openclaw-engineer`）。

## 初始化命令示例

以下在 OpenClaw 已安装前提下执行；`--workspace` 请换为你本机实际路径。

### 运维助手

```bash
openclaw agents add openclaw-assistant --workspace ~/.openclaw/workspace-openclaw-assistant
```

### 开发工程师

```bash
openclaw agents add openclaw-engineer --workspace ~/.openclaw/workspace-openclaw-engineer
```

### 查看绑定

```bash
openclaw agents list
openclaw agents bindings
```

### 按渠道绑定（示例）

```bash
openclaw agents bind --agent openclaw-assistant --bind feishu:openclaw-assistant;
openclaw agents bind --agent openclaw-engineer --bind feishu:openclaw-engineer;
```

其他渠道（如 `feishu`、`telegram`、`discord`）将 `wecom` 替换为对应 channel 即可。

（具体子命令以当前 CLI `openclaw agents --help` 为准。）

## 文件结构（每个智能体）

- `AGENTS.md` — 英文，角色与边界（系统提示词来源之一）
- `zh-CN/AGENTS.md` — 中文对照
- `SOUL.md` / `zh-CN/SOUL.md` — 人格与底线
- `IDENTITY.md` / `zh-CN/IDENTITY.md` — 身份与开场
- `TOOLS.md` / `zh-CN/TOOLS.md` — 文档 URL 与仓库备注（**勿存密钥**）
- `USER.md` / `zh-CN/USER.md` — 服务对象信息
- `BOOTSTRAP.md` / `zh-CN/BOOTSTRAP.md` — 首次配置说明，用毕可删
- `HEARTBEAT.md` / `zh-CN/HEARTBEAT.md` — 心跳任务说明

**中英文约定：** 根目录为英文；`zh-CN/` 下为同名中文文件，便于整目录拷贝到业务仓库。

## 文档索引

所有智能体均以 **`https://docs.openclaw.ai/llms.txt`** 为总索引；开发向页面集中在 **`plugins/`** 与 **`tools/plugin`**。

# 助手智能体 (Assistant Agents)

> 面向 OpenClaw 部署与运维的助理智能体集合。与 openclaw-agents 其他领域（company / it / game / wecom-kf）并列，单独目录便于配置与扩展。

## 智能体清单

| 序号 | Agent id | 展示名 | 目录 | 职责摘要 |
|------|----------|--------|------|----------|
| 1 | openclaw-assistant | OpenClaw 运维助手 | 1-openclaw-assistant | 以 [OpenClaw 官方文档](https://docs.openclaw.ai/) 为唯一依据，协助安装、配置、通道、网关、模型、节点、插件、自动化与故障排查；权限受限：不执行有系统风险的命令、不读取系统环境变量；仅提供步骤与建议，由用户自行执行 |

## 配置说明

- **Workspace**：智能体 workspace 指向本目录下对应子目录（如 `<REPO_ROOT>/openclaw-agents/channels/assistant/1-openclaw-assistant`），或部署时复制/链接到 `~/.openclaw/workspace-openclaw-assistant`。
- **Config 片段**：可合并进主 openclaw 配置；使用前将 `<REPO_ROOT>` 替换为 openclaw-agents 实际路径。
- **路由**：按渠道或场景将会话绑定到 `openclaw-assistant`（如部署咨询、故障排查入口）。

## 初始化命令

以下命令在 OpenClaw 配置已就绪的前提下执行；`--workspace` 使用本地路径（如 `~/.openclaw/workspace-openclaw-assistant`），需先将本仓库 `channels/assistant/1-openclaw-assistant` 复制或链接到对应 workspace 目录。

### 1. 查看当前智能体列表

```bash
openclaw agents list
```

### 2. 添加助手智能体

```bash
openclaw agents add openclaw-assistant --workspace ~/.openclaw/workspace-openclaw-assistant;
```

### 3. 查看当前绑定

```bash
openclaw agents bindings
```

### 4. 按渠道绑定智能体（示例）

```bash
openclaw agents bind --agent openclaw-assistant --bind wecom:openclaw-assistant;
```

其他渠道（如 `feishu`、`telegram`、`discord`）将 `wecom` 替换为对应 channel 即可。

## 文件结构（每智能体）

- `AGENTS.md` — **英文**，角色定义、职责、边界、Session Startup、Memory、Red Lines、External vs Internal、Tools、Heartbeats；供 OpenClaw 系统提示词注入
- `zh-CN/AGENTS.md` — **中文**，与 AGENTS.md 内容等价，供团队阅读；整目录 `zh-CN/` 可直接拷贝到业务使用
- `SOUL.md` — 人格与风格、底线（建议在 `zh-CN/` 下提供 SOUL.md 中文版）
- `IDENTITY.md` — **英文**，Who Am I?（Name/Creature/Vibe/Emoji/Avatar 为确定值）+ Purpose、When to Invoke、Expertise、Deliverables；身份已定义，对对话方主动告知，不询问对方该怎么称呼
- `zh-CN/IDENTITY.md` — **中文**，我是谁？+ 职责/何时调用/专长/产出，与 IDENTITY.md 对应
- `TOOLS.md` — 常用文档 URL、环境相关备注（代理、内部 Gateway 地址等）
- `USER.md` — 所服务对象信息（随使用更新）
- `BOOTSTRAP.md` — 首次运行引导（仅配置者使用），完成后删除
- `HEARTBEAT.md` — 心跳任务说明（英文）；留空或仅注释即不执行
- `zh-CN/HEARTBEAT.md` — 心跳任务说明（中文对照）

**中英文约定：** 所有智能体配置提供**中英文两个独立版本**：英文文件在智能体根目录，中文版集中在 `zh-CN/` 子目录下，文件名与英文一致，便于将 `zh-CN/` 整目录拷贝到业务使用。模板与启发见 [docs/AGENTS-template-inspiration](../../docs/AGENTS-template-inspiration.md)、[docs/IDENTITY-template](../../docs/IDENTITY-template.md) 及 [docs/zh-CN/](../../docs/zh-CN/) 下对应中文版。

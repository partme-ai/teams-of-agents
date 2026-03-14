# 企微客服智能体 (WeCom KF Agents)

企微客服场景：主入口（0-main）、售前（presale）、售后（aftersale）、技术（tech）。可单独使用，或作为 SCRM 的客服子角色（见 `config/openclaw-scrm-fragment.json`）。

## 初始化命令（与 company 同规则）

以下命令在 OpenClaw 配置已就绪的前提下执行；需先将本仓库 `wecom-kf/0-main/`、`wecom-kf/presale/` 等复制或链接到对应 workspace 目录。

### 1. 查看当前智能体列表

```bash
openclaw agents list
```

### 2. 添加企微客服智能体（4 个）

```bash
openclaw agents add wecom-kf-main --workspace ~/.openclaw/workspace-wecom-kf/main
openclaw agents add presale      --workspace ~/.openclaw/workspace-wecom-kf/presale
openclaw agents add aftersale    --workspace ~/.openclaw/workspace-wecom-kf/aftersale
openclaw agents add tech         --workspace ~/.openclaw/workspace-wecom-kf/tech
```

说明：主入口在仓库中为 `0-main`，部署时建议对应 agent id 为 `wecom-kf-main` 或 `main`，workspace 指向 `~/.openclaw/workspace-wecom-kf/main`（可将 `0-main/` 内容复制到该目录）。

### 3. 查看当前绑定

```bash
openclaw agents bindings
```

### 4. 按渠道绑定智能体（示例：企微 wecom）

```bash
openclaw agents bind --agent wecom-kf-main --bind wecom:wecom-kf-main
openclaw agents bind --agent presale      --bind wecom:presale
openclaw agents bind --agent aftersale    --bind wecom:aftersale
openclaw agents bind --agent tech         --bind wecom:tech
```

若接入 SCRM，使用 `config/openclaw-scrm-fragment.json`，其 bindings 将 wecom-kf 路由到 scrm-orchestrator；按账号/会话细化 presale/aftersale/tech 时见 partme-docs 客服技术方案。

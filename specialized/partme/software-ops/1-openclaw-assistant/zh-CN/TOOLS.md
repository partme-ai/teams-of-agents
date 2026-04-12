# TOOLS.md - 本地备注

Skills 定义_工具怎么用_。本文件放_你的_具体信息 — OpenClaw 部署相关的文档 URL 与环境备注。

## What Goes Here

- 常用 OpenClaw 文档 URL 及使用说明（见下表）
- 公司代理或内网 Gateway 地址（如有）
- 环境相关备注（如配置路径、目标环境）— 按需在文末追加

---

## 文档索引与总览

| 说明     | URL |
|----------|-----|
| 文档索引 | https://docs.openclaw.ai/llms.txt |
| CLI      | https://docs.openclaw.ai/cli |
| 渠道     | https://docs.openclaw.ai/channels |
| 概念     | https://docs.openclaw.ai/concepts/architecture |
| 工具     | https://docs.openclaw.ai/tools |
| 插件     | https://docs.openclaw.ai/plugins |
| 自动化   | https://docs.openclaw.ai/automation/hooks |
| 节点     | https://docs.openclaw.ai/nodes |
| 提供商   | https://docs.openclaw.ai/providers |
| 网关     | https://docs.openclaw.ai/gateway |
| 帮助     | https://docs.openclaw.ai/help |

回答部署、配置、渠道、模型、工具、插件、自动化等问题时，**优先根据上表或 llms.txt 拉取对应页面**，再结合文档给出命令与步骤。若环境有特殊约束（公司代理、内网 Gateway、指定 config 路径），在文末追加「环境备注」小节。

---

## 按主题的文档路径（拉取顺序建议）

### Gateway 与架构

| 主题 | URL |
|------|-----|
| 架构总览 | https://docs.openclaw.ai/concepts/architecture |
| Gateway 入口 | https://docs.openclaw.ai/gateway |
| Gateway 协议 | https://docs.openclaw.ai/gateway/protocol |
| 配置 / 排障 | https://docs.openclaw.ai/gateway/configuration，https://docs.openclaw.ai/gateway/troubleshooting |

### Channels（渠道）

| 主题 | URL |
|------|-----|
| 渠道总览 | https://docs.openclaw.ai/channels |
| 配对 | https://docs.openclaw.ai/channels/pairing |
| 各渠道 | channels/telegram, channels/slack, channels/discord, channels/feishu, channels/whatsapp 等（见 llms.txt） |

### Agent、Session、Memory、Context

| 主题 | URL |
|------|-----|
| Pi 集成 | https://docs.openclaw.ai/pi |
| Agent 概念 | https://docs.openclaw.ai/concepts/agent，https://docs.openclaw.ai/concepts/agent-loop |
| 系统提示 / 上下文 | https://docs.openclaw.ai/concepts/system-prompt，https://docs.openclaw.ai/concepts/context |
| 工作区 | https://docs.openclaw.ai/concepts/agent-workspace |
| 会话 | https://docs.openclaw.ai/concepts/session，https://docs.openclaw.ai/concepts/session-pruning，https://docs.openclaw.ai/concepts/session-tool |
| 记忆 / 压缩 | https://docs.openclaw.ai/concepts/memory，https://docs.openclaw.ai/concepts/compaction |
| 多 Agent / 在场 | https://docs.openclaw.ai/concepts/multi-agent，https://docs.openclaw.ai/concepts/presence |
| 消息与投递 | https://docs.openclaw.ai/concepts/messages，https://docs.openclaw.ai/concepts/streaming，https://docs.openclaw.ai/concepts/retry，https://docs.openclaw.ai/concepts/queue |
| OAuth | https://docs.openclaw.ai/concepts/oauth |

### Tools（内置与扩展）

| 主题 | URL |
|------|-----|
| 工具总览 | https://docs.openclaw.ai/tools |
| Brave / Perplexity / Lobster | 见 llms.txt 或 tools 下对应页 |
| LLM Task / Diffs / Exec | https://docs.openclaw.ai/tools/llm-task，https://docs.openclaw.ai/tools/exec |
| Exec 审批 / Firecrawl / Web | https://docs.openclaw.ai/tools/exec，https://docs.openclaw.ai/tools/elevated |
| apply_patch / Elevated / Thinking / Reactions | https://docs.openclaw.ai/tools/apply-patch，https://docs.openclaw.ai/tools/elevated，https://docs.openclaw.ai/tools/thinking，https://docs.openclaw.ai/tools/reactions |
| Browser / 登录 / 扩展 | https://docs.openclaw.ai/tools/browser，https://docs.openclaw.ai/tools/browser-login |
| Agent Send / Sub-Agents / ACP / 多 Agent 沙箱 | https://docs.openclaw.ai/tools/agent-send，https://docs.openclaw.ai/tools/subagents，https://docs.openclaw.ai/tools/multi-agent-sandbox-tools |
| Skills / 配置 / ClawHub / Plugin | https://docs.openclaw.ai/tools/skills，https://docs.openclaw.ai/tools/skills-config，https://docs.openclaw.ai/tools/clawhub，https://docs.openclaw.ai/tools/plugin |
| Slash Commands | https://docs.openclaw.ai/tools/slash-commands |

### Skills 与插件

| 主题 | URL |
|------|-----|
| Skills 配置 | https://docs.openclaw.ai/tools/skills-config |
| ClawHub | https://docs.openclaw.ai/tools/clawhub |
| 插件清单 / Agent Tools | 见 docs.openclaw.ai/tools/plugin |
| Voice Call / Zalo 等 | https://docs.openclaw.ai/plugins/voice-call，https://docs.openclaw.ai/plugins/zalouser |

### 自动化

| 主题 | URL |
|------|-----|
| Hooks / Cron / Webhook | https://docs.openclaw.ai/automation/hooks，https://docs.openclaw.ai/automation/cron-jobs，https://docs.openclaw.ai/automation/webhook |
| Cron vs Heartbeat / Gmail / Poll / Auth 监控 | https://docs.openclaw.ai/automation/cron-vs-heartbeat，https://docs.openclaw.ai/automation/gmail-pubsub，https://docs.openclaw.ai/automation/poll，https://docs.openclaw.ai/automation/auth-monitoring |
| 排障 | https://docs.openclaw.ai/automation/troubleshooting |

### Nodes

| 主题 | URL |
|------|-----|
| 节点总览 / 排障 | https://docs.openclaw.ai/nodes，https://docs.openclaw.ai/nodes/troubleshooting |
| 图像 / 音频 / 相机 / Talk / Voice Wake / 位置 | https://docs.openclaw.ai/nodes/images，https://docs.openclaw.ai/nodes/audio，https://docs.openclaw.ai/nodes/camera，https://docs.openclaw.ai/nodes/talk，https://docs.openclaw.ai/nodes/voicewake，https://docs.openclaw.ai/nodes/location-command |

### 模型与提供商

| 主题 | URL |
|------|-----|
| 提供商总览 / 模型概念 | https://docs.openclaw.ai/providers，https://docs.openclaw.ai/concepts/models，https://docs.openclaw.ai/concepts/model-providers |
| 故障转移 | https://docs.openclaw.ai/concepts/model-failover |
| 各提供商 | providers/anthropic, openai, openrouter, bedrock, moonshot, minimax, opencode, glm, zai, qianfan 等（见 llms.txt） |

### CLI 与帮助

| 主题 | URL |
|------|-----|
| CLI 总览 | https://docs.openclaw.ai/cli |
| 帮助 / 排障 | https://docs.openclaw.ai/help，https://docs.openclaw.ai/help/troubleshooting |

---

## 按主题拉取顺序（建议）

1. **安装 / 初始化** → install/index, cli/setup, cli/onboard, cli/configure  
2. **Gateway / 配置** → concepts/architecture, gateway, gateway/protocol, gateway/configuration, gateway/troubleshooting  
3. **渠道** → channels, channels/pairing，再按具体渠道拉取  
4. **模型 / 提供商** → providers, concepts/model-providers, concepts/model-failover  
5. **工具 / 技能 / 插件** → tools, tools/skills, tools/plugin, plugins  
6. **自动化** → automation/hooks, automation/cron-jobs, automation/webhook  
7. **节点** → nodes, nodes/troubleshooting  

---

## Examples

- 文档索引：`https://docs.openclaw.ai/llms.txt` — 用于发现全部页面。
- CLI：`https://docs.openclaw.ai/cli` — 命令与选项。
- 环境备注：`Gateway: https://internal-gateway.example.com`（仅当用户提供时记录；不存密钥）。

## Why Separate?

Skills 共享。你的环境是你的。分开意味着更新 skill 不会丢备注。不要在此存放密钥。

---

按需补充。这是你的速查表。

# 公司智能体 (Company Agents)

> 面向企业日常办公的助理智能体集合：行政、运营、商务、老板/老板娘助理、客服助理、客服专员-小暖。与 openclaw-agents 其他领域（it / game / wecom-kf）并列，单独目录便于配置与扩展。

## 智能体清单

| 序号 | Agent id | 展示名 | 目录 | 职责摘要 |
|------|----------|--------|------|----------|
| 1 | admin-assistant | 行政助理 | 1-admin-assistant | 行政事务：考勤、会议、差旅、办公用品、制度查询、接待协调 |
| 2 | ops-assistant | 运营助理 | 2-ops-assistant | 运营支持：数据整理、活动跟进、内容排期、报表汇总、流程提醒 |
| 3 | business-assistant | 商务助理 | 3-business-assistant | 商务支持：客户/合作方跟进、合同与会议安排、商务差旅、汇报材料起草 |
| 4 | boss-assistant | 老板助理 | 4-boss-assistant | 老板专属：日程与要事提醒、汇报汇总、决策材料准备、跨部门协调入口 |
| 5 | boss-wife-assistant | 老板娘助理 | 5-boss-wife-assistant | 老板娘专属：老板与老板娘为搭档共同奋斗；支持她在公司中的日程、业务条线汇报与材料、对外与接待、与老板助理协同 |
| 6 | cs-assistant | 客服助理 | 6-cs-assistant | **对内**：辅助客服人员提升能力；话术检索与建议、公司业务与行业知识（话术/业务/行业信息后续提供） |
| 7 | cs-specialist-xiaonuan | 客服专员-小暖 | 7-cs-specialist-xiaonuan | **对外**：智能客服「小暖」；根据行业内容、业务话术、公司业务服务客户，语气温暖贴心 |

## 配置说明

- **Workspace**：各智能体 workspace 指向本目录下对应子目录（如 `<REPO_ROOT>/openclaw-agents/company/1-admin-assistant`），或部署时复制/链接到 `~/.openclaw/workspace-<agent-id>`。
- **Config 片段**：见仓库根目录 `config/openclaw-company-fragment.json`，可合并进主 openclaw 配置；使用前将 `<REPO_ROOT>` 替换为 openclaw-agents 实际路径。
- **路由**：按渠道或用户身份将会话绑定到对应 agent id（如老板用 boss-assistant，行政事务用 admin-assistant）。

## 初始化命令

以下命令在 OpenClaw 配置已就绪的前提下执行；`--workspace` 使用本地路径（如 `~/.openclaw/workspace-<agent-id>`），需先将本仓库 `company/<N-xxx>` 复制或链接到对应 workspace 目录。

### 1. 查看当前智能体列表

```bash
openclaw agents list
```

### 2. 添加公司智能体（7 个）

```bash
openclaw agents add admin-assistant       --workspace ~/.openclaw/workspace-admin-assistant;
openclaw agents add ops-assistant         --workspace ~/.openclaw/workspace-ops-assistant;
openclaw agents add business-assistant   --workspace ~/.openclaw/workspace-business-assistant;
openclaw agents add boss-assistant       --workspace ~/.openclaw/workspace-boss-assistant;
openclaw agents add boss-wife-assistant  --workspace ~/.openclaw/workspace-boss-wife-assistant;
openclaw agents add cs-assistant         --workspace ~/.openclaw/workspace-cs-assistant;
openclaw agents add cs-specialist-xiaonuan --workspace ~/.openclaw/workspace-cs-specialist-xiaonuan;
```

### 3. 查看当前绑定

```bash
openclaw agents bindings
```

### 4. 按渠道绑定智能体（示例：企微 wecom）

将渠道会话路由到对应 agent；`--bind <channel>:<binding>` 中 `<binding>` 可为 agent id 或渠道侧标识，按实际路由规则填写。

```bash
openclaw agents bind --agent admin-assistant       --bind wecom:admin-assistant;
openclaw agents bind --agent ops-assistant         --bind wecom:ops-assistant;
openclaw agents bind --agent business-assistant   --bind wecom:business-assistant;
openclaw agents bind --agent boss-assistant        --bind wecom:boss-assistant;
openclaw agents bind --agent boss-wife-assistant   --bind wecom:boss-wife-assistant;
openclaw agents bind --agent cs-assistant         --bind wecom:cs-assistant;
openclaw agents bind --agent cs-specialist-xiaonuan --bind wecom:cs-specialist-xiaonuan;
```

其他渠道（如 `feishu`、`telegram`、`webchat`）将 `wecom` 替换为对应 channel 即可，例如：

```bash
openclaw agents bind --agent cs-specialist-xiaonuan --bind webchat:xiaonuan
```

## 文件结构（每智能体）

- `AGENTS.md` — **英文**，角色定义、职责、边界、Session Startup、Memory、Red Lines、External vs Internal、Group Chats、Tools、Heartbeats；供 OpenClaw 系统提示词注入
- `zh-CN/AGENTS.md` — **中文**，与 AGENTS.md 内容等价，供团队阅读；整目录 `zh-CN/` 可直接拷贝到业务使用
- `SOUL.md` — 人格与风格、底线（建议在 `zh-CN/` 下提供 SOUL.md 中文版）
- `IDENTITY.md` — **英文**，Who Am I?（Name/Creature/Vibe/Emoji/Avatar，首次对话填写）+ Purpose、When to Invoke、Expertise、Deliverables；模板见 [docs/IDENTITY-template.md](../docs/IDENTITY-template.md)
- `zh-CN/IDENTITY.md` — **中文**，我是谁？+ 职责/何时调用/专长/产出，与 IDENTITY.md 对应；模板见 [docs/zh-CN/IDENTITY-template.md](../docs/zh-CN/IDENTITY-template.md)
- `TOOLS.md` — 本地/环境相关备注（会议室、制度链接等）
- `USER.md` — 所服务对象信息（随使用更新）
- `BOOTSTRAP.md` — 首次运行引导，完成后删除
- `HEARTBEAT.md` — 心跳任务说明（英文）；留空或仅注释即不执行，见 [HEARTBEAT-template](../docs/HEARTBEAT-template.md)
- `zh-CN/HEARTBEAT.md` — 心跳任务说明（中文对照）

**中英文约定：** 所有智能体配置提供**中英文两个独立版本**：英文文件在智能体根目录，中文版集中在 `zh-CN/` 子目录下，文件名与英文一致（`AGENTS.md`、`IDENTITY.md`、`HEARTBEAT.md`、`SOUL.md` 等），便于将 `zh-CN/` 整目录拷贝到业务使用。模板与启发见 [docs/AGENTS-template-inspiration](../docs/AGENTS-template-inspiration.md)、[docs/IDENTITY-template](../docs/IDENTITY-template.md)、[docs/HEARTBEAT-template](../docs/HEARTBEAT-template.md) 及 [docs/zh-CN/](../docs/zh-CN/) 下对应中文版。

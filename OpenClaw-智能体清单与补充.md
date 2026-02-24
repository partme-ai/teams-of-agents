# PartMe Claw — 智能体清单与补充

> 本文档基于 **openclaw-agents** 仓库中各智能体定义，以及《我用 OpenClaw 搞了家 16 人的公司：全员 AI，24 小时无休！》一文的 Squad 与角色建议，对「已有 PartMe.AI 智能体清单」进行**对照**与**补充**，便于配置、路由与扩展。

**参考**：
- 文章：[我用 OpenClaw 搞了家 16 人的公司](https://mp.weixin.qq.com/s/MnVHvx1N497Bq0kz1fRc1w)（总办 + 产品/技术/营销三 Squad、SOUL.md、agentToAgent、飞书多机器人）
- 仓库：`openclaw-agents`（it / game / product / scrm / partner / blog 等）

---

## 1. 已有智能体与 openclaw-agents 对照

下表为「展示名-PartMe.AI」与 openclaw-agents 中 **agent id**、**workspace 来源**、**职责摘要** 的对应关系。配置时以 `agents.list[].id` 为准，展示名可用于 bindings 或前端展示。

| 展示名（已有） | Agent id | 来源目录 / workspace | 职责摘要 |
|----------------|----------|----------------------|----------|
| 移动端-PartMe.AI | `mobile-engineer` | it/partme-mobile-engineer (11-mobile-engineer) | 移动端开发：Native/跨平台、性能、测试、应用商店 |
| 助理-PartMe.AI | `main` | it/partme-main (0-main) | 个人助理：日程、备忘、调研、起草、协调；主编排时作总协调 |
| 游戏主持人-PartMe.AI | `game-master` | game/1-game-master | 游戏主控/主持：整体愿景、工作坊与试玩、编排 game-designer/architect/developer |
| 游戏策划-PartMe.AI | `game-designer` | game/2-game-designer | 游戏策划：玩法、规则、系统、关卡、叙事 |
| 游戏开发-PartMe.AI | `game-developer` | game/4-game-developer | 游戏开发：客户端/服务端/工具实现、代码、性能与集成 |
| 游戏运营-PartMe.AI | `game-ops` | game/5-game-ops | 游戏运营：活动、留存、商业化、版本节奏、KPI 与看板建议 |
| 游戏架构-PartMe.AI | `game-architect` | game/3-game-architect | 游戏架构：整体架构、系统与数据设计 |
| 运维-PartMe.AI | `ops-engineer` 或 `ops` | it/partme-ops-engineer、it/partme-ops | 运维/运维工程师：CI/CD、发布、监控、故障、容量、IaC |
| 测试-PartMe.AI | `qa-engineer` | it/partme-qa-engineer (12-qa-engineer) | 测试：测试策略、用例、自动化、性能测试、缺陷管理 |
| 项目经理-PartMe.AI | `project-manager` | it/partme-project-manager (2-project-manager) | 项目管理：计划、里程碑、资源、风险、复盘 |
| 数据库-PartMe.AI | `database-engineer` | it/partme-database-engineer (9-database-engineer) | 数据库：模型、性能、安全、备份、合规 |
| UED设计-PartMe.AI | `ux-designer` | it/partme-ux-designer (6-ux-designer) | UED：用户研究、信息架构、交互原型、可用性测试 |
| UI 设计-PartMe.AI | `ui-designer` | it/partme-ui-designer (7-ui-designer) | UI：视觉与设计系统、高保真交付、设计评审 |
| 系统架构-PartMe.AI | `system-architect` | it/partme-system-architect (4-system-architect) | 系统架构：架构设计、技术选型、领域/数据架构、ADR |
| 前端-PartMe.AI | `frontend-engineer` | it/partme-frontend-engineer (10-frontend-engineer) | 前端：组件、工程化、性能、无障碍 |
| 后端-PartMe.AI | `backend-engineer` | it/partme-backend-engineer (8-backend-engineer) | 后端：API、服务、数据库设计、消息、缓存、测试 |
| 产品经理-PartMe.AI | `product-manager` | it/partme-product-manager (3-product-manager) | 产品：需求、市场研究、PRD、路线图、优先级与验收 |
| 领域专家-PartMe.AI | `domain-expert` | it/partme-domain-expert (5-domain-expert) | 领域：领域建模、统一语言、业务规则、领域文档 |
| 技术总监-PartMe.AI | `technical-director` | it/partme-technical-director (1-technical-director) | 技术总监：技术战略、架构与选型、效率与质量、编排 it 子智能体 |
| 运营-PartMe.AI | 见 §2 补充 | scrm/0-main 或 product/report-agent 等 | 运营/营销：SCRM 主入口或报表/数据分析，见下文补充 |

**说明**：
- **主编排/总办**：您当前清单中未单独列出。文章建议有一名「总办/CEO」做总协调；openclaw-agents 中 **main**（it/0-main）既可作个人助理，也可在多智能体场景下作为**主编排**（default agent），建议在补充中显式加入，见 §2。
- **游戏运营**：openclaw-agents 的 game 领域仅有 game-master / game-designer / game-architect / game-developer，无专用「游戏运营」；需通过补充新角色或复用「运营-PartMe.AI」覆盖活动、留存、商业化等。

---

## 2. 依据文章与 openclaw-agents 的补充建议

### 2.1 文章中的 16 人结构与建议

文章采用 **Squad 模式**：
- **总办（1 人）**：统筹全局。
- **产品增长队（5 人）**：做啥产品、对留存负责。
- **技术平台队（5 人）**：怎么实现、对稳定性负责。
- **营销增长队（5 人）**：怎么卖、对 MAU/转化负责。

并建议**首批优先**：**CEO（总协调）** + **一名 Squad Lead**（按方向选产品/技术/营销） + **数据分析师**（情报与数据很重要）。

### 2.2 建议补充的智能体

在您已有清单基础上，建议**补充**以下角色（展示名与 id 可依产品命名调整）：

| 补充展示名 | 建议 id | 来源 / 说明 |
|------------|---------|--------------|
| **主编排-PartMe.AI** 或 **总办-PartMe.AI** | `main`（若未单独建总办则与助理共用）或 `ceo` | 对应文章「总办」；openclaw-agents 中 **it/0-main** 为个人助理/主编排，可设 `default: true` 作总协调与任务分发。 |
| **数据分析师-PartMe.AI** | `data-analyst` | 仓库 **it/14-data-analyst** 已提供模板：情报搜集、数据分析、趋势与风险汇总、可视化建议；可与 product/report-agent 协作完成标准化周月报。 |
| **游戏运营-PartMe.AI** | `game-ops` | 仓库 **game/5-game-ops** 已提供模板：活动、留存、商业化、版本节奏；Game Master 编排表中已加入 game-ops，配置见 openclaw-game-fragment.json。 |
| **运营-PartMe.AI**（若尚未落地） | `scrm-orchestrator` 或 `ops-growth` | **scrm/0-main** 为 SCRM/私域主入口；**config/openclaw-scrm-fragment.json** 中有 **scrm-orchestrator**（SCRM 运营编排）。营销增长队 Lead 或「运营」可对应此角色；具体阶段（引流、获客、客资、建联、客服、私域）可再绑 scrm 子角色。 |

### 2.3 可选扩展（来自 openclaw-agents 其他领域）

若希望与仓库其他垂直领域对齐，还可考虑（非必补）：

| 展示名 | Agent id | 来源 | 说明 |
|--------|----------|------|------|
| 博客-PartMe.AI | `blog` | blog/partme-blog | 内容/博客撰写与发布 |
| 陪伴/伙伴-PartMe.AI | `companion` | partner/companion | 陪伴域主入口（如元宝小伴），情感、习惯、目标、故事等 |
| 产品/研发主入口-PartMe.AI | product/0-main | product/0-main | 产品/研发场景总入口，协调 requirement-analyst、report-agent、architect-advisor 等 |
| SCRM 主入口-PartMe.AI | scrm/0-main | scrm/0-main | 私域/CRM 场景总入口，跟进、起草、提醒、合规 |

---

## 3. 配置要点（与文章一致）

- **SOUL.md**：定义每个人格与职责，写清「你是谁、核心职责、性格与原则」；文章认为 SOUL 写得好坏直接决定 Agent 是否好用。
- **agentToAgent**：在 `openclaw.json` 中设置 `tools.agentToAgent.enabled: true`，并在 `allow` 中列出所有需互相委派的 agent id（含 main、technical-director、game-master 及各子角色），这样智能体之间才能自动协作。
- **bindings**：按渠道/飞书应用等将入站请求路由到对应 agent；多机器人时可为每个 Agent 配置独立飞书应用并做 binding。
- **独立记忆**：每个 Agent 独立 workspace 与 session，记忆不共享，便于「各司其职、越用越聪明」。

---

## 4. 补充后的推荐清单（按角色类型）

以下为**补充后**的推荐展示名与 id 一览（仅列出与您业务强相关的部分；博客/陪伴/SCRM 子阶段等按需启用）。

**总办与协调**
- 主编排-PartMe.AI（main）
- 技术总监-PartMe.AI（technical-director）
- 助理-PartMe.AI（可与 main 共用或单独 main-assistant）

**产品与项目**
- 产品经理-PartMe.AI（product-manager）
- 项目经理-PartMe.AI（project-manager）
- 领域专家-PartMe.AI（domain-expert）
- **数据分析师-PartMe.AI**（report-agent / data-analyst）※ 补充

**设计与研发**
- 系统架构-PartMe.AI（system-architect）
- UED设计-PartMe.AI（ux-designer）
- UI 设计-PartMe.AI（ui-designer）
- 后端-PartMe.AI（backend-engineer）
- 前端-PartMe.AI（frontend-engineer）
- 移动端-PartMe.AI（mobile-engineer）
- 数据库-PartMe.AI（database-engineer）

**质量与交付**
- 测试-PartMe.AI（qa-engineer）
- 运维-PartMe.AI（ops-engineer）

**游戏**
- 游戏主持人-PartMe.AI（game-master）
- 游戏策划-PartMe.AI（game-designer）
- 游戏架构-PartMe.AI（game-architect）
- 游戏开发-PartMe.AI（game-developer）
- **游戏运营-PartMe.AI**（game-ops 或复用运营）※ 补充

**运营与增长**
- **运营-PartMe.AI**（scrm-orchestrator 或 SCRM 主 agent）※ 明确对应

以上 id 与 `openclaw-agents` 中 **config/openclaw-agents-fragment.json**、**config/openclaw-it-fragment.json** 及 **config/openclaw-scrm-fragment.json** 中的 `agents.list` 一致或可扩展；合并配置时请将 `<REPO_ROOT>` 替换为实际路径，并确保 `agentToAgent.allow` 包含所有需互调的 agent id。

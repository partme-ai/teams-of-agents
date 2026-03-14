# IT 软件开发团队智能体 (IT Team Agents)

> 技术总监为**编排者（orchestrator）**，可经 agent-to-agent 委派 12 个子角色。基于 [full-stack-skills](https://github.com/partme-ai/full-stack-skills)（优先）与 ClawHub / skills.sh（后补），为**软件开发全链路**提供需求→设计→开发→测试→发布→运维的协同智能体。使用 `config/openclaw-it-fragment.json` 合并 `agents`、`bindings`、`tools.agentToAgent`。

## 技能选型（full-stack-skills 优先，ClawHub / skills.sh 后补）

**技能来源区分：**

| 序号 | 来源 | 说明 | 技能一览文档 | 安装/使用方式 |
|------|------|------|--------------|----------------|
| 1 | **full-stack-skills（优先）** | 本仓库全栈技能库，176+ 技能，覆盖 Vue/React/Spring/UniApp/DDD/测试/运维等 | [IT-SKILLS.md](./IT-SKILLS.md) | 见各技能 `SKILL.md`，workspace 或 Cursor 引用 |
| 2 | **ClawHub** | 社区技能市场 | [IT-SKILLS.md § ClawHub](./IT-SKILLS.md#clawhub-it-相关技能可选) | `clawhub install <slug> --workdir ~/.openclaw` |
| 3 | **skills.sh** | 开源技能聚合 | [IT-SKILLS.md § skills.sh](./IT-SKILLS.md#skillssh-可选) | `npx skills add <owner/repo> --skill <名> -y -g` |

**评估结论摘录：** 完整按角色与环节的推荐技能见 [SKILLS-EVALUATION-IT.md](./SKILLS-EVALUATION-IT.md)。原则：**full-stack-skills 为主**，按角色绑定文档与技能；同能力只保留一个最优技能。

## 智能体清单

| 序号 | Agent id | 展示名（中文） | 目录 | 职责摘要 |
|------|----------|----------------|------|----------|
| 0 | main | 个人助理 | 0-main | 通用个人助理：日程、笔记、调研、起草与协调（可选，非编排链） |
| 1 | technical-director | 技术总监 | 1-technical-director | 编排者：技术战略、架构决策、委派子角色、整合产出 |
| 2 | project-manager | 项目经理 | 2-project-manager | 计划、排期、风险、资源、里程碑、复盘 |
| 3 | product-manager | 产品经理 | 3-product-manager | 需求、市场调研、PRD、路线图、优先级、验收 |
| 4 | system-architect | 系统架构师 | 4-system-architect | 架构设计、技术选型、领域/数据架构、ADR、文档 |
| 5 | domain-expert | 领域专家 | 5-domain-expert | 领域建模、统一语言、业务规则、领域文档 |
| 6 | ux-designer | UED 设计师 | 6-ux-designer | 用户研究、信息架构、交互原型、可用性测试 |
| 7 | ui-designer | UI 设计师 | 7-ui-designer | 视觉与设计系统、高保真交付、设计评审 |
| 8 | backend-engineer | 后端工程师 | 8-backend-engineer | API、服务、数据库设计、消息/缓存、测试 |
| 9 | database-engineer | 数据库工程师 | 9-database-engineer | 模型、性能、安全、备份与灾备、合规 |
| 10 | frontend-engineer | 前端工程师 | 10-frontend-engineer | 组件、构建、性能、可访问性、技术调研 |
| 11 | mobile-engineer | 移动开发工程师 | 11-mobile-engineer | 原生/跨端、性能、测试、应用商店 |
| 12 | qa-engineer | 测试工程师 | 12-qa-engineer | 测试策略、用例、自动化、性能测试、缺陷管理 |
| 13 | ops-engineer | 运维工程师 | 13-ops-engineer | CI/CD、发布、监控、日志、故障、容量、IaC |
| 14 | data-analyst | 数据分析师 | 14-data-analyst | 情报、数据分析、趋势、风险摘要、可视化建议 |

**管线关系：** 技术总监（入口）→ 按任务派发 PM/架构/领域/UX/UI/后端/数据库/前端/移动/QA/运维/数据 → 整合产出 → 可持续交付与复盘。

## 智能工作执行链路

IT 团队按以下链路协同；由技术总监统一入口，按需派发子角色。可按时序触发（如迭代规划）或按需触发单环节。

| 步骤 | 环节 | 智能体 | 输入 | 输出 | 说明 |
|------|------|--------|------|------|------|
| 0 | 需求与规划 | product-manager, project-manager | 业务目标/约束 | PRD、路线图、迭代计划、风险清单 | 入口可选 PM 或技术总监直接拆解 |
| 1 | 架构与领域 | system-architect, domain-expert | PRD、约束 | 架构方案、ADR、领域模型、统一语言 | 技术总监可先派架构再派领域 |
| 2 | 设计 | ux-designer, ui-designer | 需求与架构 | 交互原型、设计系统、高保真稿 | 可并行或串行 |
| 3 | 开发 | backend-engineer, database-engineer, frontend-engineer, mobile-engineer | 设计稿、接口契约、领域模型 | 代码、迁移、API、前端/移动实现 | 多端可并行 |
| 4 | 质量 | qa-engineer | 需求、用例、构建物 | 测试策略、用例、自动化、报告 | 与开发并行或迭代末 |
| 5 | 发布与运维 | ops-engineer | 构建物、环境配置 | CI/CD、发布、监控、故障处理 | 发布后持续运维 |
| 6 | 数据与复盘 | data-analyst | 日志、指标、业务数据 | 趋势、风险摘要、可视化建议、复盘输入 | 可持续或周期执行 |

**闭环：** 数据与复盘的结论反馈至产品与项目，技术总监据此调整优先级与架构；形成「规划 → 架构 → 设计 → 开发 → 测试 → 发布 → 数据 → 反馈」闭环。

**并行与触发：** 设计/开发多角色可并行；技术总监负责拆解与整合。执行顺序由编排者决定，常见为 0 → 1 → 2 → 3 → 4 → 5 → 6；单环节也可独立调用。

## 预设技能（按角色，去重取最优）

以下为 [SKILLS-EVALUATION-IT.md](./SKILLS-EVALUATION-IT.md) 按角色推荐；同能力只选一个来源。config 中 `agents.list[].skills` 填写的为「安装后目录名」或技能名。

| 角色 | Agent id | 推荐技能（示例） | 来源 | 说明 |
|------|----------|------------------|------|------|
| 技术总监 | technical-director | ddd-cola, drawio-architecture, mermaid, documentation-builder | full-stack-skills | 战略与架构表达、文档 |
| 产品经理 | product-manager | doc-coauthoring, full-stack-doc, mermaid | full-stack-skills | PRD、路线图、协作 |
| 系统架构师 | system-architect | ddd-cola, ddd-event-driven, drawio-architecture, spring-cloud, kubernetes | full-stack-skills | 架构、DDD、部署 |
| 领域专家 | domain-expert | ddd-cola, ddd-event-driven, ddd-clean-architecture | full-stack-skills | 领域建模、事件驱动 |
| UX/UI | ux-designer, ui-designer | figma, sketch, frontend-design, ant-design-vue, element-plus-vue3 | full-stack-skills | 原型、设计系统、前端组件 |
| 后端 | backend-engineer | spring-boot, nestjs, fastapi, spring-security, redis | full-stack-skills | 服务、API、安全、缓存 |
| 数据库 | database-engineer | mysql, mongodb, redis, elasticsearch, dbeaver | full-stack-skills | 模型、查询、运维 |
| 前端 | frontend-engineer | vue3, react, vite, pinia, playwright, vitest | full-stack-skills | 框架、构建、测试 |
| 移动 | mobile-engineer | flutter, react-native, uniapp-project, android-kotlin, ios-swift | full-stack-skills | 跨端与原生 |
| QA | qa-engineer | playwright, jest, pytest, junit, appium, detox | full-stack-skills | 自动化与 E2E |
| 运维 | ops-engineer | docker-compose, kubernetes, jenkins, ansible, github-actions | full-stack-skills | CI/CD、编排、IaC |
| 数据 | data-analyst | mermaid, documentation-builder, elasticsearch | full-stack-skills | 报表、可视化建议 |

**安装与绑定：** full-stack-skills 通常通过工作区路径或 Cursor/Claude 技能目录引用；ClawHub/skills.sh 需先安装，再将技能名写入 config 对应 agent 的 `skills` 数组。详见 [IT-SKILLS.md](./IT-SKILLS.md)。

## 文档与技能绑定索引

| 文档 | 用途 | 绑定关系 |
|------|------|----------|
| [README.md](./README.md) | 本入口：智能体清单、流程、技能选型、初始化 | — |
| [IT-SKILLS.md](./IT-SKILLS.md) | IT 技能一览：按角色/环节、full-stack-skills / ClawHub / skills.sh | 各 agent 的 TOOLS.md 可引用 |
| [SKILLS-EVALUATION-IT.md](./SKILLS-EVALUATION-IT.md) | 技能评估结论、按 Agent 推荐技能、安装说明 | 与 README 预设技能表一致 |
| 各 agent 目录下 AGENTS.md / zh-CN/AGENTS.md | 角色定义、职责、边界、Session Startup、Memory、Red Lines、Tools、Heartbeats | OpenClaw 系统提示词注入 |
| 各 agent 目录下 IDENTITY.md / zh-CN/IDENTITY.md | Who Am I / 我是谁；名字、职责、产出、边界 | 与 SOUL.md 一致，供开场与路由 |
| 各 agent 目录下 TOOLS.md | 本地/环境备注；**技能列表及安装命令** | 开发时绑定 ClawHub/skills.sh 技能名 |
| 各 agent 目录下 SOUL.md、BOOTSTRAP.md、HEARTBEAT.md | 人格、首次引导、心跳任务 | 可选，与 xiaohongshu 约定一致 |

**七文件与 zh-CN 一对一约定：** 每个智能体的 7 个标准文件（AGENTS、BOOTSTRAP、HEARTBEAT、IDENTITY、SOUL、TOOLS、USER）与 `zh-CN/` 目录下同名文件为一对一关系；根目录存在的任一文件，必须在 `zh-CN/` 下存在同名中文版。openclaw-agents 下所有智能体（it、content-ops、company 等）均需满足此规范。

**开发所需技能：** 开发或扩展某角色时，先查 [IT-SKILLS.md](./IT-SKILLS.md) 中该角色推荐技能，再查 [SKILLS-EVALUATION-IT.md](./SKILLS-EVALUATION-IT.md) 的安装与冲突说明；最后在该 agent 的 TOOLS.md 中写明已绑定的技能及命令。

## 配置说明

- **Workspace：** 各智能体 workspace 指向本目录下对应子目录（如 `<REPO_ROOT>/openclaw-agents/it/1-technical-director`），或部署时复制/链接到 `~/.openclaw/workspace-technical-director` 等。
- **Config 片段：** 见仓库根目录 `config/openclaw-it-fragment.json`，可合并进主 OpenClaw 配置；使用前将 `~/.openclaw` 替换为实际路径。
- **路由：** 按渠道或用户身份将会话绑定到对应 agent id（默认 telegram、discord 绑定 technical-director）；编排者通过 `tools.agentToAgent` 委派子角色。
- **agentToAgent：** 须设置 `tools.agentToAgent.enabled: true` 并将上述 14 个 id（不含 0-main 若未加入 list）列入 `allow`，编排者方可委派。

## 初始化命令

以下命令在 OpenClaw 配置已就绪的前提下执行；`--workspace` 使用与 agent id 一致的路径，需先将本仓库 `it/<N-xxx>/` 复制或链接到 `~/.openclaw/workspace-<agent-id>`。

### 1. 查看当前智能体列表

```bash
openclaw agents list
```

### 2. 添加 IT 团队智能体（14 个，不含 0-main）

```bash
openclaw agents add technical-director   --workspace ~/.openclaw/workspace-technical-director
openclaw agents add project-manager     --workspace ~/.openclaw/workspace-project-manager
openclaw agents add product-manager     --workspace ~/.openclaw/workspace-product-manager
openclaw agents add system-architect    --workspace ~/.openclaw/workspace-system-architect
openclaw agents add domain-expert       --workspace ~/.openclaw/workspace-domain-expert
openclaw agents add ux-designer          --workspace ~/.openclaw/workspace-ux-designer
openclaw agents add ui-designer         --workspace ~/.openclaw/workspace-ui-designer
openclaw agents add backend-engineer    --workspace ~/.openclaw/workspace-backend-engineer
openclaw agents add database-engineer   --workspace ~/.openclaw/workspace-database-engineer
openclaw agents add frontend-engineer    --workspace ~/.openclaw/workspace-frontend-engineer
openclaw agents add mobile-engineer     --workspace ~/.openclaw/workspace-mobile-engineer
openclaw agents add qa-engineer          --workspace ~/.openclaw/workspace-qa-engineer
openclaw agents add ops-engineer        --workspace ~/.openclaw/workspace-ops-engineer
openclaw agents add data-analyst        --workspace ~/.openclaw/workspace-data-analyst
```

### 3. 查看当前绑定

```bash
openclaw agents bindings
```

### 4. 按渠道绑定智能体（示例）

片段默认将 telegram、discord 路由到 technical-director；若需用 CLI 显式绑定或增加企微等：

```bash
openclaw agents bind --agent technical-director --bind telegram:technical-director
openclaw agents bind --agent technical-director --bind discord:technical-director
openclaw agents bind --agent technical-director --bind wecom:technical-director
```

### 5. 删除 IT 团队智能体（需先解除渠道绑定）

```bash
openclaw agents remove technical-director
openclaw agents remove project-manager
# ... 其余同上
```

## 文件结构（每智能体）

每智能体目录包含以下文件：

| 文件 | 说明 |
|------|------|
| **AGENTS.md** | 英文：角色定义、职责、边界、Session Startup、Memory、Red Lines、Tools、Heartbeats；供 OpenClaw 系统提示词注入（默认英文） |
| **zh-CN/AGENTS.md** | 中文，与根目录 AGENTS.md 内容等价，供中文会话或按语言拷贝 |
| **SOUL.md** | 英文：人格与风格、底线 |
| **zh-CN/SOUL.md** | 中文，与根目录 SOUL.md 内容等价 |
| **IDENTITY.md** | 英文：Who Am I? 名字、职责、产出、边界、简短开场 |
| **zh-CN/IDENTITY.md** | 中文，「我是谁？」与根目录内容等价 |
| **TOOLS.md** | 英文：本地/环境备注；含技能及安装命令 |
| **zh-CN/TOOLS.md** | 中文版（若有），与根目录内容等价 |
| **USER.md** | 英文：所服务对象信息（随使用更新） |
| **zh-CN/USER.md** | 中文，与根目录内容等价 |
| **BOOTSTRAP.md** | 英文：首次运行引导，完成后可删除 |
| **HEARTBEAT.md** / **zh-CN/HEARTBEAT.md** | 心跳任务说明（可选）；根目录为英文 |

**中英文约定：** **根目录为英文**，**zh-CN 子目录为中文**；文件名与两侧一致，便于按语言拷贝。OpenClaw 若默认读取智能体根目录，则注入的为英文提示词；中文会话可读取 zh-CN 下对应文件。

**参考：** 见本目录下任意 agent 的根目录（英文）与 zh-CN（中文）对应文件。

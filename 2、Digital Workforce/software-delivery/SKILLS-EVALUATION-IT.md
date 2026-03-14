# IT 团队智能体技能评估与推荐

> 本报告基于 [full-stack-skills](https://github.com/partme-ai/full-stack-skills) 与可选 ClawHub / skills.sh，按 IT 团队 14 个智能体角色做能力映射与推荐。原则：**full-stack-skills 为主**，按角色绑定文档与技能；同能力只保留一个最优技能。

## 一、评估原则

- **优先 full-stack-skills：** 与 openclaw-agents 同工作空间，维护一致，覆盖全栈与架构、测试、运维。
- **ClawHub / skills.sh 后补：** 当 full-stack-skills 未覆盖某能力（如某云厂商、某小众框架）时再选用。
- **同能力只装一个：** 例如架构图优先 mermaid + drawio-architecture，不重复装多套同质技能。

## 二、按 Agent 的推荐技能表

下表为按角色给出的**最终推荐技能**（技能名为 full-stack-skills 内名称或 ClawHub slug / skills.sh 技能名）；与 [README.md 预设技能表](./README.md#预设技能按角色去重取最优) 一致。

| Agent id | 推荐技能（首选） | 来源 | 说明 |
|----------|------------------|------|------|
| technical-director | ddd-cola, drawio-architecture, mermaid, documentation-builder, full-stack-doc | full-stack-skills | 战略与架构表达、文档 |
| project-manager | doc-coauthoring, full-stack-doc, mermaid, processon-mindmap | full-stack-skills | 计划、复盘、文档协作 |
| product-manager | doc-coauthoring, full-stack-doc, mermaid, api-doc-generator | full-stack-skills | PRD、路线图、接口契约 |
| system-architect | ddd-cola, ddd-event-driven, drawio-architecture, spring-cloud, kubernetes, docker-compose, mermaid | full-stack-skills | 架构、DDD、部署 |
| domain-expert | ddd-cola, ddd-event-driven, ddd-clean-architecture | full-stack-skills | 领域建模、事件驱动 |
| ux-designer | figma, sketch, axure, modao, frontend-design | full-stack-skills | 原型、用户研究、前端设计 |
| ui-designer | figma, sketch, adobe-xd, frontend-design, element-plus-vue3, ant-design-vue | full-stack-skills | 视觉、设计系统、组件 |
| backend-engineer | spring-boot, nestjs, fastapi, spring-security, redis, api-doc-generator | full-stack-skills | 服务、API、安全、缓存 |
| database-engineer | mysql, mongodb, redis, elasticsearch, dbeaver, navicat | full-stack-skills | 模型、查询、运维 |
| frontend-engineer | vue3, react, vite, pinia, playwright, vitest, element-plus-vue3 | full-stack-skills | 框架、构建、测试、组件 |
| mobile-engineer | flutter, react-native, uniapp-project, android-kotlin, ios-swift, uview-pro-vue3 | full-stack-skills | 跨端与原生、UniApp |
| qa-engineer | playwright, jest, vitest, pytest, junit, appium, detox, test-writer | full-stack-skills | 自动化与 E2E、测试编写 |
| ops-engineer | docker-compose, kubernetes, jenkins, github-actions, ansible | full-stack-skills | CI/CD、编排、IaC |
| data-analyst | mermaid, documentation-builder, full-stack-doc, elasticsearch | full-stack-skills | 报表、可视化建议、检索 |

## 三、安装与 config 绑定

### 3.1 full-stack-skills（推荐方式）

- **方式一：** 在 Cursor / Claude Code 中安装 full-stack-skills 插件，并按需选择插件类别（如 development-skills、architecture-skills、testing-skills）。无需在 OpenClaw 的 `agents.list[].skills` 中逐条填写。
- **方式二：** 将 full-stack-skills 仓库克隆到工作空间，在各 agent 的 **TOOLS.md** 中写明该角色推荐技能的 `SKILL.md` 相对路径（如 `../../full-stack-skills/skills/ddd-cola/SKILL.md`），供开发与 AI 直接阅读。

### 3.2 ClawHub（可选）

- 搜索：<https://clawhub.ai> 按关键词（如 spring、vue、testing）搜索。
- 安装：`clawhub install <slug> --workdir ~/.openclaw`
- Config：将 `<slug>` 填入 `config/openclaw-it-fragment.json` 中对应 agent 的 `skills` 数组。
- 前置：需先安装 [SkillHub CLI](https://clawhub.ai)（若尚未安装）。

### 3.3 skills.sh（可选）

- 搜索：<https://skills.sh> 按关键词搜索。
- 安装：`npx skills add <owner/repo> --skill <技能名> -y -g`
- Config：将安装后的**技能名**（与目录名一致）填入对应 agent 的 `skills` 数组。

## 四、各 Agent TOOLS.md 建议内容

每个智能体目录下的 **TOOLS.md** 建议包含：

1. **本角色推荐技能列表**（从上表或 [IT-SKILLS.md](./IT-SKILLS.md) 复制）。
2. **full-stack-skills 引用方式**：插件安装命令或 SKILL.md 路径。
3. **若使用 ClawHub / skills.sh：** 该 agent 已绑定的技能名及安装命令（便于复现与环境一致）。
4. **本地/环境备注**：如输出路径、环境变量、内部 API 等（不写密钥）。

这样既满足「文档绑定」，又满足「开发所需技能」的集中查阅与运维复现。

## 五、与 content-ops/xiaohongshu 的对照

| 项目 | xiaohongshu | it |
|------|-------------|-----|
| 技能主来源 | ClawHub + skills.sh (Baoyu) | full-stack-skills + 可选 ClawHub/skills.sh |
| 技能一览文档 | CLAWHUB-SKILLS.md, SKILLS-SH-SKILLS.md | IT-SKILLS.md |
| 评估文档 | SKILLS-EVALUATION.md | SKILLS-EVALUATION-IT.md |
| 流程定义 | README 智能工作执行链路 | README 智能工作执行链路 |
| 文档绑定 | README 文件结构 + 各 agent 文件 | README 文档与技能绑定索引 + 各 agent 文件 |
| 中英文配置 | AGENTS.md / zh-CN/AGENTS.md, IDENTITY 等 | 同结构，见 README 文件结构 |

开发或扩展 IT 智能体时，按 README → IT-SKILLS.md → SKILLS-EVALUATION-IT.md → 各 agent TOOLS.md 顺序查阅即可获得「绑定文档」与「开发所需技能」的完整信息。

# IT 软件开发团队技能一览

> 本目录智能体以 [full-stack-skills](https://github.com/partme-ai/full-stack-skills)（优先）为技能主来源，ClawHub / skills.sh 为可选后补。安装与绑定方式见 [SKILLS-EVALUATION-IT.md](./SKILLS-EVALUATION-IT.md)。

## 一、技能来源与使用方式

| 来源 | 说明 | 使用方式 |
|------|------|----------|
| **full-stack-skills** | 本工作空间全栈技能库，12 类插件、176+ 技能 | 通过 Cursor/Claude 插件或工作区路径引用；各技能见 `full-stack-skills/skills/<技能名>/SKILL.md` |
| **ClawHub** | 社区技能市场 | `clawhub install <slug> --workdir ~/.openclaw`；安装后目录名填入 config `agents.list[].skills` |
| **skills.sh** | 开源技能聚合 | `npx skills add <owner/repo> --skill <名> -y -g`；技能名与 config 一致 |

## 二、按 IT 角色与环节映射（full-stack-skills）

下表按智能体角色列出推荐技能（均为 full-stack-skills 内技能名）；同能力只列一个首选。

### 2.1 技术总监 / 编排者 (technical-director)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| 架构表达与决策 | ddd-cola, ddd-event-driven, drawio-architecture | architecture-skills, document-skills |
| 文档与图表 | mermaid, documentation-builder, full-stack-doc | document-skills, development-skills-utils |
| 战略与路线图 | doc-coauthoring, processon-mindmap | document-skills |

### 2.2 产品经理 (product-manager)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| PRD、路线图、协作 | doc-coauthoring, full-stack-doc, mermaid | document-skills, development-skills-utils |
| 需求与验收 | api-doc-generator（接口契约） | document-skills |

### 2.3 系统架构师 (system-architect)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| DDD 与架构模式 | ddd-cola, ddd-event-driven, ddd-clean-architecture, drawio-architecture | architecture-skills |
| 微服务与部署 | spring-cloud, kubernetes, docker-compose | development-skills, devops-skills |
| 文档 | mermaid, documentation-builder | document-skills |

### 2.4 领域专家 (domain-expert)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| 领域建模与事件驱动 | ddd-cola, ddd-event-driven, ddd-clean-architecture | architecture-skills |

### 2.5 UX / UI 设计师 (ux-designer, ui-designer)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| 原型与设计工具 | figma, sketch, adobe-xd, axure, modao, framer | design-skills |
| 前端设计与组件 | frontend-design, ant-design-vue, element-plus-vue3, vant-vue3, uview-pro-vue3 | development-skills-utils, development-skills |

### 2.6 后端工程师 (backend-engineer)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| Java 生态 | spring-boot, spring-cloud, spring-security, redis | development-skills |
| Node 生态 | nestjs, express, koa, fastify | development-skills |
| Python 生态 | django, fastapi | development-skills |
| Go 生态 | gin | development-skills |
| 文档与 API | api-doc-generator, documentation-builder | document-skills, development-skills-utils |

### 2.7 数据库工程师 (database-engineer)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| 关系型 / NoSQL / 搜索 | mysql, mongodb, redis, elasticsearch, oracle, postgresql | database-skills |
| 管理工具 | navicat, dbeaver | database-skills |

### 2.8 前端工程师 (frontend-engineer)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| 框架与构建 | vue3, react, vite, nextjs, pinia, webpack, rollup | development-skills |
| UI 组件库 | element-plus-vue3, ant-design-vue, vant-vue3, ant-design-react | development-skills |
| 测试 | playwright, vitest, jest | testing-skills |
| 设计协作 | frontend-design | development-skills-utils |

### 2.9 移动开发工程师 (mobile-engineer)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| 跨平台 | flutter, react-native, uniapp-project, uniappx-project | development-skills |
| 原生 | android-kotlin, ios-swift | development-skills |
| UniApp 生态 | uniapp-uview, uniapp-ucharts, uview-pro-vue3 | development-skills |

### 2.10 测试工程师 (qa-engineer)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| 单元测试 | jest, vitest, pytest, junit | testing-skills |
| E2E | playwright, cypress, selenium | testing-skills |
| 移动端测试 | appium, detox | testing-skills |
| 测试编写 | test-writer, webapp-testing | development-skills-utils |

### 2.11 运维工程师 (ops-engineer)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| CI/CD | jenkins, gitlab-ci, github-actions | devops-skills |
| 容器与编排 | docker, docker-compose, kubernetes | devops-skills |
| IaC | ansible, terraform, cloudformation | devops-skills |

### 2.12 数据分析师 (data-analyst)

| 能力 | 推荐技能 | 插件类别 |
|------|----------|----------|
| 图表与文档 | mermaid, documentation-builder, full-stack-doc | document-skills, development-skills-utils |
| 数据与检索 | elasticsearch, redis | database-skills |

## 三、full-stack-skills 插件类别与安装

| 插件类别 | 安装命令（示例） | 技能数量 | 适用 IT 角色 |
|----------|------------------|----------|--------------|
| development-skills | `/plugin install development-skills@full-stack-skills` | 76 | 后端、前端、移动、架构 |
| development-skills-utils | `/plugin install development-skills-utils@full-stack-skills` | 13 | 全角色（文档、测试、设计） |
| design-skills | `/plugin install design-skills@full-stack-skills` | 16 | UX/UI |
| document-skills | `/plugin install document-skills@full-stack-skills` | 15 | 产品、架构、数据 |
| architecture-skills | `/plugin install architecture-skills@full-stack-skills` | 7 | 架构、领域 |
| testing-skills | `/plugin install testing-skills@full-stack-skills` | 9 | QA、前端 |
| devops-skills | `/plugin install devops-skills@full-stack-skills` | 9 | 运维、架构 |
| database-skills | `/plugin install database-skills@full-stack-skills` | 8 | 数据库、后端、数据 |
| cloud-skills | `/plugin install cloud-skills@full-stack-skills` | 16 | 运维、架构 |

具体以 [full-stack-skills/README.md](https://github.com/partme-ai/full-stack-skills) 为准。

## 四、ClawHub IT 相关技能（可选）

若需从 ClawHub 补充（如代码生成、安全扫描、项目管理等），可在 [ClawHub](https://clawhub.ai) 搜索 `spring`、`vue`、`testing`、`devops`、`ddd` 等关键词，按评分与下载量选用。安装：`clawhub install <slug> --workdir ~/.openclaw`。安装后 slug 作为技能名填入对应 agent 的 `skills` 数组。

## 五、skills.sh 前端技能（前端智能体可选）

[skills.sh 按 frontend 搜索](https://skills.sh/?q=frontend) 后，以下技能可作为**前端智能体（frontend-engineer）**的补充；与 full-stack-skills 同能力可二选一或并存。

| 序号 | 技能名 | 仓库 | 安装量 | 用途 |
|------|--------|------|--------|------|
| 1 | frontend-design | anthropics/skills | 152.9K | 前端设计与高质量 UI |
| 2 | frontend-design-system | supercent-io/skills-template | 7.7K | 设计系统与组件规范 |
| 3 | frontend-code-review | langgenius/dify | 2.4K | 前端代码评审 |
| 4 | frontend-patterns | affaan-m/everything-claude-code | 2.0K | 前端模式与最佳实践 |
| 5 | frontend-design | jwynia/agent-skills | 1.5K | 前端设计（同名另一源） |
| 6 | frontend-testing | langgenius/dify | 1.4K | 前端测试 |
| 7 | frontend-testing-best-practices | sergiodxa/agent-skills | 1.4K | 前端测试最佳实践 |
| 8 | frontend responsive design standards | am-will/codex-skills | 1.2K | 响应式设计标准 |
| 9 | vercel-microfrontends | vercel/microfrontends | 21 | 微前端（Vercel） |
| 10 | frontend-ui-ux-engineer | 404kidwiz/claude-supercode-skills | 1.0K | 前端 UI/UX 工程 |

**安装命令（skills.sh）：** `npx skills add <owner/repo> --skill <技能名> -y -g`。示例：

```bash
# 首选：anthropics/skills 的 frontend-design（安装量最高）
npx skills add anthropics/skills --skill frontend-design -y -g
# 设计系统
npx skills add supercent-io/skills-template --skill frontend-design-system -y -g
# 前端测试最佳实践
npx skills add sergiodxa/agent-skills --skill frontend-testing-best-practices -y -g
# 前端模式
npx skills add affaan-m/everything-claude-code --skill frontend-patterns -y -g
```

同质能力（如两个 frontend-design）只装一个时优先选 anthropics/skills。

## 六、skills.sh 其它可选

若需从 skills.sh 补充非前端类技能（如 TDD、API 设计、Spring Boot 等），可在 [skills.sh](https://skills.sh) 搜索后使用 `npx skills add <owner/repo> --skill <名> -y -g` 安装。技能名与 config 中 `skills` 一致。

## 七、与智能体的绑定方式

- **full-stack-skills：** 通过 Cursor/Claude 插件或工作区配置引用整库或按插件类别安装；无需在 OpenClaw config 的 `agents.list[].skills` 中逐条填写，但可在各 agent 的 **TOOLS.md** 中列出该角色推荐技能及 SKILL.md 路径，便于开发与 AI 查阅。
- **ClawHub / skills.sh：** 安装后目录名（或技能名）写入 `config/openclaw-it-fragment.json` 中对应 agent 的 `skills` 数组；同时在该 agent 的 **TOOLS.md** 中注明已绑定技能及安装命令，便于运维与复现。

**开发所需技能查阅顺序：** README → IT-SKILLS.md（本节）→ SKILLS-EVALUATION-IT.md（按 Agent 推荐与安装）→ 各 agent 的 TOOLS.md。

**前端智能体专项：** 见上文 § 五、skills.sh 前端技能；本地备注与安装命令见 [10-frontend-engineer/TOOLS.md](./10-frontend-engineer/TOOLS.md)。

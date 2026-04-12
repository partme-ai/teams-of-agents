# Claw Agents

面向 `OctoClaw / OpenClaw` 生态的智能体工作区仓库，提供可直接复用的角色定义、领域编排方案、渠道运营管线和技能选型文档。

当前仓库的一级目录与 [agency-agents](https://github.com/msitarzewski/agency-agents) 的智能体分类对齐（如 `engineering/`、`marketing/`、`specialized/` 等）。与 The Agency roster 对应的角色位于相应分类下；PartMe 独有或渠道编排类资产集中在 `specialized/partme/`（含原 IM 渠道说明、内容运营各平台 README/技能索引、交付域遗留文档等）。

> `OctoClaw` 强调零信任、流式执行、边说边执行与企业级安全；本仓库中的智能体定义与技能文档可直接作为 `OctoClaw` 的业务工作区内容，也兼容 OpenClaw 式工作区组织方式。  
> 参考：`../octoclaw/README.md`、`../octoclaw/README_CN.md`

---

## 目录

1. [仓库现状总览](#1-仓库现状总览)
2. [推荐安装方式](#2-推荐安装方式)
3. [快速接入一个智能体组](#3-快速接入一个智能体组)
4. [分类与代表性智能体](#4-分类与代表性智能体)
5. [技能体系与安装策略](#5-技能体系与安装策略)
6. [智能体文档规范](#6-智能体文档规范)
7. [配置与部署建议](#7-配置与部署建议)
8. [常见落地场景](#8-常见落地场景)
9. [文档入口](#9-文档入口)

---

## 1. 仓库现状总览

### 顶层结构

```text
claw-agents/
├── academic/
├── design/
├── engineering/
├── game-development/
├── marketing/
├── paid-media/
├── product/
├── project-management/
├── sales/
├── spatial-computing/
├── specialized/
│   └── partme/          # PartMe 独有智能体 + 原三大分组遗留文档（渠道 README、技能索引等）
├── strategy/
├── support/
├── testing/
├── config/
├── docs/
└── scripts/
```

### 分类说明

| 类型 | 说明 |
|------|------|
| 与 Agency roster 对齐的一级目录 | 名称与 `research/agency-agents` 中分类一致；标准角色目录名为 kebab-case slug（如 `marketing/douyin-strategist`）。OpenClaw 转换稿中的 `AGENTS.md` / `IDENTITY.md` / `SOUL.md` 已与源目录对齐合并。 |
| `specialized/partme/` | 非 roster 或需保留原路径语义的资产（如 `im-channels/`、`content-ops/`、`digital-workforce-legacy/`）；若曾与 roster 目录重名，副本在 `specialized/partme/roster-collision/` 下可追溯。 |

### 迁移说明

- 批量迁移由 `scripts/migrate_to_agency_layout.py` 完成（可 `--dry-run` 预览）。
- 历史文档若仍出现 `1、IM Channels` 等旧路径，请以当前仓库实际目录为准。

---

## 2. 推荐安装方式

### 2.1 运行时安装

本仓库推荐优先面向 `OctoClaw` 使用；若你当前仍运行 `OpenClaw` 风格工作区，也可以沿用相同的工作区组织方式。

**OctoClaw（推荐，适合企业级流式执行）**

```bash
git clone https://github.com/octoclaw-labs/octoclaw.git
cd octoclaw
cargo build --release
cargo run -p octoclaw-cli -- chat
```

**配置目录**

- OctoClaw：`~/.octoclaw/config.toml`
- OpenClaw 兼容式工作区：通常仍会使用 `~/.openclaw/...` 的 workspace / agentDir 组织

OctoClaw 的能力与定位见 `../octoclaw/README_CN.md`。

### 2.2 技能安装 CLI

本仓库默认采用“双来源”技能策略：

1. `ClawHub / SkillHub` 优先
2. `skills.sh` 后补

国内环境推荐先装 SkillHub CLI：

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

安装完成后可使用：

```bash
skillhub install <slug>
```

如果你直接使用 ClawHub：

```bash
clawhub install <slug> --workdir ~/.openclaw;
```

如果你使用 skills.sh：

```bash
npx skills add <owner/repo> --skill <skill-name> -y -g;
```

### 2.3 技能目录要点

技能安装目录必须与你的运行时加载目录一致：

| 类型 | 典型路径 |
|------|----------|
| 全局技能 | `~/.openclaw/skills/` |
| 工作区技能 | `<workspace>/.openclaw/skills/` |

`npx skills add` 默认安装位置与 OpenClaw/OctoClaw 工作区未必一致，因此：

- 能用 `clawhub install` / `skillhub install` 时，优先用它们
- 若用 `npx skills add`，需将技能复制或软链到实际技能目录

更完整说明见 `docs/SKILLS-MASTER.md`。

---

## 3. 快速接入一个智能体组

### 方式一：直接复用仓库目录作为工作区模板

1. 选择一个目录，例如：
   - `specialized/partme/software-delivery/`（原 Software & Delivery 文档与 PartMe 角色）
   - `specialized/partme/web3/`
   - `specialized/partme/content-ops/xiaohongshu/`
2. 将目标角色目录复制或软链到实际运行时工作区
3. 在运行时配置中注册 `agentId`、`workspace`、`agentDir`
4. 按需启用绑定与 agent-to-agent 委派

### 方式二：以本仓库为“定义源”，由运行时生成 agent 再覆盖工作区

如果你已有现成 agent 管理命令，可先创建 agent，再用本仓库内容覆盖工作区目录：

```bash
mkdir -p ~/.openclaw/workspace-technical-director
mkdir -p ~/.openclaw/agents/technical-director/agent
mkdir -p ~/.openclaw/agents/technical-director/sessions
```

然后把仓库中的角色定义复制进去：

```bash
cp -R "/path/to/claw-agents/specialized/partme/software-delivery/1-technical-director/"* \
  ~/.openclaw/workspace-technical-director/
```

### 最小配置示例

```json5
{
  "agents": {
    "list": [
      {
        "id": "technical-director",
        "default": true,
        "workspace": "~/.openclaw/workspace-technical-director",
        "agentDir": "~/.openclaw/agents/technical-director/agent"
      }
    ]
  }
}
```

### 验证建议

```bash
openclaw agents list --bindings
openclaw channels status --probe
openclaw doctor
```

如果你使用 OctoClaw，则按其 CLI / config 模型完成等价注册，核心原则不变：

- 每个 agent 独立工作区
- 每个 agent 独立状态目录
- 技能目录与运行时加载目录一致
- 高风险发布/写操作默认加人工确认

---

## 4. 分类与代表性智能体

### 4.1 与 Agency 对齐的示例路径

- 工程与交付：`engineering/frontend-developer`、`engineering/backend-architect`、`engineering/code-reviewer`
- 增长与内容：`marketing/douyin-strategist`、`marketing/xiaohongshu-specialist`、`marketing/zhihu-strategist`
- 游戏与媒体：`game-development/unity-architect`、`game-development/godot-gameplay-scripter`
- 销售与投放：`sales/outbound-strategist`、`paid-media/ppc-campaign-strategist`

### 4.2 PartMe 扩展（`specialized/partme/`）

- **IM 渠道智能体与说明**：`specialized/partme/im-channels/discord/`、`telegram/` 等
- **内容运营渠道索引**：`specialized/partme/content-ops/douyin/`、`xiaohongshu/` 等（各平台 `README.md`、`CLAWHUB-SKILLS.md` 等）
- **交付与 Web3 等**：`specialized/partme/software-delivery/`、`specialized/partme/web3/`；完整树见 `specialized/partme/digital-workforce-legacy/`

---

## 5. 技能体系与安装策略

### 5.1 仓库里的技能文档分层

**根级总览**

- `docs/SKILLS-MASTER.md`：全仓库总技能索引、安装目录说明、Baoyu 技能总表

**分组级 README**

- `specialized/partme/im-channels/README.md`
- `specialized/partme/digital-workforce-legacy/README.md`
- `specialized/partme/content-ops/README.md`

**渠道/领域级技能文档**

多数成熟子域都包含以下文件：

- `README.md`
- `CLAWHUB-SKILLS.md`
- `SKILLS-SH-SKILLS.md`
- `SKILLS-EVALUATION.md`

例如：

- `specialized/partme/content-ops/xiaohongshu/README.md`
- `specialized/partme/content-ops/xiaohongshu/CLAWHUB-SKILLS.md`
- `specialized/partme/content-ops/xiaohongshu/SKILLS-SH-SKILLS.md`
- `specialized/partme/content-ops/xiaohongshu/SKILLS-EVALUATION.md`

软件交付子域则有单独口径：

- `specialized/partme/software-delivery/README.md`（及同目录下 `IT-SKILLS.md`、`SKILLS-EVALUATION-IT.md`）

### 5.2 统一选型原则

本仓库推荐的统一规则是：

1. 先看 `ClawHub / SkillHub` 是否已有高质量平台专用技能
2. 再用 `skills.sh` 和 `Baoyu` 技能补齐格式化、抓取、配图、压缩、发布等通用能力
3. 同能力优先只保留一个最优技能，避免重复安装

### 5.3 Content Ops 的标准技能心智模型

以内容平台为例，一个完整渠道通常会用到这些技能类型：

| 能力层 | 常见用途 | 典型来源 |
|--------|----------|----------|
| 平台连接 | 搜索、发布、评论、账号操作 | ClawHub / SkillHub |
| 抓取转换 | URL 转 Markdown、正文提取 | skills.sh / Baoyu |
| 格式输出 | 日报、拆解报告、结构化 Markdown | skills.sh / Baoyu |
| 配图生成 | 封面、插图、信息图、漫画 | skills.sh / Baoyu |
| 发布前处理 | 图片压缩、HTML 转换 | skills.sh / Baoyu |
| 数据复盘 | 报告生成、趋势周报 | 平台技能 + Markdown 格式技能 |

### 5.4 常用 Baoyu 技能

根文档无需逐条展开所有安装命令，但你应优先知道这些是跨渠道高频基础设施：

- `baoyu-url-to-markdown`
- `baoyu-format-markdown`
- `baoyu-cover-image`
- `baoyu-article-illustrator`
- `baoyu-xhs-images`
- `baoyu-compress-image`
- `baoyu-markdown-to-html`
- `baoyu-post-to-wechat`
- `baoyu-post-to-x`
- `baoyu-translate`

完整表与安装说明见 `docs/SKILLS-MASTER.md`。

---

## 6. 智能体文档规范

本仓库当前以“七文件 + `zh-CN` 镜像”作为主规范。

### 标准文件集

```text
<agent-dir>/
├── AGENTS.md
├── BOOTSTRAP.md
├── HEARTBEAT.md
├── IDENTITY.md
├── SOUL.md
├── TOOLS.md
├── USER.md
└── zh-CN/
    ├── AGENTS.md
    ├── BOOTSTRAP.md
    ├── HEARTBEAT.md
    ├── IDENTITY.md
    ├── SOUL.md
    ├── TOOLS.md
    └── USER.md
```

### 各文件职责

| 文件 | 作用 |
|------|------|
| `AGENTS.md` | 角色定义、边界、行为准则、委派关系 |
| `SOUL.md` | 个性、语气、价值观、沟通风格 |
| `IDENTITY.md` | 身份卡、自我介绍、适用场景 |
| `TOOLS.md` | 本角色可调用的工具、交付物、工作流 |
| `USER.md` | 目标用户与服务对象信息 |
| `BOOTSTRAP.md` | 首次启动说明、初始化任务 |
| `HEARTBEAT.md` | 周期性任务、巡检与主动动作 |

### 中英文约定

- 英文文件用于运行时注入或作为主定义
- `zh-CN/` 用于团队阅读、业务交付和本地运营维护
- 新建或补齐智能体时，建议保持中英双份同步

---

## 7. 配置与部署建议

### 工作区映射原则

无论使用 OctoClaw 还是 OpenClaw 式工作区，都建议遵循：

- 每个 agent 一个独立 workspace
- 每个 agent 一个独立 `agentDir`
- 会话目录独立
- 技能目录与实际加载路径一致

### 多智能体部署建议

如果你要部署一个“团队”而不是单个角色：

- 为入口角色配置 `default: true`
- 通过 `bindings` 将渠道入口路由给入口角色
- 通过 `agent-to-agent` 仅开放必要的子角色
- 对发布、外呼、评论回复等写操作增加审批门禁

### 端口与隔离

如果你在一台机器上部署多组智能体：

- 配置文件隔离
- 状态目录隔离
- 工作区隔离
- 端口隔离
- 浏览器 / CDP / Canvas 派生端口避免重叠

这一点与旧版 OpenClaw 多网关原则一致，在 OctoClaw 场景下同样成立。

---

## 8. 常见落地场景

### 软件研发团队

推荐从 `specialized/partme/software-delivery/`（及 `engineering/` 等 roster 角色）开始，使用：

- `technical-director` 作为入口编排者
- 项目、产品、架构、前后端、测试、运维为执行角色
- `code-reviewer`、`backend-architect` 等作为增强专家

### 内容运营团队

推荐从 `specialized/partme/content-ops/<channel>` 开始，按渠道部署七件套：

- 先部署监控、拆解、原创/二创、发布
- 再加数据助手与评论管理
- 技能先从该渠道 `README.md` 与 `SKILLS-EVALUATION.md` 中选型

### 社群与 IM 运营

推荐从 `specialized/partme/im-channels/<channel>` 开始，按 Bot 开发、社区运营、支持响应拆分角色。

---

## 9. 文档入口

### 推荐阅读顺序

1. `docs/README.md`
2. `docs/SKILLS-MASTER.md`
3. 分组 README
4. 具体子域 `README.md`
5. `CLAWHUB-SKILLS.md` / `SKILLS-SH-SKILLS.md` / `SKILLS-EVALUATION*.md`

### 快速入口

- 总技能索引：`docs/SKILLS-MASTER.md`
- IM 渠道总览：`specialized/partme/im-channels/README.md`
- 数字员工总览：`specialized/partme/digital-workforce-legacy/README.md`
- 内容运营总览：`specialized/partme/content-ops/README.md`
- 小红书完整样板：`specialized/partme/content-ops/xiaohongshu/README.md`

---

**最后更新**：2026-04-12

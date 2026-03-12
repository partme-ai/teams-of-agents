# 公众号文章生产管线 (WeChat Article Agents)

> 基于 [ClawHub wechat 技能](https://clawhub.ai/skills?sort=downloads&q=wechat) 与 [skills.sh wechat](https://skills.sh/?q=wechat)（**以 ClawHub 为主，两源取最优**），为**微信公众号文章**提供统一内容管线七件套：热门监控、爆款拆解、二创、写作、自动发布、数据助手、评论管理。与 openclaw-agents 其他领域（company / discord / telegram 等）并列。

## 技能来源区分

| 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|----------|--------------|----------|
| **ClawHub（为主）** | [clawhub.ai/skills?q=wechat](https://clawhub.ai/skills?sort=downloads&q=wechat) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug>` |
| **skills.sh（取最优）** | [skills.sh/?q=wechat](https://skills.sh/?q=wechat) | 见下方技能表与安装方式 | `npx skills add <owner/repo> --skill <名>` |

## 必须保证的七个环节

1. **热门监控**：每日/按需搜索公众号/微信生态行业热点与爆款文章，产出日报或摘要，供爆款拆解与数据助手使用。
2. **爆款拆解**：自动搜索平台关于行业热点和爆款文章，产出结构化拆解框架（标题/钩子/结构/主题等），供二创与数据助手使用。
3. **二创**：根据拆解框架和结合主题进行新文案和配图（封面 + 文中插图），产出草稿供发布与数据助手使用。
4. **写作**：强调原创；用户主图+热点/爆款做原创文章，产出草稿供发布与数据助手。
5. **自动发布**：将已通过的草稿发布到微信公众号（文章/贴图），并记录发布结果供数据助手分析。
6. **数据助手**：解析文案数据、主题方向，交叉验证效果，将可执行结论反馈给爆款拆解，用于修正和提升（形成闭环）。
7. **评论管理**：评论采集、起草回复、情感分析；回复需审批/门禁后发布。

**管线关系：** 热门监控 → 日报/摘要 → 爆款拆解 → 拆解框架 → 二创/写作 → 草稿+配图 → 自动发布 → 发布日志 → 数据助手 + 评论管理 → 反馈至爆款拆解与热门监控。

## 智能体清单

| 序号 | Agent id                        | 展示名           | 目录                               | 职责摘要 |
|------|---------------------------------|------------------|------------------------------------|----------|
| 1    | wechat-article-hot-monitor      | 公众号热门监控   | 1-wechat-article-hot-monitor      | 每日/按需搜索公众号/微信生态热点与爆款，产出日报或摘要供拆解与数据助手 |
| 2    | wechat-article-viral-breakdown | 公众号爆款拆解   | 2-wechat-article-viral-breakdown  | 自动搜索行业热点与爆款文章，产出结构化拆解框架 |
| 3    | wechat-article-rewrite          | 公众号二创       | 3-wechat-article-rewrite          | 根据拆解框架与主题创作新文案与封面/文中插图 |
| 4    | wechat-article-write            | 公众号写作       | 4-wechat-article-write            | 强调原创：用户主图+热点/爆款做原创文章，产出草稿供发布与数据助手 |
| 5    | wechat-article-publisher        | 公众号自动发布   | 5-wechat-article-publisher        | 将已通过草稿发布到公众号并记录结果 |
| 6    | wechat-article-data-assistant   | 公众号数据助手   | 6-wechat-article-data-assistant   | 解析数据、交叉验证效果、可执行反馈给爆款拆解 |
| 7    | wechat-article-comment-manager  | 公众号评论管理   | 7-wechat-article-comment-manager  | 评论采集、起草回复、情感分析；回复需审批/门禁后发布 |

## 智能工作执行链路

七件套按以下链路协同执行；可按时序触发（如每日）或按需触发单环节。

| 步骤 | 环节 | 智能体 | 输入 | 输出 | 说明 |
|------|------|--------|------|------|------|
| 1 | 热门监控 | wechat-article-hot-monitor | 关键词/品类/时间范围 | 日报或按需摘要（热点、爆款列表） | 入口；可为定时或人工触发 |
| 2 | 爆款拆解 | wechat-article-viral-breakdown | 日报/摘要中的爆款链接或列表 | 拆解框架（标题、钩子、结构、主题） | 消费监控产出，供二创与数据侧使用 |
| 3a | 二创 | wechat-article-rewrite | 拆解框架 + 主题 | 草稿（文案 + 封面 + 配图） | 基于拆解做差异化二创，不发布 |
| 3b | 写作 | wechat-article-write | 用户选题 + 热点/爆款洞察 | 草稿（文案 + 封面 + 配图） | 独立于拆解的原创内容生产 |
| 4 | 自动发布 | wechat-article-publisher | 已审核草稿 | 发布结果日志（链接、时间、状态） | 仅发布已通过审核内容；发布前压缩图片 |
| 5 | 数据助手 | wechat-article-data-assistant | 发布日志 + 互动数据 | 可执行反馈（关键词/拆解维度/优先主题） | 交叉验证效果，反馈至爆款拆解与监控 |
| 6 | 评论管理 | wechat-article-comment-manager | 文章/账号评论源 | 回复草稿 + 情感摘要 | 回复须审批/门禁后由人工或流程发布 |

**闭环：** 数据助手的反馈驱动爆款拆解调整搜索与拆解标准，热门监控可据此调整关键词与范围，形成「监控 → 拆解 → 内容 → 发布 → 数据 → 反馈」闭环。

**并行与触发：** 3a 二创与 3b 写作可并行；评论管理可与数据助手并行。执行顺序 1 → 2 → (3a 或 3b) → 4 → 5/6；步骤 5、6 可持续运行或按周期执行。

## 预设技能（按执行链路顺序）

**ClawHub 技能一览**见 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)，**skills.sh 技能一览**安装：`npx skills add <owner/repo> --skill <名>`；技能列表见下方。以下按 **智能工作执行链路** 顺序列出（1→2→3a→3b→4→5→6）。

| 步骤 | Agent id                        | 默认技能列表                                                                 | 用途说明 |
|------|---------------------------------|------------------------------------------------------------------------------|----------|
| 1 | wechat-article-hot-monitor     | baoyu-url-to-markdown, baoyu-format-markdown                               | 抓取热点链接、规范日报格式 |
| 2 | wechat-article-viral-breakdown  | wechat-article-extractor, baoyu-format-markdown                             | 文章提取（ClawHub/skills.sh）+ 拆解输出规范 |
| 3a | wechat-article-rewrite         | baoyu-cover-image, baoyu-article-illustrator                               | 封面与长文配图 |
| 3b | wechat-article-write           | baoyu-cover-image, baoyu-article-illustrator                              | 原创内容配图与封面 |
| 4 | wechat-article-publisher       | wechat-ai-publisher, baoyu-markdown-to-html, baoyu-compress-image, baoyu-post-to-wechat | 发布（ClawHub 或 skills.sh）+ 排版与压缩 |
| 5 | wechat-article-data-assistant  | baoyu-format-markdown                                                      | 数据报告格式规范 |
| 6 | wechat-article-comment-manager | （按需从 ClawHub/skills.sh 选评论采集与回复技能）                             | 评论拉取、回复草稿、情感摘要 |

### 安装方式（按来源区分，建议按链路顺序安装）

**来源：ClawHub（为主）** — 安装后目录名与 config 中 `skills` 一致。

```bash
clawhub search wechat
clawhub install wechat-article-extractor
clawhub install wechat-ai-publisher
```

**来源：skills.sh（取最优）** — Baoyu 系列与公众号专项安装：`npx skills add <owner/repo> --skill <名>`；技能列表见下方。按执行链路顺序安装示例：

```bash
# 步骤 1、2：监控与拆解
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown
# 步骤 3a、3b：二创与写作
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator
# 步骤 4：发布
npx skills add jimliu/baoyu-skills --skill baoyu-post-to-wechat
npx skills add jimliu/baoyu-skills --skill baoyu-markdown-to-html
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image
# 文章提取 / 发布（可选）
npx skills add freestylefly/wechat-article-extractor-skill --skill wechat-article-extractor
npx skills add iamzifei/wechat-article-publisher-skill --skill wechat-article-publisher
```

若使用 `npx skillsadd`（无空格），格式以 skills.sh 文档为准。安装后确认技能目录名与 config 中 `skills` 一致。**发布智能体需配置公众号凭证**（环境变量或 EXTEND.md）；不要在 TOOLS.md 或工作区存储凭证。

## 补充约定（设计时已落实）

- **拆解框架结构**：爆款拆解输出字段约定为 title/hook/outline/theme/format，见各智能体 TOOLS.md。
- **发布日志衔接**：发布智能体将结果写入约定路径（如 `publish-logs/`），格式一致，供数据助手解析。
- **数据助手反馈**：反馈具体到可修正项（如某类主题/钩子加强或弱化），便于爆款拆解调整搜索与拆解标准。
- **凭证与隐私**：凭证仅用环境变量或 EXTEND.md；各智能体不泄露用户或内部数据。
- **版权与合规**：拆解与二创做摘要与再创作，不原文照搬；发布与内容尺度由使用方负责。

## 配置说明

- **Workspace：** 各智能体 workspace 为 `~/.openclaw/workspace-wechat-article-<agentId>`；部署时将本目录下对应子目录复制或链接到该路径。
- **Config 片段：** `config/openclaw-wechat-article-fragment.json`，合并进主 openclaw 配置即可。
- **路由：** 通过 bindings 将对应渠道或会话路由到各 agent id。

## 初始化命令（按执行链路顺序）

### 添加七件套

```bash
openclaw agents add wechat-article-hot-monitor       --workspace ~/.openclaw/workspace-wechat-article-hot-monitor;
openclaw agents add wechat-article-viral-breakdown   --workspace ~/.openclaw/workspace-wechat-article-viral-breakdown;
openclaw agents add wechat-article-rewrite            --workspace ~/.openclaw/workspace-wechat-article-rewrite;
openclaw agents add wechat-article-write             --workspace ~/.openclaw/workspace-wechat-article-write;
openclaw agents add wechat-article-publisher         --workspace ~/.openclaw/workspace-wechat-article-publisher;
openclaw agents add wechat-article-data-assistant    --workspace ~/.openclaw/workspace-wechat-article-data-assistant;
openclaw agents add wechat-article-comment-manager   --workspace ~/.openclaw/workspace-wechat-article-comment-manager;
```

### 按渠道绑定（示例：wecom）

```bash
openclaw agents bind --agent wechat-article-hot-monitor       --bind wecom:wechat-article-hot-monitor;
openclaw agents bind --agent wechat-article-viral-breakdown   --bind wecom:wechat-article-viral-breakdown;
openclaw agents bind --agent wechat-article-rewrite            --bind wecom:wechat-article-rewrite;
openclaw agents bind --agent wechat-article-write              --bind wecom:wechat-article-write;
openclaw agents bind --agent wechat-article-publisher          --bind wecom:wechat-article-publisher;
openclaw agents bind --agent wechat-article-data-assistant      --bind wecom:wechat-article-data-assistant;
openclaw agents bind --agent wechat-article-comment-manager     --bind wecom:wechat-article-comment-manager;
```

### 删除七件套（需先解除绑定）

```bash
openclaw agents remove wechat-article-hot-monitor;
openclaw agents remove wechat-article-viral-breakdown;
openclaw agents remove wechat-article-rewrite;
openclaw agents remove wechat-article-write;
openclaw agents remove wechat-article-publisher;
openclaw agents remove wechat-article-data-assistant;
openclaw agents remove wechat-article-comment-manager;
```

## 文件结构（每智能体）

与 company、discord、telegram 一致：`AGENTS.md`、`zh-CN/AGENTS.md`、`SOUL.md`、`zh-CN/SOUL.md`、`IDENTITY.md`、`zh-CN/IDENTITY.md`、`TOOLS.md`、`zh-CN/TOOLS.md`、`BOOTSTRAP.md`、`zh-CN/BOOTSTRAP.md`、`USER.md`、`HEARTBEAT.md`、`zh-CN/HEARTBEAT.md`。

# 头条号内容管线 (Toutiao Agents)

> 基于 [ANALYSIS-渠道与流程对齐 OctoFlow](../../ANALYSIS-渠道与流程对齐OctoFlow.md) §2.1 建议，为**头条号**（综合图文/视频）提供与 xiaohongshu / wechat-article 同构的内容管线七件套：热门监控、爆款拆解、二创、自动发布、数据助手、写作、评论管理。读（抓取）采用通用或专用抓取，写（发布）需开放平台或浏览器自动化。

## 技能来源区分

| 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|----------|--------------|----------|
| **ClawHub（若有）** | [clawhub.ai/skills?q=toutiao](https://clawhub.ai/skills?sort=downloads&q=toutiao) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug>` |
| **skills.sh（取最优）** | [skills.sh/?q=baoyu](https://skills.sh/?q=baoyu) | 见下方技能表与安装方式 | `npx skills add <owner/repo> --skill <名>` |

全仓库技能总览与 Baoyu 归类见 [docs/SKILLS-MASTER.md](../../docs/SKILLS-MASTER.md)。

## 必须保证的七个环节

1. **热门监控**：每日/按需搜索头条号热点与爆款文章/视频，产出日报或摘要，供爆款拆解与数据助手使用。
2. **爆款拆解**：对爆款内容做拆解（标题、钩子、结构、主题），产出拆解框架供二创与数据助手使用。
3. **二创**：根据拆解框架与主题进行新文案与配图，产出草稿供发布与数据助手使用。
4. **自动发布**：将已通过草稿发布到头条号（需开放平台或浏览器），并记录结果供数据助手分析。
5. **数据助手**：解析数据、交叉验证效果，将可执行结论反馈给爆款拆解（形成闭环）。
6. **写作**：强调原创；用户主图/选题+热点做原创内容，产出草稿供发布与数据助手。
7. **评论管理**：评论采集、起草回复、情感分析；回复需审批/门禁后发布。

**管线关系：** 热门监控 → 日报/摘要 → 爆款拆解 → 拆解框架 → 二创/写作 → 草稿+配图 → 自动发布 → 发布日志 → 数据助手 + 评论管理 → 反馈至爆款拆解与热门监控。

## 智能体清单

| 序号 | Agent id                 | 展示名           | 目录                               | 职责摘要 |
|------|---------------------------|------------------|------------------------------------|----------|
| 1    | toutiao-hot-monitor       | 头条号热门监控   | 1-toutiao-hot-monitor              | 每日/按需搜索头条号热点与爆款，产出日报或摘要 |
| 2    | toutiao-viral-breakdown   | 头条号爆款拆解   | 2-toutiao-viral-breakdown          | 对爆款内容做拆解，产出结构化拆解框架 |
| 3    | toutiao-rewrite           | 头条号二创       | 3-toutiao-rewrite                  | 根据拆解框架与主题创作新文案与配图 |
| 4    | toutiao-publisher          | 头条号自动发布   | 4-toutiao-publisher                | 将已通过草稿发布到头条号并记录结果（需开放平台/浏览器） |
| 5    | toutiao-data-assistant    | 头条号数据助手   | 5-toutiao-data-assistant           | 解析数据、交叉验证效果、反馈给爆款拆解 |
| 6    | toutiao-write              | 头条号写作       | 6-toutiao-write                    | 强调原创：用户主图/选题+热点做原创内容，产出草稿 |
| 7    | toutiao-comment-manager   | 头条号评论管理   | 7-toutiao-comment-manager          | 评论采集、起草回复、情感分析；回复需审批/门禁后发布 |

## 智能工作执行链路

七件套按以下链路协同执行；可按时序触发（如每日）或按需触发单环节。

| 步骤 | 环节 | 智能体 | 输入 | 输出 | 说明 |
|------|------|--------|------|------|------|
| 1 | 热门监控 | toutiao-hot-monitor | 关键词/品类/时间范围 | 日报或按需摘要（热点、爆款列表） | 入口；可为定时或人工触发 |
| 2 | 爆款拆解 | toutiao-viral-breakdown | 日报/摘要中的爆款链接或列表 | 拆解框架（标题、钩子、结构、主题） | 消费监控产出，供二创与数据侧使用 |
| 3a | 二创 | toutiao-rewrite | 拆解框架 + 主题 | 草稿（文案 + 封面 + 配图） | 基于拆解做差异化二创，不发布 |
| 3b | 写作 | toutiao-write | 用户选题 + 热点/爆款洞察 | 草稿（文案 + 封面 + 配图） | 独立于拆解的原创内容生产 |
| 4 | 自动发布 | toutiao-publisher | 已审核草稿 | 发布结果日志（链接、时间、状态） | 仅发布已通过审核内容；发布前压缩图片 |
| 5 | 数据助手 | toutiao-data-assistant | 发布日志 + 互动数据 | 可执行反馈（关键词/拆解维度/优先主题） | 交叉验证效果，反馈至爆款拆解与监控 |
| 6 | 评论管理 | toutiao-comment-manager | 文章/账号评论源 | 回复草稿 + 情感摘要 | 回复须审批/门禁后由人工或流程发布 |

**闭环：** 数据助手的反馈驱动爆款拆解调整搜索与拆解标准，热门监控可据此调整关键词与范围，形成「监控 → 拆解 → 内容 → 发布 → 数据 → 反馈」闭环。

**并行与触发：** 3a 二创与 3b 写作可并行；评论管理可与数据助手并行。执行顺序 1 → 2 → (3a 或 3b) → 4 → 5/6；步骤 5、6 可持续运行或按周期执行。

## 预设技能（按执行链路顺序）

以下按 **智能工作执行链路** 顺序列出（1→2→3a→3b→4→5→6）。见 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 与下方技能表。

| 步骤 | Agent id                 | 默认技能列表（示例） | 用途说明 |
|------|--------------------------|----------------------|----------|
| 1 | toutiao-hot-monitor      | baoyu-url-to-markdown, baoyu-format-markdown | 抓取热点链接、规范日报格式 |
| 2 | toutiao-viral-breakdown  | baoyu-url-to-markdown, baoyu-format-markdown | 抓取成文、规范拆解输出 |
| 3a | toutiao-rewrite          | baoyu-cover-image, baoyu-article-illustrator | 封面与配图 |
| 3b | toutiao-write            | baoyu-cover-image, baoyu-article-illustrator | 原创内容配图与封面 |
| 4 | toutiao-publisher        | baoyu-compress-image | 发布前压缩；发布需开放平台或浏览器 |
| 5 | toutiao-data-assistant   | baoyu-format-markdown | 数据报告格式规范 |
| 6 | toutiao-comment-manager  | （按需选评论采集与回复技能） | 评论拉取、回复草稿、情感摘要 |

### 安装方式（建议按链路顺序安装）

**来源：ClawHub** — `clawhub search toutiao` 后 `clawhub install <slug>`。

**来源：skills.sh** — 按执行链路对应智能体顺序安装：

```bash
# 步骤 1、2：监控与拆解
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown
# 步骤 3a、3b：二创与写作
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator
# 步骤 4：发布
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image
```

**勿在 TOOLS.md 存凭证。**

## 配置说明

- **Workspace：** `~/.openclaw/workspace-toutiao-<agentId>`。
- **Config 片段：** `config/openclaw-toutiao-fragment.json`。
- **路由：** 通过 bindings 将渠道或会话路由到各 agent id。

## 初始化命令（按执行链路顺序）

### 添加七件套

```bash
openclaw agents add toutiao-hot-monitor       --workspace ~/.openclaw/workspace-toutiao-hot-monitor;
openclaw agents add toutiao-viral-breakdown   --workspace ~/.openclaw/workspace-toutiao-viral-breakdown;
openclaw agents add toutiao-rewrite           --workspace ~/.openclaw/workspace-toutiao-rewrite;
openclaw agents add toutiao-write             --workspace ~/.openclaw/workspace-toutiao-write;
openclaw agents add toutiao-publisher         --workspace ~/.openclaw/workspace-toutiao-publisher;
openclaw agents add toutiao-data-assistant    --workspace ~/.openclaw/workspace-toutiao-data-assistant;
openclaw agents add toutiao-comment-manager   --workspace ~/.openclaw/workspace-toutiao-comment-manager;
```

### 按渠道绑定（示例：wecom）

```bash
openclaw agents bind --agent toutiao-hot-monitor       --bind wecom:toutiao-hot-monitor;
openclaw agents bind --agent toutiao-viral-breakdown   --bind wecom:toutiao-viral-breakdown;
openclaw agents bind --agent toutiao-rewrite           --bind wecom:toutiao-rewrite;
openclaw agents bind --agent toutiao-write             --bind wecom:toutiao-write;
openclaw agents bind --agent toutiao-publisher         --bind wecom:toutiao-publisher;
openclaw agents bind --agent toutiao-data-assistant    --bind wecom:toutiao-data-assistant;
openclaw agents bind --agent toutiao-comment-manager   --bind wecom:toutiao-comment-manager;
```

### 删除七件套（需先解除绑定）

```bash
openclaw agents remove toutiao-hot-monitor;
openclaw agents remove toutiao-viral-breakdown;
openclaw agents remove toutiao-rewrite;
openclaw agents remove toutiao-write;
openclaw agents remove toutiao-publisher;
openclaw agents remove toutiao-data-assistant;
openclaw agents remove toutiao-comment-manager;
```

## 文件结构（每智能体）

与 zhihu、weibo 一致：`AGENTS.md`、`zh-CN/AGENTS.md`、`SOUL.md`、`IDENTITY.md`、`TOOLS.md`、`BOOTSTRAP.md`、`HEARTBEAT.md`、`USER.md` 及 zh-CN 对应文件。

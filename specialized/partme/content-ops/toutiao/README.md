# 头条号内容管线 (Toutiao Agents)

> 基于 [ANALYSIS-渠道与流程对齐 OctoFlow](../../ANALYSIS-渠道与流程对齐OctoFlow.md) §2.1 建议，为**头条号**（综合图文/视频）提供与 xiaohongshu / wechat-article 同构的内容管线七件套：热门监控、爆款拆解、二创、自动发布、数据助手、原创、评论管理。读（抓取）采用通用或专用抓取，写（发布）需开放平台或浏览器自动化。

## 技能选型（ClawHub 优先，skills.sh 后补）

**技能来源区分：**

| 序号 | 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|------|----------|--------------|----------|
| 1 | **ClawHub（为主）** | [clawhub.ai/skills?q=toutiao](https://clawhub.ai/skills?sort=downloads&q=toutiao) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug> --workdir ~/.openclaw;` |
| 2 | **SkillHub（国内推荐）** | SkillHub 搜索「头条」 | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `skillhub install <slug>`（需先安装 SkillHub CLI） |
| 3 | **skills.sh（取最优）** | [skills.sh/?q=baoyu](https://skills.sh/?q=baoyu) | [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md) | `npx skills add <owner/repo> --skill <名> -y -g;` |

## 技能评估结论（摘录）

> 完整评估见 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md)。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。** 头条号 ClawHub 技能待补充，当前以 Baoyu 为主。**完整技能栈**（七件套 + 补充能力）见 [SKILLS-EVALUATION.md § 七、完整技能栈](./SKILLS-EVALUATION.md#七完整技能栈七件套--补充能力)。

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown/报告格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 封面/长文配图 | baoyu-cover-image, baoyu-article-illustrator | — |
| 3 | 图片压缩 | baoyu-compress-image | — |

**补充能力（完整栈）** — 在七件套基础上扩展，能用上的全列：

| 序号 | 补充能力 | 用途 | 推荐技能 | 来源 |
|------|----------|------|----------|------|
| 1 | 多语言与翻译 | 多语言内容、翻译适配 | baoyu-translate | skills.sh |
| 2 | 信息图/漫画风配图 | 丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh |

全仓库技能总览与 Baoyu 归类见 [docs/SKILLS-MASTER.md](../../docs/SKILLS-MASTER.md)。

## 必须保证的七个环节

1. **热门监控**：每日/按需搜索头条号热点与爆款文章/视频，产出日报或摘要，供爆款拆解与数据助手使用。
2. **爆款拆解**：对爆款内容做拆解（标题、钩子、结构、主题），产出拆解框架供二创与数据助手使用。
3. **二创**：根据拆解框架与主题进行新文案与配图，产出草稿供发布与数据助手使用。
4. **自动发布**：将已通过草稿发布到头条号（需开放平台或浏览器），并记录结果供数据助手分析。
5. **数据助手**：解析数据、交叉验证效果，将可执行结论反馈给爆款拆解（形成闭环）。
6. **原创**：强调原创；用户主图/选题+热点做原创内容，产出草稿供发布与数据助手。
7. **评论管理**：评论采集、起草回复、情感分析；回复需审批/门禁后发布。

**管线关系：** 热门监控 → 日报/摘要 → 爆款拆解 → 拆解框架 → 二创/原创 → 草稿+配图 → 自动发布 → 发布日志 → 数据助手 + 评论管理 → 反馈至爆款拆解与热门监控。

## 主智能体

- 本渠道主智能体目录：`1-toutiao-specialist`（若存在 `*-strategist` 目录，保持不重命名并作为该组最后扩展角色）。

## 智能体清单

| 序号 | Agent id                 | 展示名           | 目录                               | 职责摘要 |
|------|---------------------------|------------------|------------------------------------|----------|
| 1    | toutiao-hot-monitor       | 头条号热门监控   | 2-toutiao-hot-monitor              | 每日/按需搜索头条号热点与爆款，产出日报或摘要 |
| 2    | toutiao-viral-breakdown   | 头条号爆款拆解   | 3-toutiao-viral-breakdown          | 对爆款内容做拆解，产出结构化拆解框架 |
| 3    | toutiao-rewrite           | 头条号二创       | 4-toutiao-rewrite                  | 根据拆解框架与主题创作新文案与配图 |
| 4    | toutiao-publisher          | 头条号自动发布   | 5-toutiao-publisher                | 将已通过草稿发布到头条号并记录结果（需开放平台/浏览器） |
| 5    | toutiao-data-assistant    | 头条号数据助手   | 6-toutiao-data-assistant           | 解析数据、交叉验证效果、反馈给爆款拆解 |
| 6    | toutiao-write              | 头条号原创       | 7-toutiao-write                    | 强调原创：用户主图/选题+热点做原创内容，产出草稿 |
| 7    | toutiao-comment-manager   | 头条号评论管理   | 8-toutiao-comment-manager          | 评论采集、起草回复、情感分析；回复需审批/门禁后发布 |

## 智能工作执行链路

七件套按以下链路协同执行；可按时序触发（如每日）或按需触发单环节。

| 步骤 | 环节 | 智能体 | 输入 | 输出 | 说明 |
|------|------|--------|------|------|------|
| 1 | 热门监控 | toutiao-hot-monitor | 关键词/品类/时间范围 | 日报或按需摘要（热点、爆款列表） | 入口；可为定时或人工触发 |
| 2 | 爆款拆解 | toutiao-viral-breakdown | 日报/摘要中的爆款链接或列表 | 拆解框架（标题、钩子、结构、主题） | 消费监控产出，供二创与数据侧使用 |
| 3a | 二创 | toutiao-rewrite | 拆解框架 + 主题 | 草稿（文案 + 封面 + 配图） | 基于拆解做差异化二创，不发布 |
| 3b | 原创 | toutiao-write | 用户选题 + 热点/爆款洞察 | 草稿（文案 + 封面 + 配图） | 独立于拆解的原创内容生产 |
| 4 | 自动发布 | toutiao-publisher | 已审核草稿 | 发布结果日志（链接、时间、状态） | 仅发布已通过审核内容；发布前压缩图片 |
| 5 | 数据助手 | toutiao-data-assistant | 发布日志 + 互动数据 | 可执行反馈（关键词/拆解维度/优先主题） | 交叉验证效果，反馈至爆款拆解与监控 |
| 6 | 评论管理 | toutiao-comment-manager | 文章/账号评论源 | 回复草稿 + 情感摘要 | 回复须审批/门禁后由人工或流程发布 |

**闭环：** 数据助手的反馈驱动爆款拆解调整搜索与拆解标准，热门监控可据此调整关键词与范围，形成「监控 → 拆解 → 内容 → 发布 → 数据 → 反馈」闭环。

**并行与触发：** 3a 二创与 3b 原创可并行；评论管理可与数据助手并行。执行顺序 1 → 2 → (3a 或 3b) → 4 → 5/6；步骤 5、6 可持续运行或按周期执行。

## 预设技能（按评估结论，去重取最优）

以下为 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md) 最终推荐；同能力只选一个来源。

| 步骤 | Agent id                 | 推荐技能 | 来源 | 说明 |
|------|--------------------------|----------|------|------|
| 1 | toutiao-hot-monitor      | toutiao-news-trends；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh | 热点/趋势 + 抓取+日报格式 |
| 2 | toutiao-viral-breakdown  | baoyu-url-to-markdown, baoyu-format-markdown；可选 toutiao-news-trends | skills.sh；ClawHub/SkillHub | 抓取成文+拆解格式 |
| 3a | toutiao-rewrite          | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面与配图 |
| 3b | toutiao-write            | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | toutiao-publisher        | toutiao-publisher；baoyu-compress-image | ClawHub/SkillHub；skills.sh | 头条发布 + 压缩；发布需浏览器/开放平台 |
| 5 | toutiao-data-assistant   | baoyu-format-markdown；可选 toutiao-news-trends | skills.sh；ClawHub/SkillHub | 报告格式 |
| 6 | toutiao-comment-manager  | （按需选评论采集与回复技能） | ClawHub/skills.sh | 评论拉取、回复草稿 |

### 七件套全部可使用的技能：全部安装 / 全部卸载命令

**全部不冲突**：来自 [SKILLS-EVALUATION.md § 7.3](./SKILLS-EVALUATION.md#73-全部不冲突全部安装命令与全部卸载命令)；同质只取 1 个首选，可并存的全部列入。

**全部安装命令（复制执行即可）**

```bash
# 第一步：安装 SkillHub CLI（仅首次需要，国内推荐）
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash

# ClawHub/SkillHub — 头条热点趋势 + 头条发布
skillhub install toutiao-news-trends
skillhub install toutiao-publisher

# skills.sh — 头条号七件套 + 补充（能用上的全要）
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g;
```

**全部卸载命令（复制执行即可）**

```bash
# ClawHub/SkillHub 安装的头条技能
clawhub uninstall toutiao-news-trends;
clawhub uninstall toutiao-publisher;

# skills.sh 技能
npx skills remove baoyu-url-to-markdown;
npx skills remove baoyu-format-markdown;
npx skills remove baoyu-cover-image;
npx skills remove baoyu-article-illustrator;
npx skills remove baoyu-compress-image;
npx skills remove baoyu-translate;
npx skills remove baoyu-infographic;
npx skills remove baoyu-comic;
```

### 安装前置与唯一命令来源

**第一步：安装 SkillHub CLI**（仅首次需要）

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**全部技能安装/卸载**：以本页上方「全部安装命令」与「全部卸载命令」为准（与 [SKILLS-EVALUATION.md § 7.3](./SKILLS-EVALUATION.md#73-全部不冲突全部安装命令与全部卸载命令) 一致）；安装后目录名需与 config 中 `skills` 一致。勿在 TOOLS.md 存凭证。

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

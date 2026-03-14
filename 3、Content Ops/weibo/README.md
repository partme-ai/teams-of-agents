# 微博内容管线 (Weibo Agents)

> 基于 [ANALYSIS-渠道与流程对齐 OctoFlow](../../ANALYSIS-渠道与流程对齐OctoFlow.md) §2.1 建议，为**微博**提供与 xiaohongshu / wechat-article 同构的内容管线七件套：热门监控、爆款拆解、二创、自动发布、数据助手、原创、评论管理。读（抓取）采用通用抓取或 API，写（发布）可采用 social-push、baoyu-post-to-weibo 或浏览器自动化。

## 技能选型（ClawHub 优先，skills.sh 后补）

**技能来源区分：**

| 序号 | 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|------|----------|--------------|----------|
| 1 | **ClawHub（为主）** | [clawhub.ai/skills?q=weibo](https://clawhub.ai/skills?sort=downloads&q=weibo) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug> --workdir ~/.openclaw;` |
| 2 | **SkillHub（国内推荐）** | SkillHub 搜索「微博」 | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `skillhub install <slug>`（需先安装 SkillHub CLI） |
| 3 | **skills.sh（取最优）** | [skills.sh/?q=weibo](https://skills.sh/?q=weibo)、[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu) | [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md) | `npx skills add <owner/repo> --skill <名> -y -g;` |

## 技能评估结论（摘录）

> 完整评估见 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md)。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。** 微博 ClawHub 技能待补充，当前以 Baoyu 为主。**完整技能栈**（七件套 + 补充能力）见 [SKILLS-EVALUATION.md § 七、完整技能栈](./SKILLS-EVALUATION.md#七完整技能栈七件套--补充能力)。

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown/报告格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 封面/配图 | baoyu-cover-image, baoyu-article-illustrator | — |
| 3 | 发布到微博 | baoyu-post-to-weibo 或 social-push | 按需选一 |
| 4 | 图片压缩 | baoyu-compress-image | — |

**补充能力（完整栈）** — 在七件套基础上扩展，能用上的全列：

| 序号 | 补充能力 | 用途 | 推荐技能 | 来源 |
|------|----------|------|----------|------|
| 1 | 多语言与翻译 | 多语言内容、翻译适配 | baoyu-translate | skills.sh |
| 2 | 信息图/漫画风配图 | 丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh |
| 3 | 微博发布 | 将草稿发布到微博 | baoyu-post-to-weibo | skills.sh |

## 必须保证的七个环节

1. **热门监控**：每日/按需搜索微博热点与爆款博文/话题，产出日报或摘要，供爆款拆解与数据助手使用。
2. **爆款拆解**：对监控/调研得到的爆款博文做拆解（标题、钩子、结构、主题），产出拆解框架供二创与数据助手使用。
3. **二创**：根据拆解框架与主题进行新文案与配图，产出草稿供发布与数据助手使用。
4. **自动发布**：将已通过草稿发布到微博，并记录结果供数据助手分析。
5. **数据助手**：解析数据、交叉验证效果，将可执行结论反馈给爆款拆解（形成闭环）。
6. **原创**：强调原创；用户主图+热点/爆款做原创博文，产出草稿供发布与数据助手。
7. **评论管理**：评论采集、起草回复、情感分析；回复需审批/门禁后发布。

**管线关系：** 热门监控 → 日报/摘要 → 爆款拆解 → 拆解框架 → 二创/原创 → 草稿+配图 → 自动发布 → 发布日志 → 数据助手 + 评论管理 → 反馈至爆款拆解与热门监控。

## 智能体清单

| 序号 | Agent id               | 展示名         | 目录                           | 职责摘要 |
|------|------------------------|----------------|--------------------------------|----------|
| 1    | weibo-hot-monitor      | 微博热门监控   | 1-weibo-hot-monitor           | 每日/按需搜索微博热点与爆款博文/话题，产出日报或摘要 |
| 2    | weibo-viral-breakdown  | 微博爆款拆解   | 2-weibo-viral-breakdown       | 对爆款博文做拆解，产出结构化拆解框架 |
| 3    | weibo-rewrite          | 微博二创       | 3-weibo-rewrite               | 根据拆解框架与主题创作新文案与配图 |
| 4    | weibo-publisher        | 微博自动发布   | 4-weibo-publisher             | 将已通过草稿发布到微博并记录结果 |
| 5    | weibo-data-assistant   | 微博数据助手   | 5-weibo-data-assistant        | 解析数据、交叉验证效果、反馈给爆款拆解 |
| 6    | weibo-write            | 微博原创       | 6-weibo-write                 | 强调原创：用户主图+热点/爆款做原创博文，产出草稿 |
| 7    | weibo-comment-manager  | 微博评论管理   | 7-weibo-comment-manager       | 评论采集、起草回复、情感分析；回复需审批/门禁后发布 |

## 智能工作执行链路

七件套按以下链路协同执行；可按时序触发（如每日）或按需触发单环节。

| 步骤 | 环节 | 智能体 | 输入 | 输出 | 说明 |
|------|------|--------|------|------|------|
| 1 | 热门监控 | weibo-hot-monitor | 关键词/品类/时间范围 | 日报或按需摘要（热点、爆款列表） | 入口；可为定时或人工触发 |
| 2 | 爆款拆解 | weibo-viral-breakdown | 日报/摘要中的爆款链接或列表 | 拆解框架（标题、钩子、结构、主题） | 消费监控产出，供二创与数据侧使用 |
| 3a | 二创 | weibo-rewrite | 拆解框架 + 主题 | 草稿（文案 + 封面 + 配图） | 基于拆解做差异化二创，不发布 |
| 3b | 原创 | weibo-write | 用户选题 + 热点/爆款洞察 | 草稿（文案 + 封面 + 配图） | 独立于拆解的原创内容生产 |
| 4 | 自动发布 | weibo-publisher | 已审核草稿 | 发布结果日志（链接、时间、状态） | 仅发布已通过审核内容；发布前压缩图片 |
| 5 | 数据助手 | weibo-data-assistant | 发布日志 + 互动数据 | 可执行反馈（关键词/拆解维度/优先主题） | 交叉验证效果，反馈至爆款拆解与监控 |
| 6 | 评论管理 | weibo-comment-manager | 文章/账号评论源 | 回复草稿 + 情感摘要 | 回复须审批/门禁后由人工或流程发布 |

**闭环：** 数据助手的反馈驱动爆款拆解调整搜索与拆解标准，热门监控可据此调整关键词与范围，形成「监控 → 拆解 → 内容 → 发布 → 数据 → 反馈」闭环。

**并行与触发：** 3a 二创与 3b 原创可并行；评论管理可与数据助手并行。执行顺序 1 → 2 → (3a 或 3b) → 4 → 5/6；步骤 5、6 可持续运行或按周期执行。

## 预设技能（按评估结论，去重取最优）

以下为 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md) 最终推荐；同能力只选一个来源。

| 步骤 | Agent id               | 推荐技能 | 来源 | 说明 |
|------|------------------------|----------|------|------|
| 1 | weibo-hot-monitor      | weibo-fresh-posts；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh | 关注流监控+每日 Markdown + 抓取+日报格式 |
| 2 | weibo-viral-breakdown  | baoyu-url-to-markdown, baoyu-format-markdown；可选 weibo-fresh-posts | skills.sh；ClawHub/SkillHub | 抓取成文+拆解格式 |
| 3a | weibo-rewrite          | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面与配图 |
| 3b | weibo-write            | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | weibo-publisher        | weibo-manager；baoyu-compress-image；可选 baoyu-post-to-weibo / social-push | ClawHub/SkillHub；skills.sh | 管理/执行/发布/审查 + 压缩+发布 |
| 5 | weibo-data-assistant   | baoyu-format-markdown；可选 weibo-fresh-posts | skills.sh；ClawHub/SkillHub | 报告格式 |
| 6 | weibo-comment-manager  | weibo-manager（审查）；按需评论采集与回复技能 | ClawHub/SkillHub；skills.sh | 评论拉取、回复草稿、审查 |

### 七件套全部可使用的技能：全部安装 / 全部卸载命令

**全部不冲突**：来自 [SKILLS-EVALUATION.md § 7.3](./SKILLS-EVALUATION.md#73-全部不冲突全部安装命令与全部卸载命令)；同质只取 1 个首选，可并存的全部列入；config 中 `agents.list[].skills` 填写的为「安装后目录名」。若某技能与当前环境冲突可单独注释该行。

**全部安装命令（复制执行即可）**

```bash
# 第一步：安装 SkillHub CLI（仅首次需要，国内推荐）
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash

# ClawHub/SkillHub — 微博关注流监控 + 微博管理/发布/审查
skillhub install weibo-fresh-posts
skillhub install weibo-manager

# skills.sh — 微博七件套 + 补充（能用上的全要）
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-post-to-weibo -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g;
```

**全部卸载命令（复制执行即可）**

```bash
# ClawHub/SkillHub 安装的微博技能
clawhub uninstall weibo-fresh-posts;
clawhub uninstall weibo-manager;

# skills.sh 技能
npx skills remove baoyu-url-to-markdown;
npx skills remove baoyu-format-markdown;
npx skills remove baoyu-cover-image;
npx skills remove baoyu-article-illustrator;
npx skills remove baoyu-compress-image;
npx skills remove baoyu-post-to-weibo;
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

- **Workspace：** `~/.openclaw/workspace-weibo-<agentId>`。
- **Config 片段：** `config/openclaw-weibo-fragment.json`。
- **路由：** 通过 bindings 将渠道或会话路由到各 agent id。

## 初始化命令（按执行链路顺序）

### 添加七件套

```bash
openclaw agents add weibo-hot-monitor       --workspace ~/.openclaw/workspace-weibo-hot-monitor;
openclaw agents add weibo-viral-breakdown   --workspace ~/.openclaw/workspace-weibo-viral-breakdown;
openclaw agents add weibo-rewrite           --workspace ~/.openclaw/workspace-weibo-rewrite;
openclaw agents add weibo-write             --workspace ~/.openclaw/workspace-weibo-write;
openclaw agents add weibo-publisher         --workspace ~/.openclaw/workspace-weibo-publisher;
openclaw agents add weibo-data-assistant    --workspace ~/.openclaw/workspace-weibo-data-assistant;
openclaw agents add weibo-comment-manager   --workspace ~/.openclaw/workspace-weibo-comment-manager;
```

### 按渠道绑定（示例：wecom）

```bash
openclaw agents bind --agent weibo-hot-monitor       --bind wecom:weibo-hot-monitor;
openclaw agents bind --agent weibo-viral-breakdown   --bind wecom:weibo-viral-breakdown;
openclaw agents bind --agent weibo-rewrite           --bind wecom:weibo-rewrite;
openclaw agents bind --agent weibo-write             --bind wecom:weibo-write;
openclaw agents bind --agent weibo-publisher         --bind wecom:weibo-publisher;
openclaw agents bind --agent weibo-data-assistant    --bind wecom:weibo-data-assistant;
openclaw agents bind --agent weibo-comment-manager   --bind wecom:weibo-comment-manager;
```

### 删除七件套（需先解除绑定）

```bash
openclaw agents remove weibo-hot-monitor;
openclaw agents remove weibo-viral-breakdown;
openclaw agents remove weibo-rewrite;
openclaw agents remove weibo-write;
openclaw agents remove weibo-publisher;
openclaw agents remove weibo-data-assistant;
openclaw agents remove weibo-comment-manager;
```

## 文件结构（每智能体）

与 zhihu、wechat-article、xiaohongshu 一致：`AGENTS.md`、`zh-CN/AGENTS.md`、`SOUL.md`、`IDENTITY.md`、`TOOLS.md`、`BOOTSTRAP.md`、`HEARTBEAT.md`、`USER.md` 及 zh-CN 对应文件。

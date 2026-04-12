# 抖音内容管线 (Douyin Agents)

> 基于 [ANALYSIS-渠道与流程对齐 OctoFlow](../../ANALYSIS-渠道与流程对齐OctoFlow.md) §2.1 建议，为**抖音**（短视频）提供与 xiaohongshu / wechat-article 同构的内容管线七件套：热门监控、爆款拆解、二创、自动发布、数据助手、原创、评论管理。读（抓取）优先官方 API，无 API 时可用 yt-dlp 类；写（发布）需抖音开放平台 API 或浏览器自动化。**合规与平台 ToS 需严格遵守。**

## 技能选型

| 序号 | 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|------|----------|--------------|----------|
| 1 | **ClawHub（为主）** | [clawhub.ai/skills?q=douyin](https://clawhub.ai/skills?sort=downloads&q=douyin) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug>` |
| 2 | **skills.sh（取最优）** | [skills.sh/?q=douyin](https://skills.sh/?q=douyin)、[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu) | [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md) | `npx skills add <owner/repo> --skill <名>` |

## 技能评估结论（摘录）

> 完整评估见 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md)。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。**

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown/日报格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 抖音热榜/热搜 | douyin-hot-trend（ClawHub） | — |
| 3 | 抖音视频下载 | douyin-downloader / douyin-video-fetch | 同质只装一处 |
| 4 | 封面/配图 | baoyu-cover-image, baoyu-article-illustrator | — |
| 5 | 发布到抖音 | douyin-publish（ClawHub） | 同质只选一 |
| 6 | 图片压缩 | baoyu-compress-image | — |

## 补充能力（完整栈）

七件套之外本管线可用上的补充能力（与 [SKILLS-EVALUATION.md §6.1](./SKILLS-EVALUATION.md) 一致）：评论回复/采集、多语言与翻译、信息图/漫画风配图；推荐技能见 6.1 表。

## 必须保证的七个环节

1. **热门监控**：每日/按需搜索抖音热点与爆款短视频，产出日报或摘要，供爆款拆解与数据助手使用。
2. **爆款拆解**：对监控/调研得到的爆款短视频做拆解（标题、钩子、结构、主题），产出拆解框架供二创与数据助手使用。
3. **二创**：根据拆解框架与主题进行新文案与封面/脚本，产出草稿供发布与数据助手使用。
4. **自动发布**：将已通过草稿发布到抖音（需开放平台 API 或浏览器），并记录结果供数据助手分析。
5. **数据助手**：解析数据、交叉验证效果，将可执行结论反馈给爆款拆解（形成闭环）。
6. **原创**：强调原创；用户选题+热点/爆款做原创短视频脚本与封面，产出草稿供发布与数据助手。
7. **评论管理**：评论采集、起草回复、情感分析；回复需审批/门禁后发布。

**管线关系：** 热门监控 → 日报/摘要 → 爆款拆解 → 拆解框架 → 二创/原创 → 草稿+配图 → 自动发布 → 发布日志 → 数据助手 + 评论管理 → 反馈至爆款拆解与热门监控。

## 主智能体

- 本渠道主智能体目录：`1-douyin-specialist`（若存在 `*-strategist` 目录，保持不重命名并作为该组最后扩展角色）。

## 智能体清单

| 序号 | Agent id                | 展示名         | 目录                           | 职责摘要 |
|------|-------------------------|----------------|--------------------------------|----------|
| 1    | douyin-hot-monitor      | 抖音热门监控   | 2-douyin-hot-monitor          | 每日/按需搜索抖音热点与爆款短视频，产出日报或摘要 |
| 2    | douyin-viral-breakdown  | 抖音爆款拆解   | 3-douyin-viral-breakdown      | 对爆款短视频做拆解，产出结构化拆解框架 |
| 3    | douyin-rewrite          | 抖音二创       | 4-douyin-rewrite               | 根据拆解框架与主题创作新文案与封面/脚本 |
| 4    | douyin-publisher        | 抖音自动发布   | 5-douyin-publisher             | 将已通过草稿发布到抖音并记录结果（需开放平台/浏览器） |
| 5    | douyin-data-assistant   | 抖音数据助手   | 6-douyin-data-assistant        | 解析数据、交叉验证效果、反馈给爆款拆解 |
| 6    | douyin-write            | 抖音原创       | 7-douyin-write                 | 强调原创：用户选题+热点/爆款做原创短视频内容，产出草稿 |
| 7    | douyin-comment-manager  | 抖音评论管理   | 8-douyin-comment-manager      | 评论采集、起草回复、情感分析；回复需审批/门禁后发布 |

## 智能工作执行链路

七件套按以下链路协同执行；可按时序触发（如每日）或按需触发单环节。

| 步骤 | 环节 | 智能体 | 输入 | 输出 | 说明 |
|------|------|--------|------|------|------|
| 1 | 热门监控 | douyin-hot-monitor | 关键词/品类/时间范围 | 日报或按需摘要（热点、爆款列表） | 入口；可为定时或人工触发 |
| 2 | 爆款拆解 | douyin-viral-breakdown | 日报/摘要中的爆款链接或列表 | 拆解框架（标题、钩子、结构、主题） | 消费监控产出，供二创与数据侧使用 |
| 3a | 二创 | douyin-rewrite | 拆解框架 + 主题 | 草稿（文案 + 封面 + 配图） | 基于拆解做差异化二创，不发布 |
| 3b | 原创 | douyin-write | 用户选题 + 热点/爆款洞察 | 草稿（文案 + 封面 + 配图） | 独立于拆解的原创内容生产 |
| 4 | 自动发布 | douyin-publisher | 已审核草稿 | 发布结果日志（链接、时间、状态） | 仅发布已通过审核内容；发布前压缩图片 |
| 5 | 数据助手 | douyin-data-assistant | 发布日志 + 互动数据 | 可执行反馈（关键词/拆解维度/优先主题） | 交叉验证效果，反馈至爆款拆解与监控 |
| 6 | 评论管理 | douyin-comment-manager | 文章/账号评论源 | 回复草稿 + 情感摘要 | 回复须审批/门禁后由人工或流程发布 |

**闭环：** 数据助手的反馈驱动爆款拆解调整搜索与拆解标准，热门监控可据此调整关键词与范围，形成「监控 → 拆解 → 内容 → 发布 → 数据 → 反馈」闭环。

**并行与触发：** 3a 二创与 3b 原创可并行；评论管理可与数据助手并行。执行顺序 1 → 2 → (3a 或 3b) → 4 → 5/6；步骤 5、6 可持续运行或按周期执行。

## 预设技能（按评估结论，去重取最优）

以下为 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md) 最终推荐；同能力只选一个来源。

| 步骤 | Agent id                | 推荐技能 | 来源 | 说明 |
|------|-------------------------|----------|------|------|
| 1 | douyin-hot-monitor      | douyin-hot-trend, baoyu-url-to-markdown, baoyu-format-markdown | ClawHub + skills.sh | 热榜+抓取+日报格式 |
| 2 | douyin-viral-breakdown  | douyin-downloader 或 douyin-video-fetch, baoyu-format-markdown | ClawHub + skills.sh | 视频下载+拆解格式 |
| 3a | douyin-rewrite          | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面与配图 |
| 3b | douyin-write            | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | douyin-publisher        | douyin-publish, baoyu-compress-image | ClawHub + skills.sh | 发布+压缩；须遵守平台 ToS |
| 5 | douyin-data-assistant   | baoyu-format-markdown | skills.sh | 报告格式 |
| 6 | douyin-comment-manager  | （按需选评论采集与回复技能） | ClawHub/skills.sh | 评论拉取、回复草稿 |

### 安装前置与唯一命令来源

**第一步：安装 SkillHub CLI**（仅首次需要）

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**全部技能安装/卸载以本页下方「七件套全部可使用的技能」或 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 为准。** 安装后目录名需与 config 中 `skills` 一致。勿在 TOOLS.md 存凭证。发布与抓取须遵守抖音开放平台与平台 ToS。

### 七件套全部可使用的技能：全部安装 / 全部卸载命令

与 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 一致。

**全部安装命令**

```bash
# ClawHub
clawhub install douyin-hot-trend --workdir ~/.openclaw;
clawhub install douyin-downloader --workdir ~/.openclaw;
clawhub install douyin-publish --workdir ~/.openclaw;

# skills.sh
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g;
```

**全部卸载命令**

```bash
# ClawHub
clawhub uninstall douyin-hot-trend;
clawhub uninstall douyin-downloader;
clawhub uninstall douyin-publish;

# skills.sh
npx skills remove baoyu-url-to-markdown;
npx skills remove baoyu-format-markdown;
npx skills remove baoyu-cover-image;
npx skills remove baoyu-article-illustrator;
npx skills remove baoyu-compress-image;
npx skills remove baoyu-translate;
npx skills remove baoyu-infographic;
npx skills remove baoyu-comic;
```

## 配置说明

- **Workspace：** `~/.openclaw/workspace-douyin-<agentId>`。
- **Config 片段：** `config/openclaw-douyin-fragment.json`。
- **路由：** 通过 bindings 将渠道或会话路由到各 agent id。

## 初始化命令（按执行链路顺序）

### 添加七件套

```bash
openclaw agents add douyin-hot-monitor       --workspace ~/.openclaw/workspace-douyin-hot-monitor;
openclaw agents add douyin-viral-breakdown   --workspace ~/.openclaw/workspace-douyin-viral-breakdown;
openclaw agents add douyin-rewrite           --workspace ~/.openclaw/workspace-douyin-rewrite;
openclaw agents add douyin-write             --workspace ~/.openclaw/workspace-douyin-write;
openclaw agents add douyin-publisher         --workspace ~/.openclaw/workspace-douyin-publisher;
openclaw agents add douyin-data-assistant    --workspace ~/.openclaw/workspace-douyin-data-assistant;
openclaw agents add douyin-comment-manager   --workspace ~/.openclaw/workspace-douyin-comment-manager;
```

### 按渠道绑定（示例：wecom）

```bash
openclaw agents bind --agent douyin-hot-monitor       --bind wecom:douyin-hot-monitor;
openclaw agents bind --agent douyin-viral-breakdown   --bind wecom:douyin-viral-breakdown;
openclaw agents bind --agent douyin-rewrite           --bind wecom:douyin-rewrite;
openclaw agents bind --agent douyin-write             --bind wecom:douyin-write;
openclaw agents bind --agent douyin-publisher         --bind wecom:douyin-publisher;
openclaw agents bind --agent douyin-data-assistant    --bind wecom:douyin-data-assistant;
openclaw agents bind --agent douyin-comment-manager   --bind wecom:douyin-comment-manager;
```

### 删除七件套（需先解除绑定）

```bash
openclaw agents remove douyin-hot-monitor;
openclaw agents remove douyin-viral-breakdown;
openclaw agents remove douyin-rewrite;
openclaw agents remove douyin-write;
openclaw agents remove douyin-publisher;
openclaw agents remove douyin-data-assistant;
openclaw agents remove douyin-comment-manager;
```

## 文件结构（每智能体）

与 zhihu、weibo 一致：`AGENTS.md`、`zh-CN/AGENTS.md`、`SOUL.md`、`IDENTITY.md`、`TOOLS.md`、`BOOTSTRAP.md`、`HEARTBEAT.md`、`USER.md` 及 zh-CN 对应文件。

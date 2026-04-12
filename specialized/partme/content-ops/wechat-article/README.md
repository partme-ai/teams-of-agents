# 公众号文章生产管线 (WeChat Article Agents)

> 基于 [ClawHub wechat 技能](https://clawhub.ai/skills?sort=downloads&q=wechat) 与 [skills.sh wechat](https://skills.sh/?q=wechat)（**以 ClawHub 为主，两源取最优**），为**微信公众号文章**提供统一内容管线七件套：热门监控、爆款拆解、二创、原创、自动发布、数据助手、评论管理。与 openclaw-agents 其他领域（company / discord / telegram 等）并列。

## 技能选型

| 序号 | 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|------|----------|--------------|----------|
| 1 | **ClawHub（为主）** | [clawhub.ai/skills?q=wechat](https://clawhub.ai/skills?sort=downloads&q=wechat) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug> --workdir ~/.openclaw;` |
| 2 | **skills.sh（取最优）** | [skills.sh/?q=wechat](https://skills.sh/?q=wechat) | [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md) | `npx skills add <owner/repo> --skill <名>` |

## 技能评估结论（摘录）

> 完整评估见 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md)。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能，减少重复。**

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown | baoyu-url-to-markdown | wechat-article-fetcher, wechat-article-to-markdown |
| 2 | 公众号搜索 | wechat-article-search（ClawHub） | skills.sh 同源只装一处 |
| 3 | 正文提取 | wechat-article-extractor（freestylefly） | scrapling-web-fetch 作补充 |
| 4 | 报告/拆解格式 | baoyu-format-markdown | — |
| 5 | 封面/长文配图 | baoyu-cover-image, baoyu-article-illustrator | huashu-wechat-image 等不替代 |
| 6 | 发布到公众号 | baoyu-post-to-wechat | wechat-article-publisher, wechat-ai-publisher, md2wechat 等不重复 |
| 7 | MD→微信 HTML | baoyu-markdown-to-html | — |
| 8 | 图片压缩 | baoyu-compress-image | — |
| 9 | 监控/阅读量/舆情 | wechat-mp-cn | — |
| 10 | 评论回复建议 | wechat-auto-reply-assistant | — |


## 浏览器已登录态补充入口

对于热点读取、站内搜索、趋势抓取这类场景，可补充使用：

- `opencli-skill`：热点读取、站内搜索、趋势抓取
- `baoyu-url-to-markdown`：链接正文抓取与转 markdown
- `baoyu-format-markdown`：日报、拆解报告、趋势周报规范化输出

推荐链路：

```text
opencli-skill -> 热点 / 热榜 / 搜索结果
baoyu-url-to-markdown -> 正文抓取
baoyu-format-markdown -> 日报 / 拆解报告
```

边界：

- 适合作为浏览器登录态数据入口补充，不替代现有平台专用技能
- 写操作默认人工确认、小号测试、低频执行，不作为自动执行基线

## 补充能力（完整栈）

七件套之外本管线可用上的补充能力（与 [SKILLS-EVALUATION.md §8.1](./SKILLS-EVALUATION.md) 一致）：

| 序号 | 补充能力 | 用途 | 推荐技能 | 来源 |
|------|----------|------|----------|------|
| 1 | 监控/阅读量/舆情 | 公众号文章监控、阅读量、舆情 | wechat-mp-cn | ClawHub |
| 2 | 评论回复建议 | 回复草稿生成 | wechat-auto-reply-assistant | ClawHub |
| 3 | 反爬/正文抓取补充 | viral-breakdown 遇反爬时 | scrapling-web-fetch | ClawHub |
| 4 | 多语言与翻译 | 多语言内容、翻译 | baoyu-translate | skills.sh |
| 5 | 信息图/漫画风配图 | 丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh |

## 必须保证的七个环节

1. **热门监控**：每日/按需搜索公众号/微信生态行业热点与爆款文章，产出日报或摘要，供爆款拆解与数据助手使用。
2. **爆款拆解**：自动搜索平台关于行业热点和爆款文章，产出结构化拆解框架（标题/钩子/结构/主题等），供二创与数据助手使用。
3. **二创**：根据拆解框架和结合主题进行新文案和配图（封面 + 文中插图），产出草稿供发布与数据助手使用。
4. **原创**：强调原创；用户主图+热点/爆款做原创文章，产出草稿供发布与数据助手。
5. **自动发布**：将已通过的草稿发布到微信公众号（文章/贴图），并记录发布结果供数据助手分析。
6. **数据助手**：解析文案数据、主题方向，交叉验证效果，将可执行结论反馈给爆款拆解，用于修正和提升（形成闭环）。
7. **评论管理**：评论采集、起草回复、情感分析；回复需审批/门禁后发布。

**管线关系：** 热门监控 → 日报/摘要 → 爆款拆解 → 拆解框架 → 二创/原创 → 草稿+配图 → 自动发布 → 发布日志 → 数据助手 + 评论管理 → 反馈至爆款拆解与热门监控。

## 主智能体

- 本渠道主智能体目录：`1-wechat-article-specialist`（若存在 `*-strategist` 目录，保持不重命名并作为该组最后扩展角色）。

## 智能体清单

| 序号 | Agent id                        | 展示名           | 目录                               | 职责摘要 |
|------|---------------------------------|------------------|------------------------------------|----------|
| 1    | wechat-article-hot-monitor      | 公众号热门监控   | 2-wechat-article-hot-monitor      | 每日/按需搜索公众号/微信生态热点与爆款，产出日报或摘要供拆解与数据助手 |
| 2    | wechat-article-viral-breakdown | 公众号爆款拆解   | 3-wechat-article-viral-breakdown  | 自动搜索行业热点与爆款文章，产出结构化拆解框架 |
| 3    | wechat-article-rewrite          | 公众号二创       | 4-wechat-article-rewrite          | 根据拆解框架与主题创作新文案与封面/文中插图 |
| 4    | wechat-article-write            | 公众号原创       | 5-wechat-article-write            | 强调原创：用户主图+热点/爆款做原创文章，产出草稿供发布与数据助手 |
| 5    | wechat-article-publisher        | 公众号自动发布   | 6-wechat-article-publisher        | 将已通过草稿发布到公众号并记录结果 |
| 6    | wechat-article-data-assistant   | 公众号数据助手   | 7-wechat-article-data-assistant   | 解析数据、交叉验证效果、可执行反馈给爆款拆解 |
| 7    | wechat-article-comment-manager  | 公众号评论管理   | 8-wechat-article-comment-manager  | 评论采集、起草回复、情感分析；回复需审批/门禁后发布 |

## 智能工作执行链路

七件套按以下链路协同执行；可按时序触发（如每日）或按需触发单环节。

| 步骤 | 环节 | 智能体 | 输入 | 输出 | 说明 |
|------|------|--------|------|------|------|
| 1 | 热门监控 | wechat-article-hot-monitor | 关键词/品类/时间范围 | 日报或按需摘要（热点、爆款列表） | 入口；可为定时或人工触发 |
| 2 | 爆款拆解 | wechat-article-viral-breakdown | 日报/摘要中的爆款链接或列表 | 拆解框架（标题、钩子、结构、主题） | 消费监控产出，供二创与数据侧使用 |
| 3a | 二创 | wechat-article-rewrite | 拆解框架 + 主题 | 草稿（文案 + 封面 + 配图） | 基于拆解做差异化二创，不发布 |
| 3b | 原创 | wechat-article-write | 用户选题 + 热点/爆款洞察 | 草稿（文案 + 封面 + 配图） | 独立于拆解的原创内容生产 |
| 4 | 自动发布 | wechat-article-publisher | 已审核草稿 | 发布结果日志（链接、时间、状态） | 仅发布已通过审核内容；发布前压缩图片 |
| 5 | 数据助手 | wechat-article-data-assistant | 发布日志 + 互动数据 | 可执行反馈（关键词/拆解维度/优先主题） | 交叉验证效果，反馈至爆款拆解与监控 |
| 6 | 评论管理 | wechat-article-comment-manager | 文章/账号评论源 | 回复草稿 + 情感摘要 | 回复须审批/门禁后由人工或流程发布 |

**闭环：** 数据助手的反馈驱动爆款拆解调整搜索与拆解标准，热门监控可据此调整关键词与范围，形成「监控 → 拆解 → 内容 → 发布 → 数据 → 反馈」闭环。

**并行与触发：** 3a 二创与 3b 原创可并行；评论管理可与数据助手并行。执行顺序 1 → 2 → (3a 或 3b) → 4 → 5/6；步骤 5、6 可持续运行或按周期执行。

## 预设技能（按评估结论，去重取最优）

以下为 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md) 最终推荐：每个 Agent 只保留必要且不重复的技能；同能力只选一个来源。

| 步骤 | Agent id                        | 推荐技能 | 来源 | 说明 |
|------|---------------------------------|----------|------|------|
| 1 | wechat-article-hot-monitor     | baoyu-url-to-markdown, baoyu-format-markdown | skills.sh | 抓取链接、日报格式；若需阅读量/舆情再加 wechat-mp-cn |
| 2 | wechat-article-viral-breakdown  | wechat-article-search, wechat-article-extractor, baoyu-format-markdown | ClawHub + skills.sh | 搜索用 ClawHub；提取用 freestylefly；遇反爬可加 scrapling-web-fetch |
| 3a | wechat-article-rewrite         | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面与长文配图 |
| 3b | wechat-article-write           | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | wechat-article-publisher       | baoyu-post-to-wechat, baoyu-markdown-to-html, baoyu-compress-image | skills.sh | 发布+排版+压缩（wechat-ai-publisher 可不装） |
| 5 | wechat-article-data-assistant  | baoyu-format-markdown；可选 wechat-mp-cn | skills.sh；ClawHub | 报告格式必选；要数据再选 wechat-mp-cn |
| 6 | wechat-article-comment-manager | wechat-auto-reply-assistant；评论采集按接口/自研 | ClawHub | 回复草稿用 ClawHub；采集需另配 |

### 安装前置与唯一命令来源

**第一步：安装 SkillHub CLI**（仅首次需要）

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**全部技能安装/卸载以本页下方「七件套全部可使用的技能」或 [SKILLS-EVALUATION.md §8.3](./SKILLS-EVALUATION.md) 为准。** 安装后目录名需与 config 中 `skills` 一致。发布智能体需配置公众号凭证（环境变量或 EXTEND.md）；勿在 TOOLS.md 或工作区存凭证。

### 七件套全部可使用的技能：全部安装 / 全部卸载命令

与 [SKILLS-EVALUATION.md §8.3](./SKILLS-EVALUATION.md) 一致；能用上的全列（同质取一，可并存全列）。

**全部安装命令**

```bash
# ClawHub — 公众号七件套 + 补充
clawhub install wechat-article-search --workdir ~/.openclaw;
clawhub install wechat-mp-cn --workdir ~/.openclaw;
clawhub install wechat-auto-reply-assistant --workdir ~/.openclaw;
clawhub install scrapling-web-fetch --workdir ~/.openclaw;

# skills.sh — 抓取、格式、提取、配图、发布、排版、压缩、补充
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;
npx skills add freestylefly/wechat-article-extractor-skill --skill wechat-article-extractor -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-post-to-wechat -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-markdown-to-html -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g;

```

**全部卸载命令**

```bash
# ClawHub
clawhub uninstall wechat-article-search;
clawhub uninstall wechat-mp-cn;
clawhub uninstall wechat-auto-reply-assistant;
clawhub uninstall scrapling-web-fetch;

# skills.sh
npx skills remove baoyu-url-to-markdown;
npx skills remove baoyu-format-markdown;
npx skills remove wechat-article-extractor;
npx skills remove baoyu-cover-image;
npx skills remove baoyu-article-illustrator;
npx skills remove baoyu-post-to-wechat;
npx skills remove baoyu-markdown-to-html;
npx skills remove baoyu-compress-image;
npx skills remove baoyu-translate;
npx skills remove baoyu-infographic;
npx skills remove baoyu-comic;
```

若 CLI 为 `npx skillsadd`（无空格），以 skills.sh 文档为准。

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
openclaw agents add wechat-article-specialist        --workspace ~/.openclaw/workspace-wechat-article-specialist;
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
openclaw agents bind --agent wechat-article-specialist       --bind wecom:wechat-article-specialist;
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

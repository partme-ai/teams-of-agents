# 小红书内容管线 (Rednode / Xiaohongshu Agents)

> 基于 [ClawHub xiaohongshu 技能](https://clawhub.ai/skills?sort=downloads&q=xiaohongshu)（优先）与 [skills.sh baoyu / xiaohongshu](https://skills.sh/?q=baoyu)（后补），为**小红书**提供内容管线七件套：热门监控、爆款拆解、二创、原创、自动发布、数据助手、评论管理。本目录为独立 xiaohongshu 管线，可单独部署。

## 技能选型（ClawHub 优先，skills.sh 后补）

**技能来源区分：**

| 序号 | 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|------|----------|--------------|----------|
| 1 | **ClawHub（优先）** | [clawhub.ai/skills?q=xiaohongshu](https://clawhub.ai/skills?sort=downloads&q=xiaohongshu) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug>` |
| 2 | **skills.sh（后补）** | [skills.sh/?q=xiaohongshu](https://skills.sh/?q=xiaohongshu)、[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu) | [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md) | `npx skills add <owner/repo> --skill <名>` |

## 技能评估结论（摘录）

> 完整评估见 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md)。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。** ClawHub 技能按**评分优选**（见 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 表）。  
> **完整技能栈**（七件套 + 标题筛选、爆款筛选、标题/算法优化、原创辅导、审核复盘、视频分析、多语言等补充）见 [SKILLS-EVALUATION.md § 七、完整技能栈](./SKILLS-EVALUATION.md#七完整技能栈七件套--补充能力)。

| 序号 | 能力 | 首选（按 ClawHub 评分） | 备选/不重复装 |
|------|------|-------------------------|----------------|
| 1 | 链接→Markdown/报告格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 小红书配图/封面 | baoyu-xhs-images, baoyu-cover-image, baoyu-article-illustrator | — |
| 3 | 发布到小红书 | xiaohongshu-mcp (3.633) | xiaohongshu-mcp-skill、xiaohongshu-mcp-skills、assistant-operator 选一 |
| 4 | 搜索/趋势/分析 | xiaohongshu-mcp, xiaohongshu-cn (3.584) | xiaohongshu-deep-research, xiaohongshu-search-summarizer |
| 5 | 深度调研/拆解 | xiaohongshu-deep-research (3.568), xiaohongshu-search-summarizer (3.275) | — |
| 6 | 内容/原创策略 | xiaohongshu-content (3.349), xiaohongshu-founder-growth-writer (3.338) | — |
| 7 | 图片压缩 | baoyu-compress-image | — |
| 8 | 评论回复 | xiaohongshu-mcp / xiaohongshu-mcp-skills；reply-assistant 按需 | — |

**补充能力（完整栈）** — 在七件套基础上扩展，覆盖选题→筛选→拆解→创作→发布→数据→评论全链路：

| 序号 | 补充能力 | 用途 | 推荐技能 | 来源 |
|------|----------|------|----------|------|
| 1 | 标题筛选 / 标题质量 | 按爆款标题范式筛选笔记，监控/拆解前预筛 | xiaohongshu-content、xiaohongshu-algorithm-optimizer | ClawHub |
| 2 | 标题与首图优化 | 优化标题、首图、标签，提高曝光与互动 | xiaohongshu-algorithm-optimizer、xhs-writing-coach | ClawHub |
| 3 | 爆款/视频筛选 | 按细分领域筛新鲜/爆款视频，带 xsec_token URL | xhs-video-finder | ClawHub |
| 4 | 原创与互动辅导 | 标题/正文/标签/封面/评论引导、互动提升 | xhs-writing-coach | ClawHub |
| 5 | 审核与复盘 | 选题→草稿→飞书审核→发布→复盘 | openclaw-xiaohongshu-ops、clawnote | ClawHub |
| 6 | 视频下载与分析 | 下载视频、提取语音/总结，供拆解与数据 | xhs-video-downloader、xhs-video-analyzer | ClawHub |
| 7 | 评论破冰与回复 | 破冰句、评论情感与回复建议 | xiaohongshu-first-line、xiaohongshu-reply-assistant | ClawHub |
| 8 | 多语言 | 多语言与翻译 | baoyu-translate | skills.sh |
| 9 | 信息图/漫画风 | 丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh |

更细的映射与同质取舍见 [SKILLS-EVALUATION.md § 七、完整技能栈](./SKILLS-EVALUATION.md#七完整技能栈七件套--补充能力)。

- **全仓库技能总览与 Baoyu 归类**见 [docs/SKILLS-MASTER.md](../../docs/SKILLS-MASTER.md)。

## 智能体清单

| 序号 | Agent id                      | 展示名           | 目录                               | 职责摘要 |
|------|-------------------------------|------------------|------------------------------------|----------|
| 1    | xiaohongshu-hot-monitor       | 小红书热门监控   | 1-xiaohongshu-hot-monitor          | 每日/按需搜索行业热点与爆款，产出日报或摘要供拆解与数据助手 |
| 2    | xiaohongshu-viral-breakdown   | 小红书爆款拆解   | 2-xiaohongshu-viral-breakdown      | 自动搜索平台行业热点与爆款，产出结构化拆解框架 |
| 3    | xiaohongshu-rewrite           | 小红书二创       | 3-xiaohongshu-rewrite              | 根据拆解框架与主题创作新文案与配图方向 |
| 4    | xiaohongshu-write             | 小红书原创       | 4-xiaohongshu-write                | 强调原创：用户主图+热点/爆款做原创内容，产出草稿供发布与数据助手 |
| 5    | xiaohongshu-publisher         | 小红书自动发布   | 5-xiaohongshu-publisher            | 将已通过草稿发布到小红书并记录结果 |
| 6    | xiaohongshu-data-assistant    | 小红书数据助手   | 6-xiaohongshu-data-assistant       | 解析数据、交叉验证效果、反馈爆款拆解 |
| 7    | xiaohongshu-comment-manager   | 小红书评论管理   | 7-xiaohongshu-comment-manager      | 评论采集、起草回复、情感分析；回复需审批/门禁后发布 |

**管线关系：** 热门监控 → 日报/摘要 → 爆款拆解 → 拆解框架 → 二创/原创 → 草稿+配图 → 自动发布 → 发布日志 → 数据助手 + 评论管理 → 反馈至爆款拆解与热门监控。

## 智能工作执行链路

七件套按以下链路协同执行；可按时序触发（如每日）或按需触发单环节。

| 步骤 | 环节 | 智能体 | 输入 | 输出 | 说明 |
|------|------|--------|------|------|------|
| 1 | 热门监控 | xiaohongshu-hot-monitor | 关键词/品类/时间范围 | 日报或按需摘要（热点、爆款列表） | 入口；可为定时或人工触发 |
| 2 | 爆款拆解 | xiaohongshu-viral-breakdown | 日报/摘要中的爆款链接或列表 | 拆解框架（标题、钩子、结构、主题） | 消费监控产出，供二创与数据侧使用 |
| 3a | 二创 | xiaohongshu-rewrite | 拆解框架 + 主题 | 草稿（文案 + 封面 + 配图） | 基于拆解做差异化二创，不发布 |
| 3b | 原创 | xiaohongshu-write | 用户选题 + 热点/爆款洞察 | 草稿（文案 + 封面 + 配图） | 独立于拆解的原创内容生产 |
| 4 | 自动发布 | xiaohongshu-publisher | 已审核草稿 | 发布结果日志（链接、时间、状态） | 仅发布已通过审核内容；发布前压缩图片 |
| 5 | 数据助手 | xiaohongshu-data-assistant | 发布日志 + 互动数据 | 可执行反馈（关键词/拆解维度/优先主题） | 交叉验证效果，反馈至爆款拆解与监控 |
| 6 | 评论管理 | xiaohongshu-comment-manager | 文章/账号评论源 | 回复草稿 + 情感摘要 | 回复须审批/门禁后由人工或流程发布 |

**闭环：** 数据助手的反馈驱动爆款拆解调整搜索与拆解标准，热门监控可据此调整关键词与范围，形成「监控 → 拆解 → 内容 → 发布 → 数据 → 反馈」闭环。

**并行与触发：** 3a 二创与 3b 原创可并行；评论管理可与数据助手并行。执行顺序 1 → 2 → (3a 或 3b) → 4 → 5/6；步骤 5、6 可持续运行或按周期执行。

## 预设技能（按评估结论，去重取最优）

以下为 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md) 最终推荐；同能力只选一个来源。

| 步骤 | Agent id                      | 推荐技能 | 来源 | 说明 |
|------|-------------------------------|----------|------|------|
| 1 | xiaohongshu-hot-monitor       | baoyu-url-to-markdown, baoyu-format-markdown；可选 xiaohongshu-cn | skills.sh；ClawHub | 抓取+日报格式；可选趋势 |
| 2 | xiaohongshu-viral-breakdown   | baoyu-url-to-markdown, baoyu-format-markdown；可选 xiaohongshu-mcp, xiaohongshutools | skills.sh；ClawHub | 抓取成文+拆解格式；可选平台搜索 |
| 3a | xiaohongshu-rewrite           | baoyu-xhs-images, baoyu-cover-image, baoyu-article-illustrator | skills.sh | 小红书配图与封面 |
| 3b | xiaohongshu-write             | baoyu-xhs-images, baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | xiaohongshu-publisher         | baoyu-compress-image；xiaohongshu-mcp 或 xiaohongshu-publish | skills.sh + ClawHub | 压缩+发布 |
| 5 | xiaohongshu-data-assistant    | baoyu-format-markdown；可选 xiaohongshu-cn | skills.sh；ClawHub | 报告格式；可选数据分析 |
| 6 | xiaohongshu-comment-manager   | xiaohongshu-reply-assistant；评论采集按需 | ClawHub | 回复建议；采集需另配 |

### 七件套全部可使用的技能：全部安装 / 全部卸载命令

**全部不冲突**：来自 [CLAWHUB-SKILLS.md 按用途分类](./CLAWHUB-SKILLS.md)——同质只取 1 个首选（如发布只列 xiaohongshu-mcp），可并存的全部列入；config 中 `agents.list[].skills` 填写的为「安装后目录名」（ClawHub 即 `<slug>`，skills.sh 即技能名）。若某技能与当前环境冲突可单独注释该行。

**全部安装命令（复制执行即可）**

```bash
# ClawHub — 监控/搜索/抓取/趋势
clawhub install xiaohongshu-mcp --workdir ~/.openclaw;
clawhub install xiaohongshu-cn --workdir ~/.openclaw;
clawhub install xiaohongshutools --workdir ~/.openclaw;
clawhub install xiaohongshu-deep-research --workdir ~/.openclaw;
clawhub install xiaohongshu-search-summarizer --workdir ~/.openclaw;
clawhub install xiaohongshu-skill --workdir ~/.openclaw;
clawhub install xiaohongshu-api --workdir ~/.openclaw;
clawhub install xhs-research-daily --workdir ~/.openclaw;

# ClawHub — 发布（可并存，同质已只取 mcp）
clawhub install xiaohongshu-publish --workdir ~/.openclaw;
clawhub install xiaohongshu-publisher --workdir ~/.openclaw;
clawhub install xiaohongshu-post --workdir ~/.openclaw;
clawhub install redbook-browser-ops --workdir ~/.openclaw;
clawhub install xiaohongshu-mcporter-publish --workdir ~/.openclaw;
clawhub install xiaohongshu-video-publish --workdir ~/.openclaw;
clawhub install auto-publisher --workdir ~/.openclaw;
clawhub install dragon-xiaohongshu --workdir ~/.openclaw;
clawhub install xiaohongshu-publish-skill --workdir ~/.openclaw;
clawhub install xiaohongshu-publish-wangzh --workdir ~/.openclaw;
clawhub install xhs-publisher --workdir ~/.openclaw;
clawhub install xhsredbook --workdir ~/.openclaw;
clawhub install xiaohongshu-operate --workdir ~/.openclaw;

# ClawHub — 内容/二创/原创（viral 同质只取 viral-content）
clawhub install xiaohongshu-content --workdir ~/.openclaw;
clawhub install xiaohongshu-founder-growth-writer --workdir ~/.openclaw;
clawhub install xhs-content-creator --workdir ~/.openclaw;
clawhub install xiaohongshu-viral-content --workdir ~/.openclaw;
clawhub install xhs-writing-coach --workdir ~/.openclaw;
clawhub install xiaohongshu-article-generator --workdir ~/.openclaw;
clawhub install xiaohongshu-algorithm-optimizer --workdir ~/.openclaw;
clawhub install xiaohongshu-ai-money-guide --workdir ~/.openclaw;

# ClawHub — 评论/互动
clawhub install xiaohongshu-reply-assistant --workdir ~/.openclaw;
clawhub install rednote-mac --workdir ~/.openclaw;
clawhub install xiaohongshu-comment --workdir ~/.openclaw;
clawhub install xiaohongshu-first-line --workdir ~/.openclaw;

# ClawHub — 视频
clawhub install xhs-video-finder --workdir ~/.openclaw;
clawhub install xhs-video-downloader --workdir ~/.openclaw;
clawhub install xhs-video-analyzer --workdir ~/.openclaw;

# ClawHub — 运营（同质只取 openclaw）
clawhub install openclaw-xiaohongshu-ops --workdir ~/.openclaw;
clawhub install zeelin-xiaohongshu-autopost --workdir ~/.openclaw;

# ClawHub — 登录/运维
clawhub install xiaohongshu-login --workdir ~/.openclaw;
clawhub install xiaohongshu-mcp-patch --workdir ~/.openclaw;
clawhub install jackwener-xhs-cli --workdir ~/.openclaw;

# ClawHub — 图文/信息图
clawhub install xiaohongshu-generator --workdir ~/.openclaw;
clawhub install xhs-md2pic --workdir ~/.openclaw;
clawhub install xiaohongshu-post-gen --workdir ~/.openclaw;
clawhub install xiaohongshu-auto-publish --workdir ~/.openclaw;

# ClawHub — 跨平台/迁移（餐厅只取一个）
clawhub install restaurant-crosscheck --workdir ~/.openclaw;
clawhub install kb-social-publisher --workdir ~/.openclaw;
clawhub install wechat-to-xiaohongshu --workdir ~/.openclaw;
clawhub install social-copy-generator --workdir ~/.openclaw;
clawhub install content-repurpose-studio --workdir ~/.openclaw;

# ClawHub — 其它
clawhub install xhs-comic-creator --workdir ~/.openclaw;

# skills.sh
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-xhs-images -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g;
```

**全部卸载命令（复制执行即可）**

```bash
# ClawHub — 监控/搜索/抓取/趋势
clawhub uninstall xiaohongshu-mcp;
clawhub uninstall xiaohongshu-cn;
clawhub uninstall xiaohongshutools;
clawhub uninstall xiaohongshu-deep-research;
clawhub uninstall xiaohongshu-search-summarizer;
clawhub uninstall xiaohongshu-skill;
clawhub uninstall xiaohongshu-api;
clawhub uninstall xhs-research-daily;

# ClawHub — 发布
clawhub uninstall xiaohongshu-publish;
clawhub uninstall xiaohongshu-publisher;
clawhub uninstall xiaohongshu-post;
clawhub uninstall redbook-browser-ops;
clawhub uninstall xiaohongshu-mcporter-publish;
clawhub uninstall xiaohongshu-video-publish;
clawhub uninstall auto-publisher;
clawhub uninstall dragon-xiaohongshu;
clawhub uninstall xiaohongshu-publish-skill;
clawhub uninstall xiaohongshu-publish-wangzh;
clawhub uninstall xhs-publisher;
clawhub uninstall xhsredbook;
clawhub uninstall xiaohongshu-operate;

# ClawHub — 内容/二创/原创
clawhub uninstall xiaohongshu-content;
clawhub uninstall xiaohongshu-founder-growth-writer;
clawhub uninstall xhs-content-creator;
clawhub uninstall xiaohongshu-viral-content;
clawhub uninstall xhs-writing-coach;
clawhub uninstall xiaohongshu-article-generator;
clawhub uninstall xiaohongshu-algorithm-optimizer;
clawhub uninstall xiaohongshu-ai-money-guide;

# ClawHub — 评论/互动
clawhub uninstall xiaohongshu-reply-assistant;
clawhub uninstall rednote-mac;
clawhub uninstall xiaohongshu-comment;
clawhub uninstall xiaohongshu-first-line;

# ClawHub — 视频
clawhub uninstall xhs-video-finder;
clawhub uninstall xhs-video-downloader;
clawhub uninstall xhs-video-analyzer;

# ClawHub — 运营
clawhub uninstall openclaw-xiaohongshu-ops;
clawhub uninstall zeelin-xiaohongshu-autopost;

# ClawHub — 登录/运维
clawhub uninstall xiaohongshu-login;
clawhub uninstall xiaohongshu-mcp-patch;
clawhub uninstall jackwener-xhs-cli;

# ClawHub — 图文/信息图
clawhub uninstall xiaohongshu-generator;
clawhub uninstall xhs-md2pic;
clawhub uninstall xiaohongshu-post-gen;
clawhub uninstall xiaohongshu-auto-publish;

# ClawHub — 跨平台/迁移
clawhub uninstall restaurant-crosscheck;
clawhub uninstall kb-social-publisher;
clawhub uninstall wechat-to-xiaohongshu;
clawhub uninstall social-copy-generator;
clawhub uninstall content-repurpose-studio;

# ClawHub — 其它
clawhub uninstall xhs-comic-creator;

# skills.sh
npx skills remove baoyu-url-to-markdown;
npx skills remove baoyu-format-markdown;
npx skills remove baoyu-xhs-images;
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

**全部技能安装/卸载**：以本页上方「全部安装命令」与「全部卸载命令」为准（唯一完整列表）；安装后目录名需与 config 中 `skills` 一致。若使用 `npx skills add`，以 [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md) 为准。

## 配置说明

- **Workspace**：各智能体 workspace 指向本目录下对应子目录（如 `<REPO_ROOT>/openclaw-agents/content-ops/xiaohongshu/1-xiaohongshu-viral-breakdown`），或部署时复制/链接到 `~/.openclaw/workspace-xiaohongshu-viral-breakdown` 等。
- **Config 片段**：见仓库根目录 `config/openclaw-xiaohongshu-fragment.json`，可合并进主 openclaw 配置；使用前将 `<REPO_ROOT>` 替换为 openclaw-agents 实际路径。
- **路由**：按渠道或用户身份将会话绑定到对应 agent id（见上方智能体清单）。

## 初始化命令

以下命令在 OpenClaw 配置已就绪的前提下执行；`--workspace` 使用本地路径（如 `~/.openclaw/workspace-<agent-id>`），需先将本仓库 `content-ops/xiaohongshu/1-...`～`content-ops/xiaohongshu/7-...` 复制或链接到对应 workspace 目录。

### 1. 查看当前智能体列表

```bash
openclaw agents list
```

### 2. 添加小红书七件套（7 个，按执行链路顺序）

```bash
openclaw agents add xiaohongshu-hot-monitor       --workspace ~/.openclaw/workspace-xiaohongshu-hot-monitor;
openclaw agents add xiaohongshu-viral-breakdown   --workspace ~/.openclaw/workspace-xiaohongshu-viral-breakdown;
openclaw agents add xiaohongshu-rewrite          --workspace ~/.openclaw/workspace-xiaohongshu-rewrite;
openclaw agents add xiaohongshu-write            --workspace ~/.openclaw/workspace-xiaohongshu-write;
openclaw agents add xiaohongshu-publisher        --workspace ~/.openclaw/workspace-xiaohongshu-publisher;
openclaw agents add xiaohongshu-data-assistant    --workspace ~/.openclaw/workspace-xiaohongshu-data-assistant;
openclaw agents add xiaohongshu-comment-manager   --workspace ~/.openclaw/workspace-xiaohongshu-comment-manager;
```

### 3. 查看当前绑定

```bash
openclaw agents bindings
```

### 4. 按渠道绑定智能体（示例：企微 wecom，按执行链路顺序）

将渠道会话路由到对应 agent；其他渠道将 `wecom` 替换为 `feishu`、`telegram`、`webchat` 等即可。

```bash
openclaw agents bind --agent xiaohongshu-hot-monitor       --bind wecom:xiaohongshu-hot-monitor;
openclaw agents bind --agent xiaohongshu-viral-breakdown   --bind wecom:xiaohongshu-viral-breakdown;
openclaw agents bind --agent xiaohongshu-rewrite           --bind wecom:xiaohongshu-rewrite;
openclaw agents bind --agent xiaohongshu-write             --bind wecom:xiaohongshu-write;
openclaw agents bind --agent xiaohongshu-publisher         --bind wecom:xiaohongshu-publisher;
openclaw agents bind --agent xiaohongshu-data-assistant    --bind wecom:xiaohongshu-data-assistant;
openclaw agents bind --agent xiaohongshu-comment-manager   --bind wecom:xiaohongshu-comment-manager;
```

### 5. 删除小红书七件套（7 个，按执行链路顺序）

从 OpenClaw 中移除上述 7 个 agent（需先解除各 agent 的渠道绑定，若有）。

```bash
openclaw agents remove xiaohongshu-hot-monitor;
openclaw agents remove xiaohongshu-viral-breakdown;
openclaw agents remove xiaohongshu-rewrite;
openclaw agents remove xiaohongshu-write;
openclaw agents remove xiaohongshu-publisher;
openclaw agents remove xiaohongshu-data-assistant;
openclaw agents remove xiaohongshu-comment-manager;
```

## 文件结构（每智能体）

每智能体目录包含以下文件：

- **AGENTS.md** — 英文，角色定义、职责、边界、Session Startup、Memory、Red Lines、Tools、Heartbeats；供 OpenClaw 系统提示词注入
- **zh-CN/AGENTS.md** — 中文，与 AGENTS.md 内容等价，供团队阅读
- **SOUL.md** — 人格与风格、底线（建议在 zh-CN/ 下提供中文版）
- **IDENTITY.md** / **zh-CN/IDENTITY.md** — Who Am I?（英文）与「我是谁？」（中文），模板见 [docs/IDENTITY-template.md](../../docs/IDENTITY-template.md) 及 [docs/zh-CN/IDENTITY-template.md](../../docs/zh-CN/IDENTITY-template.md)
- **TOOLS.md** — 本地/环境备注；含「技能（ClawHub 优先，skills.sh 后补）」及安装命令
- **USER.md** — 所服务对象信息（随使用更新）
- **BOOTSTRAP.md** — 首次运行引导，完成后可删除
- **HEARTBEAT.md** / **zh-CN/HEARTBEAT.md** — 心跳任务说明，见 [docs/HEARTBEAT-template.md](../../docs/HEARTBEAT-template.md)

**中英文约定**：英文文件在智能体根目录，中文版集中在 `zh-CN/` 子目录，文件名与英文一致，便于将 `zh-CN/` 整目录拷贝到业务使用。

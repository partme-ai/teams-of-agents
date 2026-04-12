# 小红书七件套技能评估报告

> 本报告基于 ClawHub 与 skills.sh 小红书相关技能，结合七件套 7 个 Agent 实际需求做分组、同质对比与最终推荐。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。** ClawHub 技能按**评分优选**；Baoyu 系列补充通用抓取、配图、压缩与多语言等能力。评估结论与安装/卸载命令均在本报告内完整给出，不依赖外部文档。

---

## 一、ClawHub 技能优选（按评分，七件套优先）

同质能力只装一个时，优先选本表评分高者。下表为 ClawHub 小红书技能按评分排序的优选 10 项，含名称/功能摘要、七件套适用环节、作者与下载量。

| 序号 | Slug | 名称/功能摘要 | 七件套适用环节 | 评分 | 作者 | 下载 |
|------|------|----------------|----------------|------|------|------|
| 1 | xiaohongshu-mcp | 发布图文/视频、搜索笔记与趋势、分析帖子与评论、管理信息流 | 监控、拆解、发布、数据助手 | 3.633 | Borye | 15.5k |
| 2 | xiaohongshu-cn | 热门笔记发现、关键词监控、趋势分析 | 热门监控、数据助手、趋势分析 | 3.584 | guohongbin-git | 2.2k |
| 3 | xiaohongshu-deep-research | 话题研究、趋势分析、头部内容洞察与总结报告 | 爆款拆解、数据助手、深度调研 | 3.568 | PalmPalm7 | 1.7k |
| 4 | xiaohongshu-mcp-skill | 搜索、发布图文/视频、点赞/评论/收藏 | 发布、搜索、互动 | 3.527 | PalmPalm7 | 828 |
| 5 | xiaohongshu-mcp-skills | 登录、发布图文/视频、搜索、详情、点赞收藏评论、内容策划 | 发布、搜索、详情、评论 | 3.420 | xmznini | 775 |
| 6 | xiaohongshu-api | 帖子、评论、用户数据 API（TikHub） | 数据助手、帖子/评论/用户 | 3.412 | BOMBFUOCK | 389 |
| 7 | xiaohongshu-content | 爆款标题、内容模板、hashtag 策略、发布时间优化 | 二创、原创、爆款策略 | 3.349 | isaacloi1995-dot | 423 |
| 8 | xiaohongshu-founder-growth-writer | 草稿/创始人洞察/英文稿→平台化帖子 | 原创、草稿转帖子 | 3.338 | ATWatcher | 344 |
| 9 | xiaohongshu-assistant-operator | 指定创作者内容创作、发布、营销与互动自动化 | 发布、运营、互动 | 3.316 | a950701zz | 350 |
| 10 | xiaohongshu-search-summarizer | 关键词搜索→Top N 帖子→综合总结 | 爆款拆解、搜索与总结 | 3.275 | piekill | 116 |

**用途与使用场景简要说明：** xiaohongshu-mcp 覆盖监控每日拉取关键词笔记、爆款拆解抓单篇详情与评论、数据助手效果交叉分析及自动发布；xiaohongshu-cn 侧重品类热搜与趋势报告；xiaohongshu-deep-research 用于话题深度调研与头部账号洞察；xiaohongshu-search-summarizer 用于按关键词取一批笔记并生成总结。发布类 mcp、mcp-skill、mcp-skills、assistant-operator 为同质，只装一个时选评分最高的 xiaohongshu-mcp。

同质能力（如 MCP 发布、搜索总结）**只装一个高评分**即可。

---

## 二、七件套所需能力与技能映射

下表按 7 个智能体列出所需能力、推荐技能及来源（ClawHub 或 skills.sh）。Agent 编号：1=hot-monitor，2=viral-breakdown，3a=rewrite，3b=write，4=publisher，5=data-assistant，6=comment-manager。

| 序号 | Agent | 所需能力 | 推荐技能 | 来源 |
|------|-------|----------|----------|------|
| 1 | xiaohongshu-hot-monitor | 链接抓取、日报格式；趋势 | baoyu-url-to-markdown, baoyu-format-markdown；xiaohongshu-mcp, xiaohongshu-cn | skills.sh；ClawHub |
| 2 | xiaohongshu-viral-breakdown | 抓取/搜索、拆解格式 | baoyu-format-markdown；xiaohongshu-mcp, xiaohongshu-cn, xiaohongshu-deep-research, xiaohongshu-search-summarizer | skills.sh；ClawHub |
| 3a/3b | xiaohongshu-rewrite / xiaohongshu-write | 小红书配图与封面；内容策略 | baoyu-xhs-images, baoyu-cover-image, baoyu-article-illustrator；可选 xiaohongshu-content, xiaohongshu-founder-growth-writer | skills.sh；ClawHub |
| 4 | xiaohongshu-publisher | 发布前压缩；发布 | baoyu-compress-image；xiaohongshu-mcp（或 xiaohongshu-mcp-skill / xiaohongshu-mcp-skills / xiaohongshu-assistant-operator 选一） | skills.sh；ClawHub |
| 5 | xiaohongshu-data-assistant | 报告格式；数据分析 | baoyu-format-markdown；xiaohongshu-cn, xiaohongshu-mcp, xiaohongshu-deep-research, xiaohongshu-api, xiaohongshu-search-summarizer | skills.sh；ClawHub |
| 6 | xiaohongshu-comment-manager | 回复建议；评论采集 | xiaohongshu-mcp / xiaohongshu-mcp-skills；xiaohongshu-reply-assistant 按需 | ClawHub |

---

## 三、同质技能「谁更好」一览（结合评分）

同一能力若有多个技能，下表给出首选（按评分）与备选；备选与首选同质时只装一个。

| 序号 | 能力 | 首选（按评分） | 备选/不重复装 |
|------|------|----------------|----------------|
| 1 | 链接→Markdown/报告格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 小红书配图/封面 | baoyu-xhs-images, baoyu-cover-image, baoyu-article-illustrator | — |
| 3 | 发布到小红书 | xiaohongshu-mcp (3.633) | xiaohongshu-mcp-skill、xiaohongshu-mcp-skills、xiaohongshu-assistant-operator 选一 |
| 4 | 搜索/趋势/分析 | xiaohongshu-mcp, xiaohongshu-cn (3.584) | xiaohongshu-deep-research, xiaohongshu-search-summarizer 按环节选 |
| 5 | 深度调研/拆解 | xiaohongshu-deep-research (3.568), xiaohongshu-search-summarizer (3.275) | — |
| 6 | 内容/原创策略 | xiaohongshu-content (3.349), xiaohongshu-founder-growth-writer (3.338) | — |
| 7 | 数据 API | xiaohongshu-api (3.412) | — |
| 8 | 图片压缩 | baoyu-compress-image | — |
| 9 | 评论回复建议 | xiaohongshu-mcp-skills 或 xiaohongshu-reply-assistant | — |

---

## 四、最终推荐：按 Agent 的技能清单

下表为按步骤/Agent 的最终推荐技能清单，与第二节能力映射一致；同能力只选一个来源，ClawHub 按评分优选。

| 步骤 | Agent id | 推荐技能 | 来源 | 说明 |
|------|----------|----------|------|------|
| 1 | xiaohongshu-hot-monitor | baoyu-url-to-markdown, baoyu-format-markdown；xiaohongshu-mcp, xiaohongshu-cn | skills.sh；ClawHub | 抓取+日报；ClawHub 趋势（按评分优选） |
| 2 | xiaohongshu-viral-breakdown | baoyu-format-markdown；xiaohongshu-mcp, xiaohongshu-cn, xiaohongshu-deep-research, xiaohongshu-search-summarizer | skills.sh；ClawHub | 拆解格式+搜索/调研/总结（按评分优选） |
| 3a | xiaohongshu-rewrite | baoyu-xhs-images, baoyu-cover-image, baoyu-article-illustrator；可选 xiaohongshu-content | skills.sh；ClawHub | 配图为主；可选内容策略 |
| 3b | xiaohongshu-write | 同上；可选 xiaohongshu-founder-growth-writer | skills.sh；ClawHub | 同 rewrite；可选成长向原创 |
| 4 | xiaohongshu-publisher | baoyu-compress-image；xiaohongshu-mcp（或 mcp-skill/mcp-skills/assistant-operator 选一） | skills.sh；ClawHub | 压缩+发布（同质只装一个） |
| 5 | xiaohongshu-data-assistant | baoyu-format-markdown；xiaohongshu-cn, xiaohongshu-mcp, xiaohongshu-deep-research, xiaohongshu-api, xiaohongshu-search-summarizer | skills.sh；ClawHub | 报告格式+数据分析（按评分优选） |
| 6 | xiaohongshu-comment-manager | xiaohongshu-mcp 或 xiaohongshu-mcp-skills；xiaohongshu-reply-assistant 按需 | ClawHub | 评论/回复（同质选一） |

---

## 五、七件套全部可使用的技能：安装后目录名与命令来源

7 个智能体**全部可使用的技能**（全部不冲突）的安装与卸载命令在**本报告第七节 7.3** 中完整列出。config 中 `agents.list[].skills` 填写的即为「安装后目录名」：ClawHub 即 `<slug>`，skills.sh 即技能名（如 `baoyu-url-to-markdown`）。安装后目录位置：ClawHub 技能在 ClawHub 配置根下 `<slug>`，skills.sh 在 `~/.skills/<目录名>` 或 `./.skills/<目录名>`。全部不冲突规则：同质只取 1 个首选（如发布只列 xiaohongshu-mcp），可并存的全部列入；共约 45 个 ClawHub slug + 9 个 skills.sh 技能。

---

## 六、安装前置

**第一步：安装 SkillHub CLI**（仅首次需要）

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**全部技能安装/卸载**见本报告**第七节 7.3**。安装后目录名需与 config 中 `skills` 一致。勿在 TOOLS.md 存凭证。

---

## 七、完整技能栈（七件套 + 补充能力）

在满足七件套 6 个环节的基础上，增加**补充能力**，形成可覆盖「选题→筛选→拆解→创作→发布→数据→评论」全链路并具备标题筛选、爆款筛选、算法优化、审核复盘等扩展的完整技能栈。

### 7.1 补充能力与技能映射

下表列出**在七件套必备之外、可按需选装的扩展能力**：每种能力对应一种业务场景（用途说明）、推荐安装的技能、来源及使用备注。装齐七件套后，若需要标题预筛、算法优化、原创辅导、视频分析、审核复盘、多语言或信息图等，可从本表按序号选装。

| 序号 | 补充能力 | 用途说明 | 推荐技能 | 来源 | 备注 |
|------|----------|----------|----------|------|------|
| 1 | 标题筛选 / 标题质量 | 按标题范式筛选笔记、过滤低质标题；爆款拆解与热门监控的预筛 | xiaohongshu-content（爆款标题模板）、xiaohongshu-algorithm-optimizer（标题/首图优化） | ClawHub | 与拆解环节配合，先筛后拆 |
| 2 | 标题与首图优化 | 优化标题、内容、标签、首图文案，提高曝光与互动 | xiaohongshu-algorithm-optimizer、xhs-writing-coach（标题/正文/标签/封面文案） | ClawHub | 二创/原创产出前可调用 |
| 3 | 爆款 / 视频筛选 | 按细分领域筛选新鲜/爆款视频，带有效 xsec_token 的 URL | xhs-video-finder | ClawHub | 热门监控、爆款拆解补充 |
| 4 | 选题与热点筛选 | 话题研究、趋势、头部内容洞察，产出可执行选题列表 | xiaohongshu-deep-research、xiaohongshu-cn | ClawHub | 已在七件套中，完整栈保留 |
| 5 | 原创与互动辅导 | 笔记原创辅导、标题/正文/标签/评论引导/封面文案、互动提升 | xhs-writing-coach | ClawHub | 二创/原创、评论管理补充 |
| 6 | 多语言与翻译 | 多语言内容、翻译适配 | baoyu-translate | skills.sh | 按需 |
| 7 | 信息图 / 漫画风配图 | 信息图、漫画风帖子配图，丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh | 与 baoyu-xhs-images 等并存 |
| 8 | 审核与复盘流程 | Review-first：选题→草稿→飞书审核→发布→复盘 | openclaw-xiaohongshu-ops、clawnote | ClawHub | 发布前人工/流程审核 |
| 9 | 视频下载与分析 | 下载小红书视频、提取语音文字、整理总结，供拆解 | xhs-video-downloader、xhs-video-analyzer | ClawHub | 爆款拆解、数据助手补充 |
| 10 | 评论破冰与回复 | 基于内容找共同兴趣、生成破冰句；评论情感与回复建议 | xiaohongshu-first-line、xiaohongshu-reply-assistant | ClawHub | 评论管理补充 |

### 7.2 完整技能栈总表（按能力分类）

**七件套必备（与第四节一致）**

| 环节 | 必备技能 | 来源 |
|------|----------|------|
| 热门监控 | baoyu-url-to-markdown, baoyu-format-markdown；xiaohongshu-mcp, xiaohongshu-cn | skills.sh；ClawHub |
| 爆款拆解 | baoyu-format-markdown；xiaohongshu-mcp, xiaohongshu-cn, xiaohongshu-deep-research, xiaohongshu-search-summarizer | skills.sh；ClawHub |
| 二创/原创 | baoyu-xhs-images, baoyu-cover-image, baoyu-article-illustrator；xiaohongshu-content, xiaohongshu-founder-growth-writer | skills.sh；ClawHub |
| 自动发布 | baoyu-compress-image；xiaohongshu-mcp（或 mcp-skill/mcp-skills/assistant-operator 选一） | skills.sh；ClawHub |
| 数据助手 | baoyu-format-markdown；xiaohongshu-cn, xiaohongshu-mcp, xiaohongshu-deep-research, xiaohongshu-api, xiaohongshu-search-summarizer | skills.sh；ClawHub |
| 评论管理 | xiaohongshu-mcp 或 xiaohongshu-mcp-skills；xiaohongshu-reply-assistant 按需 | ClawHub |

**补充技能（按需选装）**

| 序号 | 补充能力 | 技能 | 来源 |
|------|----------|------|------|
| 1 | 标题筛选/优化、原创辅导 | xiaohongshu-content、xiaohongshu-algorithm-optimizer、xhs-writing-coach | ClawHub |
| 2 | 爆款/视频筛选 | xhs-video-finder | ClawHub |
| 3 | 审核与复盘 | openclaw-xiaohongshu-ops 或 clawnote | ClawHub |
| 4 | 视频下载与分析 | xhs-video-downloader、xhs-video-analyzer | ClawHub |
| 5 | 评论破冰 | xiaohongshu-first-line | ClawHub |
| 6 | 多语言 | baoyu-translate | skills.sh |
| 7 | 信息图/漫画风 | baoyu-infographic、baoyu-comic | skills.sh |

### 7.3 全部不冲突：全部安装命令与全部卸载命令

以下为全部不冲突技能（同质只取 1 个首选，可并存全部列入）的完整安装与卸载命令。复制执行即可。若某技能与当前环境冲突可单独注释该行。

**全部安装命令**

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

**全部卸载命令**

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

同质能力只装一个高评分技能；补充技能按需启用。安装后目录名需与 config 中 `skills` 一致。勿在 TOOLS.md 存凭证。

---

*本报告评估结论与命令以文档内表格与代码块为准；ClawHub、skills.sh 技能列表与下载量以各自官网当前数据为准。*

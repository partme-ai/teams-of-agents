# 公众号七件套技能评估报告

> 基于 [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md)（skills.sh）与 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)（ClawHub）两份技能清单，结合七件套 Agent 实际需求，做分组、同质对比与最终推荐。结论：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能，减少重复。**

## 一、七件套各 Agent 所需能力与技能映射

| 序号 | Agent | 职责摘要 | 所需能力 | 当前预设技能（README/TOOLS） |
|------|-------|----------|----------|------------------------------|
| 1 | 1-hot-monitor | 热点/爆款搜索 → 日报/摘要 | 链接抓取、报告格式 | baoyu-url-to-markdown, baoyu-format-markdown |
| 2 | 2-viral-breakdown | 爆款文章 → 拆解框架 | 文章搜索、正文提取、拆解输出格式 | wechat-article-extractor, baoyu-format-markdown |
| 3 | 3-rewrite | 拆解框架 → 二创草稿+配图 | 封面图、长文配图 | baoyu-cover-image, baoyu-article-illustrator |
| 4 | 4-write | 原创原创 → 草稿+配图 | 封面图、长文配图 | baoyu-cover-image, baoyu-article-illustrator |
| 5 | 5-publisher | 草稿 → 公众号发布+日志 | 发布、MD→HTML、图片压缩 | wechat-ai-publisher, baoyu-markdown-to-html, baoyu-compress-image, baoyu-post-to-wechat |
| 6 | 6-data-assistant | 数据解析 → 可执行反馈 | 报告格式 | baoyu-format-markdown |
| 7 | 7-comment-manager | 评论采集、回复草稿、情感 | 评论拉取、回复建议（按需） | 待选（ClawHub/skills.sh） |

---

## 二、按能力分组：同质技能对比

### 2.1 链接/网页抓取 → 转 Markdown（hot-monitor、viral-breakdown 用）

| 序号 | 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|------|-----------|----------|------------|
| 1 | **baoyu-url-to-markdown** | skills.sh · jimliu/baoyu-skills | 8.7K | URL 抓取转 Markdown，Chrome CDP | **推荐**：Baoyu 生态统一、安装量大、与 baoyu-format-markdown 同源 |
| 2 | baoyu-danger-x-to-markdown | skills.sh · baoyu | 8.9K | X 推文转 Markdown | 仅 X 场景，不替代 url-to-markdown |
| 3 | wechat-article-to-markdown | skills.sh · jackwener | 26 | 微信文章转 MD | 安装量小，能力与 baoyu-url-to-markdown 重叠，**不推荐重复安装** |
| 4 | wechat-article-fetcher | skills.sh · 多仓库 | 57–96 | 抓取公众号文章 | 多源、名不统一，维护分散；若已有 baoyu-url-to-markdown，**可不装** |
| 5 | **wechat-reader** | ClawHub | 258 | 阅读公众号文章、总结 | 纯阅读/总结，不做通用 URL→MD；可与 extractor 二选一按场景用 |
| 6 | **wxmp-reader** | ClawHub | 68 | 按 URL 阅读并总结公众号文章，绕反爬 | 与 wechat-reader 同质，**选一个即可**，推荐 wechat-reader（下载更高） |
| 7 | **scrapling-web-fetch** | ClawHub | 123 | 现代网页正文抓取，含公众号、尾部清洗 | 适合反爬/动态页；与 baoyu-url-to-markdown 互补，**viral-breakdown 可备选** |
| 8 | **clean-web-fetch** | ClawHub | 89 | 干净正文抓取，含公众号、噪音清洗 | 与 scrapling-web-fetch 同作者、能力接近，**二选一**，优先 scrapling |

**结论（抓取/转 MD）**  
- **hot-monitor / viral-breakdown**：主用 **baoyu-url-to-markdown**（skills.sh）。若遇反爬或需更强清洗，可加 **scrapling-web-fetch**（ClawHub）。  
- 不重复安装 wechat-article-to-markdown、多个 wechat-article-fetcher。

---

### 2.2 公众号文章搜索（hot-monitor、viral-breakdown、data-assistant 用）

| 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|-----------|----------|------------|
| **wechat-article-search** | ClawHub · wuchubuzai2018 | 3.8k · ★13 | 微信搜索获取文章列表，关键词/分类/时间 | **推荐**：合规两层检索、可配条数/日期，ClawHub 下载高 |
| wechat-article-search | skills.sh · 同作者 | 174 | 同上能力，不同分发源 | 与 ClawHub 同源，**只装一处**，优先 **ClawHub**（clawhub install） |

**结论（搜索）**  
- 统一用 **wechat-article-search**（ClawHub），不重复装 skills.sh 版。

---

### 2.3 公众号正文提取 → Markdown/结构化（viral-breakdown 用）

| 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|-----------|----------|------------|
| **wechat-article-extractor** | skills.sh · freestylefly | 492 | 公众号文章提取为 Markdown，支持镜像/反爬 | **推荐**：安装量大、专门针对公众号 |
| wechat-article-extractor | skills.sh · liaosvcaf/openclaw | 4 | 同能力，OpenClaw 生态 | 安装量小，**优先 freestylefly 版** |
| wechat-article-extractor | ClawHub / skills.volces | 3 / 多源 | 需在 ClawHub 查 slug | 若 ClawHub 有且维护好可切 ClawHub 统一安装 |
| **scrapling-web-fetch** | ClawHub | 123 | 网页正文+公众号+清洗 | 不专名「extractor」，但能做正文提取，**可作补充** |

**结论（正文提取）**  
- **viral-breakdown**：主用 **wechat-article-extractor**（skills.sh · freestylefly）。若 ClawHub 上有同名且文档清晰，可改为 `clawhub install wechat-article-extractor --workdir ~/.openclaw;` 统一来源。

---

### 2.4 报告/拆解/反馈格式（hot-monitor、viral-breakdown、data-assistant 用）

| 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|-----------|----------|------------|
| **baoyu-format-markdown** | skills.sh · jimliu/baoyu-skills | 7.3K | 规范 Markdown 报告格式 | **推荐**：三个 Agent 共用，安装量大、与 Baoyu 链一致 |

**结论（格式）**  
- 无同质竞品需取舍，**保留 baoyu-format-markdown** 即可。

---

### 2.5 封面图 / 长文配图（rewrite、write 用）

| 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|-----------|----------|------------|
| **baoyu-cover-image** | skills.sh · baoyu | 9.7K | 文章封面图生成 | **推荐**：类型/调色/风格维度全 |
| **baoyu-article-illustrator** | skills.sh · baoyu | 9.7K | 长文配图、按结构插图 | **推荐**：与封面同源，流程统一 |
| baoyu-image-gen | skills.sh · baoyu | 10.4K | 通用文生图 | 通用，非专为「封面/长文」，按需可选 |
| huashu-wechat-image | skills.sh | 17 | 微信配图 | 安装量小，**不替代** baoyu-cover/illustrator |
| wechat-article-formatter | skills.sh · 多源 | 19–66 | 排版/格式为主，非以图为核心 | 与「配图」不同能力，不冲突 |

**结论（配图）**  
- **rewrite / write**：只保留 **baoyu-cover-image** + **baoyu-article-illustrator**，不增加同质小量技能。

---

### 2.6 发布到公众号（publisher 用）

| 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|-----------|----------|------------|
| **baoyu-post-to-wechat** | skills.sh · jimliu/baoyu-skills | 10.3K / 10.4K | 文章+贴图发布，API/CDP 双通道 | **推荐**：安装量最大、文档全、支持 MD→微信 HTML |
| wechat-article-publisher | skills.sh · iamzifei | 596 | 发布到公众号 | 与 baoyu-post-to-wechat 同质，**选 Baoyu 即可** |
| wechat-article-publisher | ClawHub · zhenglong2015 | 68 | MD/链接提取后发布，standard/viral 样式 | 能力接近，下载量低于 Baoyu，**主用 Baoyu** |
| **wechat-ai-publisher** | skills.sh · bbwdadfg | 27 | 草稿/排版/封面/保存 | 安装量小，若 Baoyu 已覆盖发布流程可**不装** |
| wechat-ai-publisher | ClawHub | — | 需在 ClawHub 查 | 若有且需统一 ClawHub 可考虑 |
| wechat-draft-publisher | skills.sh · solar-luna | 45 | 草稿发布 | 与 Baoyu 重叠，**不重复** |
| wechat-html-publisher | ClawHub | 75 | HTML 直接进草稿箱 | 适合已有 HTML 的流水线，可与 Baoyu 互补 |
| wechat-public-cli | ClawHub | 468 | 本地 CLI 发布与下载公众号+百家号 | 偏运维/批量，与 Agent 发布流程可并存 |
| wechat-style-publisher | ClawHub | 0 | 多账号+主题/头尾模板 | 下载暂无，**观察后再说** |
| md2wechat / md-to-wechat / publish-md-to-wechat | skills.sh · 多源 | 3–106 | MD 转微信或发布 | 与 baoyu-post-to-wechat + baoyu-markdown-to-html 重叠，**不重复** |

**结论（发布）**  
- **publisher**：以 **baoyu-post-to-wechat** 为主（含发布+可选 MD→HTML）。  
- 保留 **baoyu-markdown-to-html**、**baoyu-compress-image**（排版+压缩）。  
- 不重复安装 wechat-article-publisher（多源）、wechat-ai-publisher、wechat-draft-publisher、md2wechat 等。  
- 若后续有「纯 HTML 进草稿」需求，再补 **wechat-html-publisher**（ClawHub）。

---

### 2.7 Markdown → 微信排版 HTML（publisher 用）

| 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|-----------|----------|------------|
| **baoyu-markdown-to-html** | skills.sh · baoyu | 7.4K | MD→微信友好 HTML，主题/代码/公式 | **推荐**：与 baoyu-post-to-wechat 配套 |

**结论**  
- 无替代需求，**保留 baoyu-markdown-to-html**。

---

### 2.8 图片压缩（publisher 用）

| 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|-----------|----------|------------|
| **baoyu-compress-image** | skills.sh · baoyu | 8.5K | WebP/PNG 压缩 | **推荐**：发布前压缩，与 Baoyu 链一致 |

**结论**  
- 无同质取舍，**保留 baoyu-compress-image**。

---

### 2.9 监控/阅读量/舆情（hot-monitor、data-assistant 用）

| 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|-----------|----------|------------|
| **wechat-mp-cn** | ClawHub | 2.9k · ★17 | 公众号监控、文章监控、阅读量、舆情 | **推荐**：ClawHub 下载高、星多，专做监控/数据 |
| wechat-daily-report | skills.sh · 多源 | 8–98 | 日报 | 偏「报告生成」，与 hot-monitor 产出重叠，可按需选 |

**结论**  
- **hot-monitor / data-assistant**：若需「阅读量/舆情」数据，补 **wechat-mp-cn**（ClawHub）。日报格式仍用 baoyu-format-markdown。

---

### 2.10 评论采集 / 回复建议（comment-manager 用）

| 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|-----------|----------|------------|
| **wechat-auto-reply** | ClawHub | 966 | 半自动回复（置信度>85% 自动发）、可主动发 | 个人/客服聊天，非公众号留言，**不直接对应** |
| **wechat-auto-reply-assistant** | ClawHub | 335 | 生成礼貌、贴合上下文的回复建议 | **推荐**：适合「回复草稿」+ 人工审批，与 comment-manager 需求一致 |
| wechat-mcp / dragon-wechat-mcp | ClawHub | 763 / 370 | Windows 微信消息监控与发送 | 个人微信 MCP，非公众号评论 |
| wechat-qq-sender | ClawHub | 212 | 微信/QQ 自动发消息、智能回复建议 | 个人端，非公众号评论 |

**结论（评论）**  
- **comment-manager**：优先考虑 **wechat-auto-reply-assistant**（ClawHub）做「回复建议」；评论采集若依赖平台 API/爬虫，需另配或自建，当前两清单中无专有「公众号留言拉取」技能，需按接口文档或 Playwright 等自研。

---

### 2.11 一站式工具包（可选替代多技能）

| 技能 | 来源 | 热度/下载 | 能力简述 | 水平与推荐 |
|------|------|-----------|----------|------------|
| **wechat-toolkit** | ClawHub | 1k · ★6 | 文章搜索+下载+AI 洗稿改写+发布 | 集成度高，若希望「少装多能」可部分替代「搜索+提取+发布」；与七件套「分 Agent 各司其职」的架构有重叠，**建议**：要么用 toolkit 做单 Agent 简化，要么维持七件套+上面分项推荐，二选一 |

**结论**  
- 不与其他分项推荐叠加使用，避免能力重复。

---

## 三、平台与来源对比（网上结论摘要）

- **ClawHub**：OpenClaw 社区技能市场（clawhub.ai），技能多、用 `clawhub install <slug> --workdir ~/.openclaw;` 管理，适合「发现+统一安装」。  
- **skills.sh**：Skills 官方展示与排名，安装量可见，安装方式为 `npx skills add <owner/repo> --skill <名>`，与 ClawHub 互补。  
- **关系**：两者互补；同一技能可能两边都有，只装一处即可，优先选**安装量/星标更高、文档更全**的一侧。  
- **Baoyu（jimliu/baoyu-skills）**：在 skills.sh 上安装量突出（7K–10K），覆盖发布、排版、配图、抓取、格式等，适合作为「发布+配图+格式」主链。

---

## 四、最终推荐：按 Agent 的技能清单（去重、取最优）

以下每个 Agent **只保留必要且不重复**的技能；同能力只选一个来源。

| 步骤 | Agent | 推荐技能 | 来源 | 说明 |
|------|-------|----------|------|------|
| 1 | 1-hot-monitor | baoyu-url-to-markdown, baoyu-format-markdown | skills.sh | 抓取链接、日报格式；若需阅读量/舆情再加 wechat-mp-cn（ClawHub） |
| 2 | 2-viral-breakdown | wechat-article-search, wechat-article-extractor, baoyu-format-markdown | ClawHub + skills.sh | 搜索用 ClawHub；提取用 skills.sh · freestylefly；格式用 Baoyu。遇反爬可加 scrapling-web-fetch |
| 3a | 3-rewrite | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面+长文配图，不增其他同质 |
| 3b | 4-write | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | 5-publisher | baoyu-post-to-wechat, baoyu-markdown-to-html, baoyu-compress-image | skills.sh | 发布+排版+压缩；wechat-ai-publisher 可不装 |
| 5 | 6-data-assistant | baoyu-format-markdown；可选 wechat-mp-cn | skills.sh；ClawHub | 报告格式必选；要数据再选 wechat-mp-cn |
| 6 | 7-comment-manager | wechat-auto-reply-assistant（回复建议）；评论采集按接口/自研 | ClawHub | 回复草稿用 ClawHub；采集需另配 |

---

## 五、同质技能「谁更好」一览

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown | baoyu-url-to-markdown | wechat-article-fetcher, wechat-article-to-markdown |
| 2 | 公众号搜索 | wechat-article-search（ClawHub） | wechat-article-search（skills.sh）同源只装一处 |
| 3 | 正文提取 | wechat-article-extractor（freestylefly） | scrapling-web-fetch 作补充 |
| 4 | 报告/拆解格式 | baoyu-format-markdown | — |
| 5 | 封面/长文配图 | baoyu-cover-image, baoyu-article-illustrator | huashu-wechat-image 等不替代 |
| 6 | 发布到公众号 | baoyu-post-to-wechat | wechat-article-publisher, wechat-ai-publisher, md2wechat 等不重复 |
| 7 | MD→微信 HTML | baoyu-markdown-to-html | — |
| 8 | 图片压缩 | baoyu-compress-image | — |
| 9 | 监控/阅读量/舆情 | wechat-mp-cn | — |
| 10 | 评论回复建议 | wechat-auto-reply-assistant | — |

---

## 六、七件套全部可使用的技能：安装后目录名与命令来源

7 个智能体**全部可使用的技能**（全部不冲突）的安装与卸载命令在**本报告第八节 8.3** 中完整列出。公众号管线 **能用上的全要** = ClawHub 公众号相关 slug 全列 + skills.sh Baoyu 及 wechat-article-extractor 全列。

---

## 七、安装前置

**第一步：安装 SkillHub CLI**（仅首次需要）

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**全部技能安装/卸载**见本报告**第八节 8.3**。安装后目录名需与 config 中 `skills` 一致。勿在 TOOLS.md 存凭证。发布智能体需配置公众号凭证（环境变量或 EXTEND.md）。

---

## 八、完整技能栈（七件套 + 补充能力）

在满足七件套 6 个环节的基础上，增加**补充能力**，形成可覆盖「监控→拆解→创作→发布→数据→评论」全链路并具备监控/舆情、评论回复、多语言、信息图等扩展的完整技能栈。

### 8.1 补充能力与技能映射

| 序号 | 补充能力 | 用途说明 | 推荐技能 | 来源 | 备注 |
|------|----------|----------|----------|------|------|
| 1 | 监控/阅读量/舆情 | 公众号文章监控、阅读量追踪、舆情分析 | wechat-mp-cn | ClawHub | hot-monitor、data-assistant 按需 |
| 2 | 评论回复建议 | 生成礼貌、贴合上下文的回复草稿 | wechat-auto-reply-assistant | ClawHub | comment-manager |
| 3 | 反爬/正文抓取补充 | 遇反爬或动态页时正文抓取 | scrapling-web-fetch | ClawHub | viral-breakdown 备选 |
| 4 | 多语言与翻译 | 多语言内容、翻译适配 | baoyu-translate | skills.sh | 按需 |
| 5 | 信息图/漫画风配图 | 丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh | 与封面/配图并存 |

### 8.2 完整技能栈总表（按能力分类）

**七件套必备（与第四节一致）**

| 环节 | 必备技能 | 来源 |
|------|----------|------|
| 热门监控 | baoyu-url-to-markdown, baoyu-format-markdown；可选 wechat-mp-cn | skills.sh；ClawHub |
| 爆款拆解 | wechat-article-search, wechat-article-extractor, baoyu-format-markdown；可选 scrapling-web-fetch | ClawHub + skills.sh |
| 二创/原创 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 自动发布 | baoyu-post-to-wechat, baoyu-markdown-to-html, baoyu-compress-image | skills.sh |
| 数据助手 | baoyu-format-markdown；可选 wechat-mp-cn | skills.sh；ClawHub |
| 评论管理 | wechat-auto-reply-assistant；评论采集按接口/自研 | ClawHub |

**补充技能（按需选装）**

| 序号 | 补充能力 | 技能 | 来源 |
|------|----------|------|------|
| 1 | 监控/舆情 | wechat-mp-cn | ClawHub |
| 2 | 反爬抓取 | scrapling-web-fetch | ClawHub |
| 3 | 多语言 | baoyu-translate | skills.sh |
| 4 | 信息图/漫画风 | baoyu-infographic、baoyu-comic | skills.sh |

### 8.3 全部不冲突：全部安装命令与全部卸载命令

以下为全部不冲突技能（同质只取 1 个首选，可并存全部列入）的完整安装与卸载命令。**能用上的全要**：ClawHub 公众号相关 + skills.sh Baoyu 及 wechat-article-extractor 全列。

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

同质能力只装一个；补充技能按需启用。安装后目录名需与 config 中 `skills` 一致。勿在 TOOLS.md 存凭证。

---

*文档基于 SKILLS-SH-SKILLS.md、CLAWHUB-SKILLS.md 及公开搜索整理，具体以 skills.sh、ClawHub 官网及各仓库为准。*

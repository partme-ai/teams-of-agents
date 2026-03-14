# 抖音七件套技能评估报告

> 基于 [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md)（skills.sh）与 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)（ClawHub），结合七件套 Agent 实际需求做分组、同质对比与最终推荐。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。**

## 一、七件套所需能力与技能映射

| 序号 | Agent | 所需能力 | 推荐技能 | 来源 |
|------|-------|----------|----------|------|
| 1 | douyin-hot-monitor | 热点/热榜、日报格式 | douyin-hot-trend；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub + skills.sh |
| 2 | douyin-viral-breakdown | 视频抓取/下载、拆解格式 | douyin-downloader 或 douyin-video-fetch；baoyu-format-markdown | ClawHub + skills.sh |
| 3 | douyin-rewrite / douyin-write | 封面与配图 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 4 | douyin-publisher | 发布、发布前压缩 | douyin-publish 或 douyin-video-publish；baoyu-compress-image | ClawHub + skills.sh |
| 5 | douyin-data-assistant | 报告格式 | baoyu-format-markdown | skills.sh |
| 6 | douyin-comment-manager | 回复建议；评论采集 | 按需 ClawHub/skills.sh | — |

## 二、同质技能「谁更好」一览

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown / 日报格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 抖音热榜/热搜 | douyin-hot-trend（ClawHub 2.9k） | — |
| 3 | 抖音视频下载 | douyin-downloader（1.9k）或 douyin-video-fetch（1.7k） | 同质只装一处 |
| 4 | 报告/拆解格式 | baoyu-format-markdown | — |
| 5 | 封面/配图 | baoyu-cover-image, baoyu-article-illustrator | — |
| 6 | 发布到抖音 | douyin-publish（2.3k）或 douyin-video-publish | 按需选一 |
| 7 | 图片压缩 | baoyu-compress-image | — |

## 三、最终推荐：按 Agent 的技能清单

| 步骤 | Agent id | 推荐技能 | 来源 | 说明 |
|------|----------|----------|------|------|
| 1 | douyin-hot-monitor | douyin-hot-trend, baoyu-url-to-markdown, baoyu-format-markdown | ClawHub + skills.sh | 热榜+抓取+日报格式 |
| 2 | douyin-viral-breakdown | douyin-downloader 或 douyin-video-fetch, baoyu-format-markdown | ClawHub + skills.sh | 视频下载+拆解格式 |
| 3a | douyin-rewrite | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面与配图 |
| 3b | douyin-write | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | douyin-publisher | douyin-publish, baoyu-compress-image | ClawHub + skills.sh | 发布+压缩；须遵守平台 ToS |
| 5 | douyin-data-assistant | baoyu-format-markdown | skills.sh | 报告格式 |
| 6 | douyin-comment-manager | （按需选评论采集与回复技能） | ClawHub/skills.sh | 评论拉取、回复草稿 |

## 四、七件套全部可使用的技能：命令来源

7 个智能体**全部可使用的技能**（全部不冲突）的安装与卸载命令在**本报告第六节 6.3** 中完整列出。抖音管线 ClawHub + skills.sh 能用上的全列。

## 五、安装前置

**第一步：安装 SkillHub CLI**（仅首次需要）

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**全部技能安装/卸载**见本报告**第六节 6.3**。安装后目录名需与 config 中 `skills` 一致。发布与抓取须遵守抖音开放平台与平台 ToS。勿在 TOOLS.md 存凭证。

## 六、完整技能栈（七件套 + 补充能力）

### 6.1 补充能力与技能映射

| 序号 | 补充能力 | 用途说明 | 推荐技能 | 来源 | 备注 |
|------|----------|----------|----------|------|------|
| 1 | 评论回复/采集 | 回复草稿、评论拉取 | 按需 ClawHub/skills.sh | — | comment-manager |
| 2 | 多语言与翻译 | 多语言内容、翻译适配 | baoyu-translate | skills.sh | 按需 |
| 3 | 信息图/漫画风配图 | 丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh | 与封面/配图并存 |

### 6.2 完整技能栈总表（按能力分类）

**七件套必备**

| 环节 | 必备技能 | 来源 |
|------|----------|------|
| 热门监控 | douyin-hot-trend, baoyu-url-to-markdown, baoyu-format-markdown | ClawHub + skills.sh |
| 爆款拆解 | douyin-downloader 或 douyin-video-fetch, baoyu-format-markdown | ClawHub + skills.sh |
| 二创/原创 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 自动发布 | douyin-publish, baoyu-compress-image | ClawHub + skills.sh |
| 数据助手 | baoyu-format-markdown | skills.sh |
| 评论管理 | 按需选评论采集与回复技能 | ClawHub/skills.sh |

**补充技能（按需选装）**

| 序号 | 补充能力 | 技能 | 来源 |
|------|----------|------|------|
| 1 | 多语言 | baoyu-translate | skills.sh |
| 2 | 信息图/漫画风 | baoyu-infographic、baoyu-comic | skills.sh |

### 6.3 全部不冲突：全部安装命令与全部卸载命令

**全部安装命令**

```bash
# ClawHub — 同质取一（下载选 douyin-downloader，发布选 douyin-publish）
clawhub install douyin-hot-trend --workdir ~/.openclaw;
clawhub install douyin-downloader --workdir ~/.openclaw;
clawhub install douyin-publish --workdir ~/.openclaw;

# skills.sh — 抓取、格式、配图、压缩、补充
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

---

*完整技能表见 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)、[SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md)。*

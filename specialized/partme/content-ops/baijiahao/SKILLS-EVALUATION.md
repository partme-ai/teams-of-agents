# 百家号七件套技能评估报告

> 基于 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 与 skills.sh Baoyu，结合七件套 Agent 实际需求做分组与最终推荐。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。** 百家号发布多依赖浏览器或开放平台 API；当前以 Baoyu 通用能力为主。

## 一、七件套所需能力与技能映射

| 序号 | Agent | 所需能力 | 推荐技能 | 来源 |
|------|-------|----------|----------|------|
| 1 | baijiahao-hot-monitor | 链接抓取、日报格式 | baoyu-url-to-markdown, baoyu-format-markdown | skills.sh |
| 2 | baijiahao-viral-breakdown | 抓取成文、拆解格式 | baoyu-url-to-markdown, baoyu-format-markdown | skills.sh |
| 3 | baijiahao-rewrite / baijiahao-write | 封面与配图 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 4 | baijiahao-publisher | 发布前压缩；发布 | baoyu-compress-image；浏览器/开放平台 | skills.sh |
| 5 | baijiahao-data-assistant | 报告格式 | baoyu-format-markdown | skills.sh |
| 6 | baijiahao-comment-manager | 回复建议；评论采集 | 按需 ClawHub/skills.sh | — |

## 二、同质技能「谁更好」一览

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown/报告格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 封面/长文配图 | baoyu-cover-image, baoyu-article-illustrator | — |
| 3 | 图片压缩 | baoyu-compress-image | — |

## 三、最终推荐：按 Agent 的技能清单

| 步骤 | Agent id | 推荐技能 | 来源 | 说明 |
|------|----------|----------|------|------|
| 1 | baijiahao-hot-monitor | baoyu-url-to-markdown, baoyu-format-markdown | skills.sh | 抓取+日报格式 |
| 2 | baijiahao-viral-breakdown | baoyu-url-to-markdown, baoyu-format-markdown | skills.sh | 抓取成文+拆解格式 |
| 3a | baijiahao-rewrite | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面与配图 |
| 3b | baijiahao-write | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | baijiahao-publisher | baoyu-compress-image | skills.sh | 压缩；发布需浏览器/开放平台 |
| 5 | baijiahao-data-assistant | baoyu-format-markdown | skills.sh | 报告格式 |
| 6 | baijiahao-comment-manager | （按需选评论采集与回复技能） | ClawHub/skills.sh | 评论拉取、回复草稿 |

## 四、七件套全部可使用的技能：命令来源

7 个智能体**全部可使用的技能**（全部不冲突）的安装与卸载命令在**本报告第六节 6.3** 中完整列出。百家号管线以 skills.sh Baoyu 为主；ClawHub 按需。

## 五、安装前置

**第一步：安装 SkillHub CLI**（仅首次需要）

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**全部技能安装/卸载**见本报告**第六节 6.3**。安装后目录名需与 config 中 `skills` 一致。勿在 TOOLS.md 存凭证。

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
| 热门监控 | baoyu-url-to-markdown, baoyu-format-markdown | skills.sh |
| 爆款拆解 | baoyu-url-to-markdown, baoyu-format-markdown | skills.sh |
| 二创/原创 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 自动发布 | baoyu-compress-image；发布需浏览器/开放平台 | skills.sh |
| 数据助手 | baoyu-format-markdown | skills.sh |
| 评论管理 | 按需选评论采集与回复技能 | ClawHub/skills.sh |

**补充技能（按需选装）**

| 序号 | 补充能力 | 技能 | 来源 |
|------|----------|------|------|
| 1 | 多语言 | baoyu-translate | skills.sh |
| 2 | 信息图/漫画风 | baoyu-infographic、baoyu-comic | skills.sh |

### 6.3 全部不冲突：全部安装命令与全部卸载命令

**能用上的全要**：以 skills.sh Baoyu 全列为主；ClawHub 若有 baijiahao 相关 slug 可追加。

**全部安装命令**

```bash
# ClawHub — clawhub search baijiahao 后按需 install

# skills.sh — 抓取、格式、配图、压缩、补充
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g
```

**全部卸载命令**

```bash
# ClawHub — 若有安装，按 slug 逐条 uninstall

# skills.sh
npx skills remove baoyu-url-to-markdown
npx skills remove baoyu-format-markdown
npx skills remove baoyu-cover-image
npx skills remove baoyu-article-illustrator
npx skills remove baoyu-compress-image
npx skills remove baoyu-translate
npx skills remove baoyu-infographic
npx skills remove baoyu-comic
```

---

*完整技能表见 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)、本目录 README 下方技能表。*

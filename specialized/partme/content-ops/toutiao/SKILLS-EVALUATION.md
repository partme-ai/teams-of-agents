# 头条号七件套技能评估报告

> 基于 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 与 skills.sh Baoyu，结合七件套 Agent 实际需求做分组与最终推荐。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。** 头条号 ClawHub 技能待补充，当前以 skills.sh Baoyu 为主；发布需头条开放平台或浏览器自动化。

## 一、七件套所需能力与技能映射

| 序号 | Agent | 所需能力 | 推荐技能 | 来源 |
|------|-------|----------|----------|------|
| 1 | toutiao-hot-monitor | 热点/趋势数据；链接抓取、日报格式 | **toutiao-news-trends**；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh |
| 2 | toutiao-viral-breakdown | 抓取成文、拆解格式 | baoyu-url-to-markdown, baoyu-format-markdown；可选 toutiao-news-trends | skills.sh；ClawHub/SkillHub |
| 3 | toutiao-rewrite / toutiao-write | 封面与配图 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 4 | toutiao-publisher | 发布前压缩；发布 | **toutiao-publisher**；baoyu-compress-image；头条开放平台/浏览器 | ClawHub/SkillHub；skills.sh |
| 5 | toutiao-data-assistant | 报告格式；热点数据 | baoyu-format-markdown；可选 toutiao-news-trends | skills.sh；ClawHub/SkillHub |
| 6 | toutiao-comment-manager | 回复建议；评论采集 | 按需 ClawHub/skills.sh | — |

## 二、同质技能「谁更好」一览

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown/报告格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 封面/长文配图 | baoyu-cover-image, baoyu-article-illustrator | — |
| 3 | 图片压缩 | baoyu-compress-image | — |

## 三、最终推荐：按 Agent 的技能清单

| 步骤 | Agent id | 推荐技能 | 来源 | 说明 |
|------|----------|----------|------|------|
| 1 | toutiao-hot-monitor | toutiao-news-trends；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh | 热点/趋势 + 抓取+日报格式 |
| 2 | toutiao-viral-breakdown | baoyu-url-to-markdown, baoyu-format-markdown；可选 toutiao-news-trends | skills.sh；ClawHub/SkillHub | 抓取成文+拆解格式 |
| 3a | toutiao-rewrite | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面与配图 |
| 3b | toutiao-write | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | toutiao-publisher | toutiao-publisher；baoyu-compress-image | ClawHub/SkillHub；skills.sh | 头条发布 + 压缩；发布需浏览器/开放平台 |
| 5 | toutiao-data-assistant | baoyu-format-markdown；可选 toutiao-news-trends | skills.sh；ClawHub/SkillHub | 报告格式 |
| 6 | toutiao-comment-manager | （按需选评论采集与回复技能） | ClawHub/skills.sh | 评论拉取、回复草稿 |

---

## 五、七件套全部可使用的技能：安装后目录名与命令来源

7 个智能体**全部可使用的技能**（全部不冲突）的安装与卸载命令在**本报告第七节 7.3** 中完整列出。头条号管线当前 ClawHub 技能待补充，**能用上的全要**以 skills.sh Baoyu 全系为主。

---

## 六、安装前置

**第一步：安装 SkillHub CLI**（仅首次需要）

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**全部技能安装/卸载**见本报告**第七节 7.3**。安装后目录名需与 config 中 `skills` 一致。勿在 TOOLS.md 存凭证。

---

## 七、完整技能栈（七件套 + 补充能力）

在满足七件套 6 个环节的基础上，增加**补充能力**，形成可覆盖「监控→拆解→创作→发布→数据→评论」全链路并具备多语言、信息图等扩展的完整技能栈。

### 7.1 补充能力与技能映射

| 序号 | 补充能力 | 用途说明 | 推荐技能 | 来源 | 备注 |
|------|----------|----------|----------|------|------|
| 1 | 多语言与翻译 | 多语言内容、翻译适配 | baoyu-translate | skills.sh | 按需 |
| 2 | 信息图/漫画风配图 | 信息图、漫画风配图，丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh | 与封面/配图并存 |

### 7.2 完整技能栈总表（按能力分类）

**七件套必备（与第四节一致）**

| 环节 | 必备技能 | 来源 |
|------|----------|------|
| 热门监控 | toutiao-news-trends；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh |
| 爆款拆解 | baoyu-url-to-markdown, baoyu-format-markdown；可选 toutiao-news-trends | skills.sh；ClawHub/SkillHub |
| 二创/原创 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 自动发布 | toutiao-publisher；baoyu-compress-image；发布需头条开放平台/浏览器 | ClawHub/SkillHub；skills.sh |
| 数据助手 | baoyu-format-markdown；可选 toutiao-news-trends | skills.sh；ClawHub/SkillHub |
| 评论管理 | 按需 ClawHub/skills.sh 评论采集与回复技能 | ClawHub/skills.sh |

**补充技能（按需选装）**

| 序号 | 补充能力 | 技能 | 来源 |
|------|----------|------|------|
| 1 | 多语言 | baoyu-translate | skills.sh |
| 2 | 信息图/漫画风 | baoyu-infographic、baoyu-comic | skills.sh |

### 7.3 全部不冲突：全部安装命令与全部卸载命令

以下为全部不冲突技能（同质只取 1 个首选，可并存全部列入）的完整安装与卸载命令。头条号管线含 ClawHub/SkillHub 头条技能（[CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)）与 skills.sh Baoyu。

**全部安装命令**

```bash
# 前置：SkillHub CLI（仅首次，国内推荐）
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

**全部卸载命令**

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

同质能力只装一个；补充技能按需启用。安装后目录名需与 config 中 `skills` 一致。勿在 TOOLS.md 存凭证。

---

*完整技能表见 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)、[SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md)。*

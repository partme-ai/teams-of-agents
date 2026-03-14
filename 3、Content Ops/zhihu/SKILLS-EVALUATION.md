# 知乎七件套技能评估报告

> 基于 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 与 skills.sh Baoyu，结合七件套 Agent 实际需求做分组与最终推荐。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。** 知乎 ClawHub 技能待补充，当前以 skills.sh Baoyu 为主；发布可选用 social-push 或浏览器自动化。

## 一、七件套所需能力与技能映射

| 序号 | Agent | 所需能力 | 推荐技能 | 来源 |
|------|-------|----------|----------|------|
| 1 | zhihu-hot-monitor | 热榜监控、趋势分析；热榜抓取+回答草稿；链接抓取、日报格式 | **zhihu-hot-cn**；**zhihu-assistant-skill**；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh |
| 2 | zhihu-viral-breakdown | 热榜/趋势；抓取成文、拆解格式 | zhihu-hot-cn；zhihu-assistant-skill；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh |
| 3 | zhihu-rewrite / zhihu-write | 封面与配图 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 4 | zhihu-publisher | 管理、发布、获取；发布前压缩；发布 | **zhihu**；baoyu-compress-image；social-push 或知乎发布类 | ClawHub/SkillHub；skills.sh |
| 5 | zhihu-data-assistant | 热榜趋势；报告格式 | zhihu-hot-cn；baoyu-format-markdown | ClawHub/SkillHub；skills.sh |
| 6 | zhihu-comment-manager | 回答草稿推飞书审核；管理；回复建议；评论采集 | **zhihu-assistant-skill**；**zhihu**；按需 ClawHub/skills.sh | ClawHub/SkillHub；— |

## 二、同质技能「谁更好」一览

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown/报告格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 封面/长文配图 | baoyu-cover-image, baoyu-article-illustrator | — |
| 3 | 发布到知乎 | social-push（多平台含知乎想法） | 按需选一 |
| 4 | 图片压缩 | baoyu-compress-image | — |

## 三、最终推荐：按 Agent 的技能清单

| 步骤 | Agent id | 推荐技能 | 来源 | 说明 |
|------|----------|----------|------|------|
| 1 | zhihu-hot-monitor | zhihu-hot-cn；zhihu-assistant-skill；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh | 热榜监控+热榜抓取/回答草稿 + 抓取+日报格式 |
| 2 | zhihu-viral-breakdown | zhihu-hot-cn；zhihu-assistant-skill；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh | 热榜/趋势 + 抓取成文+拆解格式 |
| 3a | zhihu-rewrite | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面与配图 |
| 3b | zhihu-write | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | zhihu-publisher | zhihu（管理/发布/获取）；baoyu-compress-image；可选 social-push | ClawHub/SkillHub；skills.sh | 知乎工具+压缩+发布 |
| 5 | zhihu-data-assistant | zhihu-hot-cn；baoyu-format-markdown | ClawHub/SkillHub；skills.sh | 热榜趋势+报告格式 |
| 6 | zhihu-comment-manager | zhihu-assistant-skill（回答草稿推飞书）；zhihu（管理）；按需评论采集与回复 | ClawHub/SkillHub；skills.sh | 回答草稿+飞书审核+评论拉取 |

## 四、七件套全部可使用的技能：命令来源

7 个智能体**全部可使用的技能**（全部不冲突）的安装与卸载命令在**本报告第六节 6.3** 中完整列出。知乎管线当前以 skills.sh Baoyu 为主；ClawHub 知乎技能待补充，能用上的以 6.3 为准。

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
| 1 | 发布到知乎 | 知乎想法/多平台发布 | social-push | skills.sh / ClawHub | publisher 按需 |
| 2 | 评论回复/采集 | 回复草稿、评论拉取 | 按需 ClawHub/skills.sh | — | comment-manager |
| 3 | 多语言与翻译 | 多语言内容、翻译适配 | baoyu-translate | skills.sh | 按需 |
| 4 | 信息图/漫画风配图 | 丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh | 与封面/配图并存 |

### 6.2 完整技能栈总表（按能力分类）

**七件套必备**

| 环节 | 必备技能 | 来源 |
|------|----------|------|
| 热门监控 | zhihu-hot-cn；zhihu-assistant-skill；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh |
| 爆款拆解 | zhihu-hot-cn；zhihu-assistant-skill；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh |
| 二创/原创 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 自动发布 | zhihu（管理/发布/获取）；baoyu-compress-image；可选 social-push | ClawHub/SkillHub；skills.sh |
| 数据助手 | zhihu-hot-cn；baoyu-format-markdown | ClawHub/SkillHub；skills.sh |
| 评论管理 | zhihu-assistant-skill（回答草稿推飞书）；zhihu（管理）；按需评论采集与回复 | ClawHub/SkillHub；skills.sh |

**补充技能（按需选装）**

| 序号 | 补充能力 | 技能 | 来源 |
|------|----------|------|------|
| 1 | 发布到知乎 | social-push | skills.sh / ClawHub |
| 2 | 多语言 | baoyu-translate | skills.sh |
| 3 | 信息图/漫画风 | baoyu-infographic、baoyu-comic | skills.sh |

### 6.3 全部不冲突：全部安装命令与全部卸载命令

以下为全部不冲突技能（同质只取 1 个首选，可并存全部列入）。知乎管线含 ClawHub/SkillHub 知乎技能（[CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)）与 skills.sh Baoyu。

**全部安装命令**

```bash
# 前置：SkillHub CLI（仅首次，国内推荐）
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash

# ClawHub/SkillHub — 知乎工具 + 热榜监控 + 热榜抓取与回答草稿助手
skillhub install zhihu
skillhub install zhihu-hot-cn
skillhub install zhihu-assistant-skill

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
# ClawHub/SkillHub 安装的知乎技能
clawhub uninstall zhihu;
clawhub uninstall zhihu-hot-cn;
clawhub uninstall zhihu-assistant-skill;

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

同质能力只装一个；补充技能按需启用。安装后目录名需与 config 中 `skills` 一致。

---

*完整技能表见 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)、本目录 README 下方技能表。*

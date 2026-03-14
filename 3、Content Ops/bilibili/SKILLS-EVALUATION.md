# B站七件套技能评估报告

> 基于 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 与 [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md)，结合 B 站七件套 Agent 实际需求做分组与最终推荐。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。** B 站链路为：热门监控 → 内容创作助手 → 视频发布 → 数据助手 → 爆款拆解 → 原创 → 评论管理。

## 一、七件套所需能力与技能映射

| 序号 | Agent | 所需能力 | 推荐技能 | 来源 |
|------|-------|----------|----------|------|
| 1 | bilibili-hot-monitor | 热门日报、UP 更新 | bilibili-hot-monitor, bilibili-update-viewer | ClawHub |
| 2 | bilibili-content-helper | 标题/标签/简介、字幕总结 | bilibili-helper, bilibili-subtitle-download-skill | ClawHub |
| 3 | bilibili-video-publisher | 创作者平台发布、投稿 | bilibili-video-publish, bilibili-upload | ClawHub |
| 4 | bilibili-data-assistant | 搜索与数据分析、统计报告 | bilibili-analytics | ClawHub |
| 5 | bilibili-viral-breakdown | 爆款视频拆解、框架输出 | baoyu-format-markdown；可选 bilibili 相关 | skills.sh + ClawHub |
| 6 | bilibili-write | 原创脚本与配图方向 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 7 | bilibili-comment-manager | 评论/弹幕拉取、回复草稿 | 按需 ClawHub/skills.sh | — |

## 二、同质技能「谁更好」一览

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | B站热门/日报 | bilibili-hot-monitor（ClawHub 4.4k） | — |
| 2 | UP 主更新检查 | bilibili-update-viewer（ClawHub） | — |
| 3 | 标题/标签/简介/字幕 | bilibili-helper, bilibili-subtitle-download-skill | — |
| 4 | 视频发布/投稿 | bilibili-video-publish, bilibili-upload | biliup-skills 等选一 |
| 5 | 数据分析/统计 | bilibili-analytics | — |
| 6 | 报告/拆解格式 | baoyu-format-markdown | — |
| 7 | 封面/配图 | baoyu-cover-image, baoyu-article-illustrator | — |

## 三、最终推荐：按 Agent 的技能清单（按执行链路顺序）

| 步骤 | Agent id | 推荐技能 | 来源 | 说明 |
|------|----------|----------|------|------|
| 1 | bilibili-hot-monitor | bilibili-hot-monitor, bilibili-update-viewer | ClawHub | 热门日报、UP 更新检查 |
| 2 | bilibili-content-helper | bilibili-helper, bilibili-subtitle-download-skill | ClawHub | 标题/标签/简介、字幕总结 |
| 3 | bilibili-video-publisher | bilibili-video-publish, bilibili-upload | ClawHub | 创作者平台发布、CLI 投稿 |
| 4 | bilibili-data-assistant | bilibili-analytics | ClawHub | 搜索与数据分析、统计报告 |
| 5 | bilibili-viral-breakdown | baoyu-format-markdown | skills.sh | 爆款拆解、框架输出 |
| 6 | bilibili-write | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 原创脚本与配图方向 |
| 7 | bilibili-comment-manager | （按需选评论/弹幕采集与回复技能） | ClawHub/skills.sh | 评论/弹幕拉取、回复草稿 |

## 四、七件套全部可使用的技能：命令来源

7 个智能体**全部可使用的技能**（全部不冲突）的安装与卸载命令在**本报告第六节 6.3** 中完整列出。B 站管线 ClawHub + skills.sh 能用上的全列。

## 五、安装前置

**第一步：安装 SkillHub CLI**（仅首次需要）

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**全部技能安装/卸载**见本报告**第六节 6.3**。安装后目录名需与 config 中 `skills` 一致。投稿/发布类技能通常需浏览器登录或 B 站凭证，勿在 TOOLS.md 存凭证。

## 六、完整技能栈（七件套 + 补充能力）

### 6.1 补充能力与技能映射

| 序号 | 补充能力 | 用途说明 | 推荐技能 | 来源 | 备注 |
|------|----------|----------|----------|------|------|
| 1 | 评论/弹幕采集与回复 | 评论拉取、回复草稿 | 按需 ClawHub/skills.sh | — | comment-manager |
| 2 | 多语言与翻译 | 多语言内容、翻译适配 | baoyu-translate | skills.sh | 按需 |
| 3 | 信息图/漫画风配图 | 丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh | 与封面/配图并存 |

### 6.2 完整技能栈总表（按能力分类）

**七件套必备**

| 环节 | 必备技能 | 来源 |
|------|----------|------|
| 热门监控 | bilibili-hot-monitor, bilibili-update-viewer | ClawHub |
| 内容助手 | bilibili-helper, bilibili-subtitle-download-skill | ClawHub |
| 视频发布 | bilibili-video-publish, bilibili-upload | ClawHub |
| 数据助手 | bilibili-analytics | ClawHub |
| 爆款拆解 | baoyu-format-markdown | skills.sh |
| 原创 | baoyu-cover-image, baoyu-article-illustrator | skills.sh |
| 评论管理 | 按需选评论/弹幕采集与回复技能 | ClawHub/skills.sh |

**补充技能（按需选装）**

| 序号 | 补充能力 | 技能 | 来源 |
|------|----------|------|------|
| 1 | 多语言 | baoyu-translate | skills.sh |
| 2 | 信息图/漫画风 | baoyu-infographic、baoyu-comic | skills.sh |

### 6.3 全部不冲突：全部安装命令与全部卸载命令

**全部安装命令**

```bash
# ClawHub
clawhub install bilibili-hot-monitor --workdir ~/.openclaw;
clawhub install bilibili-update-viewer --workdir ~/.openclaw;
clawhub install bilibili-helper --workdir ~/.openclaw;
clawhub install bilibili-subtitle-download-skill --workdir ~/.openclaw;
clawhub install bilibili-video-publish --workdir ~/.openclaw;
clawhub install bilibili-upload --workdir ~/.openclaw;
clawhub install bilibili-analytics --workdir ~/.openclaw;

# skills.sh — 爆款拆解、原创、补充
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g;
```

**全部卸载命令**

```bash
# ClawHub
clawhub uninstall bilibili-hot-monitor;
clawhub uninstall bilibili-update-viewer;
clawhub uninstall bilibili-helper;
clawhub uninstall bilibili-subtitle-download-skill;
clawhub uninstall bilibili-video-publish;
clawhub uninstall bilibili-upload;
clawhub uninstall bilibili-analytics;

# skills.sh
npx skills remove baoyu-format-markdown;
npx skills remove baoyu-cover-image;
npx skills remove baoyu-article-illustrator;
npx skills remove baoyu-translate;
npx skills remove baoyu-infographic;
npx skills remove baoyu-comic;
```

---

*完整技能表见 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md)、[SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md)。*

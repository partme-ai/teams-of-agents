# skills.sh 抖音相关技能一览

> 来源：[skills.sh/?q=douyin](https://skills.sh/?q=douyin)、[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)。安装方式：`npx skills add <owner/repo> --skill <技能名>`。与 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 并列。抖音为短视频平台，发布需开放平台 API 或浏览器，须遵守平台 ToS。

## Baoyu 系列（jimliu/baoyu-skills）本管线可用

| 技能名 | 本管线适用（agent / 用途） |
|--------|----------------------------|
| baoyu-url-to-markdown | hot-monitor、viral-breakdown：抓取链接成文 |
| baoyu-format-markdown | viral-breakdown、data-assistant：报告格式 |
| baoyu-cover-image | rewrite、write：封面 |
| baoyu-article-illustrator | rewrite、write：配图 |
| baoyu-compress-image | publisher：发布前压缩 |

## 安装方式（skills.sh）

```bash
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g;
```

安装后技能目录名需与 config 中 `skills` 一致。**勿在 TOOLS.md 存凭证。** 抓取与发布须遵守抖音开放平台与 ToS。

### 各技能安装与卸载命令示例

Baoyu 系列：**安装** `npx skills add jimliu/baoyu-skills --skill <技能名>`，**卸载** `npx skills remove <技能名>;`（技能名见上方 Baoyu 表）。

## 与七件套对应建议

| 序号 | 渠道 Agent | 可选的 skills.sh 技能（ClawHub 未覆盖时） |
|------|------------|------------------------------------------|
| 1 | douyin-hot-monitor | douyin-hot-trend（ClawHub）, baoyu-url-to-markdown, baoyu-format-markdown |
| 2 | douyin-viral-breakdown | douyin-downloader（ClawHub）, baoyu-format-markdown |
| 3 | douyin-rewrite / douyin-write | baoyu-cover-image, baoyu-article-illustrator；可选 baoyu-infographic, baoyu-comic |
| 4 | douyin-publisher | douyin-publish（ClawHub）, baoyu-compress-image |
| 5 | douyin-data-assistant | baoyu-format-markdown |
| 6 | douyin-comment-manager | 按需 ClawHub/skills.sh |

**全部安装/全部卸载**以 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 或 README「七件套全部可使用的技能」为准。

### 更新
- 重新执行 `npx skills add <owner/repo> --skill <技能名>` 覆盖安装即可；或以 skills.sh CLI 文档为准。

### 卸载
- **命令**：`npx skills remove <技能名>;`（技能名与安装后目录名一致）
- 或手动删除：项目安装为 `./.skills/<技能名>`，全局安装为 `~/.skills/<技能名>`。

# skills.sh 微博相关技能一览

> 来源：[skills.sh — 按 weibo 搜索](https://skills.sh/?q=weibo)、[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)。安装方式：`npx skills add <owner/repo> --skill <技能名>`。与 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 并列。

## 技能总表（序号）

| 序号 | 技能名 | 仓库/路径 | 备注 |
|------|--------|-----------|------|
| （待补充） | — | [skills.sh/?q=weibo](https://skills.sh/?q=weibo) | 微博管线以 Baoyu 为主；发布用 baoyu-post-to-weibo |

## Baoyu 与通用技能（本管线能用上的全列）

与 [SKILLS-EVALUATION.md §7.3](./SKILLS-EVALUATION.md) 一致；序号 | 技能名 | 本管线适用（agent/用途）。

| 序号 | 技能名 | 本管线适用（agent / 用途） |
|------|--------|----------------------------|
| 1 | baoyu-url-to-markdown | hot-monitor、viral-breakdown：抓取链接成文 |
| 2 | baoyu-format-markdown | viral-breakdown、data-assistant：报告格式 |
| 3 | baoyu-cover-image | rewrite、write：封面 |
| 4 | baoyu-article-illustrator | rewrite、write：配图 |
| 5 | baoyu-compress-image | publisher：发布前压缩 |
| 6 | baoyu-post-to-weibo | publisher：发布到微博 |
| 7 | baoyu-translate | 多语言（按需） |
| 8 | baoyu-infographic | rewrite/write：信息图（按需） |
| 9 | baoyu-comic | rewrite/write：漫画风（按需） |

## 各技能安装与卸载命令示例（序号）

| 序号 | 技能名 | 仓库 | 安装 | 卸载 |
|------|--------|------|------|------|
| 1 | baoyu-url-to-markdown | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;` | `npx skills remove baoyu-url-to-markdown;` |
| 2 | baoyu-format-markdown | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;` | `npx skills remove baoyu-format-markdown;` |
| 3 | baoyu-cover-image | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;` | `npx skills remove baoyu-cover-image;` |
| 4 | baoyu-article-illustrator | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;` | `npx skills remove baoyu-article-illustrator;` |
| 5 | baoyu-compress-image | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g;` | `npx skills remove baoyu-compress-image;` |
| 6 | baoyu-post-to-weibo | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill baoyu-post-to-weibo -y -g;` | `npx skills remove baoyu-post-to-weibo;` |
| 7 | baoyu-translate | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g;` | `npx skills remove baoyu-translate;` |
| 8 | baoyu-infographic | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g;` | `npx skills remove baoyu-infographic;` |
| 9 | baoyu-comic | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g;` | `npx skills remove baoyu-comic;` |

## 与七件套对应建议

| 序号 | 渠道 Agent | 可选的 skills.sh 技能（ClawHub 未覆盖时） |
|------|------------|------------------------------------------|
| 1 | weibo-hot-monitor | baoyu-url-to-markdown, baoyu-format-markdown |
| 2 | weibo-viral-breakdown | baoyu-url-to-markdown, baoyu-format-markdown |
| 3 | weibo-rewrite / weibo-write | baoyu-cover-image, baoyu-article-illustrator；可选 baoyu-infographic, baoyu-comic |
| 4 | weibo-publisher | baoyu-compress-image, baoyu-post-to-weibo |
| 5 | weibo-data-assistant | baoyu-format-markdown |
| 6 | weibo-comment-manager | 按需 ClawHub/skills.sh |

**全部安装/全部卸载**以 [SKILLS-EVALUATION.md §7.3](./SKILLS-EVALUATION.md) 或 README「七件套全部可使用的技能」为准。

## 安装方式（skills.sh）

```bash
# 见 README 或 SKILLS-EVALUATION §7.3 全部安装命令
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-post-to-weibo -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g;
```

安装后技能目录名需与 config 中 `skills` 一致。**勿在 TOOLS.md 存凭证。**

### 更新
- 重新执行 `npx skills add <owner/repo> --skill <技能名>` 覆盖安装即可；或以 skills.sh CLI 文档为准。

### 卸载
- **命令**：`npx skills remove <技能名>;`（技能名与安装后目录名一致）
- 或手动删除：项目安装为 `./.skills/<技能名>`，全局安装为 `~/.skills/<技能名>`。

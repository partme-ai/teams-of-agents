# skills.sh 头条号相关技能一览

> 来源：[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)。安装方式：`npx skills add <owner/repo> --skill <技能名>`。与 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 并列。头条号发布需开放平台或浏览器，当前以 baoyu 配图/抓取为主。

## 技能总表（序号）

头条号管线以 Baoyu 为主；技能列表见下方「Baoyu 与通用技能」及 [SKILLS-EVALUATION.md §7.3](./SKILLS-EVALUATION.md)。

## Baoyu 与通用技能（本管线能用上的全列）

| 序号 | 技能名 | 本管线适用（agent / 用途） |
|------|--------|----------------------------|
| 1 | baoyu-url-to-markdown | hot-monitor、viral-breakdown：抓取链接成文 |
| 2 | baoyu-format-markdown | viral-breakdown、data-assistant：报告格式 |
| 3 | baoyu-cover-image | rewrite、write：封面 |
| 4 | baoyu-article-illustrator | rewrite、write：配图 |
| 5 | baoyu-compress-image | publisher：发布前压缩 |
| 6 | baoyu-translate | 多语言（按需） |
| 7 | baoyu-infographic | rewrite/write：信息图（按需） |
| 8 | baoyu-comic | rewrite/write：漫画风（按需） |

## 各技能安装与卸载命令示例（序号）

| 序号 | 技能名 | 仓库 | 安装 | 卸载 |
|------|--------|------|------|------|
| 1～8 | （见上表） | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill <技能名> -y -g;` | `npx skills remove <技能名>;` |

**全部安装/全部卸载**以 [SKILLS-EVALUATION.md §7.3](./SKILLS-EVALUATION.md) 或 README「七件套全部可使用的技能」为准。

## 与七件套对应建议

| 序号 | 渠道 Agent | 可选的 skills.sh 技能（ClawHub 未覆盖时） |
|------|------------|------------------------------------------|
| 1 | toutiao-hot-monitor | baoyu-url-to-markdown, baoyu-format-markdown |
| 2 | toutiao-viral-breakdown | baoyu-url-to-markdown, baoyu-format-markdown |
| 3 | toutiao-rewrite / toutiao-write | baoyu-cover-image, baoyu-article-illustrator；可选 baoyu-infographic, baoyu-comic |
| 4 | toutiao-publisher | baoyu-compress-image（发布需开放平台/浏览器） |
| 5 | toutiao-data-assistant | baoyu-format-markdown |
| 6 | toutiao-comment-manager | 按需 ClawHub/skills.sh |

## 安装方式（skills.sh）

```bash
# 见 README 或 SKILLS-EVALUATION §7.3 全部安装命令
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g
```

安装后技能目录名需与 config 中 `skills` 一致。**勿在 TOOLS.md 存凭证。**

### 更新
- 重新执行 `npx skills add <owner/repo> --skill <技能名>` 覆盖安装即可；或以 skills.sh CLI 文档为准。

### 卸载
- **命令**：`npx skills remove <技能名>;`（技能名与安装后目录名一致）
- 或手动删除：项目安装为 `./.skills/<技能名>`，全局安装为 `~/.skills/<技能名>`。

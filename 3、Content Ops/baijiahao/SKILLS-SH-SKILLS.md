# skills.sh 百家号相关技能一览

> 百家号属百度系，skills.sh 暂无独立「百家号」技能；本管线以 **Baoyu 系列**（[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)）与通用抓取/发布能力为主。发布需浏览器或百家号开放平台。

## Baoyu 系列（jimliu/baoyu-skills）本管线可用

| # | 技能名 | 安装量 | 本管线适用（agent / 用途） |
|---|--------|--------|----------------------------|
| 1 | baoyu-url-to-markdown | 8.7K | viral-breakdown：抓取链接成文 |
| 2 | baoyu-format-markdown | 7.3K | viral-breakdown / data-assistant：报告格式 |
| 3 | baoyu-cover-image | 9.7K | rewrite：封面 |
| 4 | baoyu-article-illustrator | 9.7K | rewrite：长文配图 |
| 5 | baoyu-compress-image | 8.5K | publisher：发布前压缩 |

## 安装方式（skills.sh）

```bash
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image
```

百家号发布需浏览器自动化或开放平台 API，技能名需与 config 中 `skills` 一致。**勿在 TOOLS.md 存凭证。**

### 各技能安装与卸载命令示例

Baoyu 系列：**安装** `npx skills add jimliu/baoyu-skills --skill <技能名>`，**卸载** `npx skills remove <技能名>;`（技能名见上方 Baoyu 表）。

### 更新
- 重新执行 `npx skills add <owner/repo> --skill <技能名>` 覆盖安装即可；或以 skills.sh CLI 文档为准。

### 卸载
- **命令**：`npx skills remove <技能名>;`（技能名与安装后目录名一致）
- 或手动删除：项目安装为 `./.skills/<技能名>`，全局安装为 `~/.skills/<技能名>`。

## 与七件套对应建议

| 序号 | 渠道 Agent | 可选的 skills.sh 技能（ClawHub 未覆盖时） |
|------|------------|------------------------------------------|
| 1 | baijiahao-hot-monitor | baoyu-url-to-markdown, baoyu-format-markdown |
| 2 | baijiahao-viral-breakdown | baoyu-url-to-markdown, baoyu-format-markdown |
| 3 | baijiahao-rewrite / baijiahao-write | baoyu-cover-image, baoyu-article-illustrator；可选 baoyu-infographic, baoyu-comic |
| 4 | baijiahao-publisher | baoyu-compress-image（发布需浏览器/开放平台） |
| 5 | baijiahao-data-assistant | baoyu-format-markdown |
| 6 | baijiahao-comment-manager | 按需 ClawHub/skills.sh |

**全部安装/全部卸载**以 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 或 README「七件套全部可使用的技能」为准。

---

*Baoyu 完整列表见 [skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)。*

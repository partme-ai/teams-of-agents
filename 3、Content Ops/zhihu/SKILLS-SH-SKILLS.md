# skills.sh 知乎相关技能一览

> 来源：[skills.sh — 按 zhihu 搜索](https://skills.sh/?q=zhihu)、[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)。安装方式：`npx skills add <owner/repo> --skill <技能名>`。与 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 并列；知乎管线可优先用 skills.sh + 多平台发布（如 social-push）。

## 技能总表（按安装量排序）

| # | 技能名 | 仓库 / 路径 | 安装量 | 备注 |
|---|--------|-------------|--------|------|
| （待补充） | — | 请在 [skills.sh/?q=zhihu](https://skills.sh/?q=zhihu) 查看 | — | 知乎想法/回答发布见 [多平台内容发布能力调研](https://github.com/jihe520/social-push)（social-push 支持知乎） |

## Baoyu 系列（jimliu/baoyu-skills）本管线可用

> 来源：[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)，仓库 **jimliu/baoyu-skills**。与公众号/小红书管线类似，知乎四件套可选用以下技能。

| # | 技能名 | 安装量 | 本管线适用（agent / 用途） |
|---|--------|--------|----------------------------|
| 1 | baoyu-url-to-markdown | 8.7K | viral-breakdown：抓取知乎链接成文 |
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

多平台发布（含知乎想法）：可安装 [social-push](https://github.com/jihe520/social-push) 或同类 Skill。安装后技能目录名需与 config 中 `skills` 一致。

### 各技能安装与卸载命令示例

| 技能名 | 安装 | 卸载 |
|--------|------|------|
| baoyu-url-to-markdown | `npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;` | `npx skills remove baoyu-url-to-markdown;` |
| baoyu-format-markdown | `npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;` | `npx skills remove baoyu-format-markdown;` |
| baoyu-cover-image | `npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;` | `npx skills remove baoyu-cover-image;` |
| 其他 Baoyu | `npx skills add jimliu/baoyu-skills --skill <技能名> -y -g;` | `npx skills remove <技能名>;` |

## 与七件套对应建议

| 序号 | 渠道 Agent | 可选的 skills.sh 技能（ClawHub 未覆盖时） |
|------|------------|------------------------------------------|
| 1 | zhihu-hot-monitor | baoyu-url-to-markdown, baoyu-format-markdown |
| 2 | zhihu-viral-breakdown | baoyu-url-to-markdown, baoyu-format-markdown |
| 3 | zhihu-rewrite / zhihu-write | baoyu-cover-image, baoyu-article-illustrator；可选 baoyu-infographic, baoyu-comic |
| 4 | zhihu-publisher | baoyu-compress-image；可选 social-push |
| 5 | zhihu-data-assistant | baoyu-format-markdown |
| 6 | zhihu-comment-manager | 按需 ClawHub/skills.sh |

**全部安装/全部卸载**以 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 或 README「七件套全部可使用的技能」为准。

### 更新
- 重新执行 `npx skills add <owner/repo> --skill <技能名>` 覆盖安装即可；或以 skills.sh CLI 文档为准。

### 卸载
- **命令**：`npx skills remove <技能名>;`（技能名与安装后目录名一致）
- 或手动删除：项目安装为 `./.skills/<技能名>`，全局安装为 `~/.skills/<技能名>`。

## 与知乎四件套的对应建议（skills.sh）

| zhihu Agent | 可选的 skills.sh 技能 |
|-------------|------------------------|
| 1-zhihu-viral-breakdown | baoyu-url-to-markdown、baoyu-format-markdown |
| 2-zhihu-rewrite | baoyu-cover-image、baoyu-article-illustrator |
| 3-zhihu-publisher | social-push（或知乎发布类）、baoyu-compress-image |
| 4-zhihu-data-assistant | baoyu-format-markdown |

---

*文档根据 [skills.sh zhihu/baoyu 搜索](https://skills.sh/?q=zhihu) 公开信息整理。Baoyu 完整列表见 [skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)。*

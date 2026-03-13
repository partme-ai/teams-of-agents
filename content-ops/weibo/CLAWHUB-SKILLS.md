# ClawHub 微博相关技能一览

> 来源：[ClawHub — 按 weibo 搜索](https://clawhub.ai/skills?sort=downloads&q=weibo)。安装方式：`clawhub install <slug>`。若当前无或较少，以本目录 README 下方技能表与 baoyu-post-to-weibo、social-push 等多平台发布 Skill 为主；安装：`npx skills add <owner/repo> --skill <名>`。

## 技能总表（按下载量排序，待补充）

| 序号 | Slug | 名称/功能摘要 | 七件套适用环节 | 备注 |
|------|------|----------------|----------------|------|
| （待补充） | — | 请在 [ClawHub weibo](https://clawhub.ai/skills?sort=downloads&q=weibo) 查看最新 | — | 微博管线当前以 skills.sh + baoyu-post-to-weibo 为主 |

## 与七件套的对应建议

- **热门监控 / 爆款拆解 / 数据助手**：ClawHub 若有 weibo 搜索/抓取/数据分析类 slug 可选用；当前以 skills.sh（baoyu-url-to-markdown, baoyu-format-markdown）为主。
- **二创 / 写作**：以 skills.sh Baoyu 配图为主（baoyu-cover-image, baoyu-article-illustrator）。
- **发布**：以 **baoyu-post-to-weibo**（skills.sh）为主；ClawHub 若有 weibo 发布类 slug 可并存或二选一。
- **评论管理**：按需 ClawHub/skills.sh。

## 推荐安装清单

本渠道**能用上的全要**时，以 [SKILLS-EVALUATION.md §7.3](./SKILLS-EVALUATION.md) 及 [README 全部安装/全部卸载](./README.md) 为准；ClawHub 部分为已收录的少量技能（待补充），其余能力由 skills.sh（Baoyu 等）补充。

## 安装、更新与卸载

### 安装
- **搜索**：[ClawHub weibo](https://clawhub.ai/skills?sort=downloads&q=weibo) 查看最新技能与下载量。
- **命令**：`clawhub install <slug>`
- 安装后技能目录名需与 config 中 `agents.list[].skills` 一致。
- **skills.sh**：安装 `npx skills add <owner/repo> --skill <名>`；微博发布与抓取可参考本目录 README 及 baoyu-post-to-weibo。

### 更新
- 重新执行 `clawhub install <slug>` 覆盖安装即可；具体以 ClawHub CLI 文档为准。

### 卸载
- **命令**：`clawhub uninstall <slug>`
- 或手动删除 ClawHub 技能目录下对应技能文件夹（目录名一般为 slug）。

### 各技能安装与卸载命令

技能总表有具体 Slug 后，每个技能：**安装** `clawhub install <slug>`，**卸载** `clawhub uninstall <slug>`（将 `<slug>` 替换为表中 Slug）。示例：`clawhub install weibo-xxx` / `clawhub uninstall weibo-xxx`。

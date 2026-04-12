# ClawHub 快手相关技能一览

> 来源：[ClawHub — 按 kuaishou 搜索](https://clawhub.ai/skills?sort=downloads&q=kuaishou)。安装方式：`clawhub install <slug> --workdir ~/.openclaw;`。若当前无或较少，以本目录 README 下方技能表与 baoyu 系列为主；安装：`npx skills add <owner/repo> --skill <名>`。发布与抓取须遵守快手开放平台与平台 ToS。

## 技能总表（按下载量排序）

| # | Slug | 名称/功能摘要 | 备注 |
|---|------|----------------|------|
| （待补充） | — | 请在 [ClawHub kuaishou](https://clawhub.ai/skills?sort=downloads&q=kuaishou) 查看最新 | 快手管线可优先用 skills.sh + baoyu；发布需开放平台 API |

## 与七件套的对应建议

- **热门监控 / 爆款拆解 / 数据助手**：以 skills.sh（baoyu-url-to-markdown, baoyu-format-markdown）为主。
- **二创 / 原创**：以 skills.sh Baoyu 配图为主（baoyu-cover-image, baoyu-article-illustrator）。
- **发布**：快手需开放平台/浏览器；压缩用 baoyu-compress-image。
- **评论管理**：按需 ClawHub/skills.sh。

## 推荐安装清单

本渠道**能用上的全要**时，以 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 及 [README 全部安装/全部卸载](./README.md) 为准。

## 安装、更新与卸载

### 安装
- **搜索**：ClawHub 查看 kuaishou 最新技能。
- **命令**：`clawhub install <slug> --workdir ~/.openclaw;`
- 安装后技能目录名需与 config 中 `agents.list[].skills` 一致。
- **skills.sh**：安装：`npx skills add <owner/repo> --skill <名>`；技能列表见下方。**勿在 TOOLS.md 存凭证。** 合规与 ToS 见平台文档。

### 更新
- 重新执行 `clawhub install <slug> --workdir ~/.openclaw;` 覆盖安装即可；具体以 ClawHub CLI 文档为准。

### 卸载
- **命令**：`clawhub uninstall <slug>;`
- 或手动删除 ClawHub 技能目录下对应技能文件夹（目录名一般为 slug）。

### 各技能安装与卸载命令

技能总表有具体 Slug 后，每个技能：**安装** `clawhub install <slug> --workdir ~/.openclaw;`，**卸载** `clawhub uninstall <slug>;`。示例：`clawhub install kuaishou-xxx --workdir ~/.openclaw;` / `clawhub uninstall kuaishou-xxx;`。

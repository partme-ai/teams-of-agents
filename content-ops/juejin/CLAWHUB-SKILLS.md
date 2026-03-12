# ClawHub 掘金相关技能一览

> 来源：[ClawHub — 按 juejin 搜索](https://clawhub.ai/skills?sort=downloads&q=juejin)。安装方式：`clawhub install <slug>`。若当前无或较少，以本目录 README 下方技能表与 baoyu 系列、social-push 为主；安装：`npx skills add <owner/repo> --skill <名>`。

## 技能总表（按下载量排序）

| # | Slug | 名称/功能摘要 | 备注 |
|---|------|----------------|------|
| （待补充） | — | 请在 [ClawHub juejin](https://clawhub.ai/skills?sort=downloads&q=juejin) 查看最新 | 掘金管线可优先用 skills.sh + baoyu + social-push |

## 安装、更新与卸载

### 安装
- **搜索**：ClawHub 查看 juejin 最新技能。
- **命令**：`clawhub install <slug>`
- 安装后技能目录名需与 config 中 `agents.list[].skills` 一致。
- **skills.sh**：安装：`npx skills add <owner/repo> --skill <名>`；技能列表见下方。**勿在 TOOLS.md 存凭证。**

### 更新
- 重新执行 `clawhub install <slug>` 覆盖安装即可；具体以 ClawHub CLI 文档为准。

### 卸载
- **命令**：`clawhub uninstall <slug>`
- 或手动删除 ClawHub 技能目录下对应技能文件夹（目录名一般为 slug）。

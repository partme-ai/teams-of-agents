# ClawHub 微博相关技能一览

> 来源：[ClawHub — 按 weibo 搜索](https://clawhub.ai/skills?sort=downloads&q=weibo)。安装方式：`clawhub install <slug>`。若当前无或较少，以本目录 README 下方技能表与 baoyu-post-to-weibo、social-push 等多平台发布 Skill 为主；安装：`npx skills add <owner/repo> --skill <名>`。

## 技能总表（按下载量排序）

| # | Slug | 名称/功能摘要 | 备注 |
|---|------|----------------|------|
| （待补充） | — | 请在 [ClawHub weibo](https://clawhub.ai/skills?sort=downloads&q=weibo) 查看最新 | 微博管线可优先用 skills.sh + baoyu-post-to-weibo |

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

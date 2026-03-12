# ClawHub 知乎相关技能一览

> 来源：[ClawHub — 按 zhihu 搜索](https://clawhub.ai/skills?sort=downloads&q=zhihu)。安装方式：`clawhub install <slug>`（以 ClawHub 当前 CLI 为准）。若当前无或较少，以本目录 README 下方技能表与 social-push 等多平台发布 Skill 为主；安装：`npx skills add <owner/repo> --skill <名>`。

## 技能总表（按下载量排序）

| # | Slug | 名称/功能摘要 | 作者 | 下载 | 备注 |
|---|------|----------------|------|------|------|
| （待补充） | — | 请在 [ClawHub zhihu](https://clawhub.ai/skills?sort=downloads&q=zhihu) 查看最新 | — | — | 知乎管线可优先用 skills.sh + social-push |

## 安装、更新与卸载

### 安装
- **搜索**：[ClawHub zhihu](https://clawhub.ai/skills?sort=downloads&q=zhihu) 查看最新技能与下载量。
- **命令**：`clawhub install <slug>`
- 安装后技能目录名需与 openclaw 配置中 `agents.list[].skills` 一致。
- **skills.sh 与多平台发布**：安装 `npx skills add <owner/repo> --skill <名>`；知乎抓取与发布可参考本目录 README 及 [social-push](https://github.com/jihe520/social-push)（想法发布）。

### 更新
- 重新执行 `clawhub install <slug>` 覆盖安装即可；具体以 ClawHub CLI 文档为准。

### 卸载
- **命令**：`clawhub uninstall <slug>`
- 或手动删除 ClawHub 技能目录下对应技能文件夹（目录名一般为 slug）。

---

*文档根据 [ClawHub zhihu 搜索](https://clawhub.ai/skills?sort=downloads&q=zhihu) 公开信息整理，具体以官网为准。*

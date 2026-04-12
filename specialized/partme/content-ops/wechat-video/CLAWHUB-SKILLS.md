# ClawHub 视频号相关技能一览

> 来源：[ClawHub — 按 weixin / 视频号 搜索](https://clawhub.ai/skills?sort=downloads&q=weixin)。安装方式：`clawhub install <slug> --workdir ~/.openclaw;`。若当前无或较少，以本目录 README 下方技能表与 baoyu 系列为主；安装：`npx skills add <owner/repo> --skill <名>`。发布依赖视频号开放能力或浏览器自动化。

## 技能总表（按下载量排序，待补充）

| 序号 | Slug | 名称/功能摘要 | 七件套适用环节 | 备注 |
|------|------|----------------|----------------|------|
| （待补充） | — | 请在 ClawHub 查看 weixin / 视频号 相关技能 | — | 视频号管线当前以 skills.sh Baoyu 为主；可选 wechat-video-publish |

## 与七件套的对应建议

- **热门监控 / 爆款拆解 / 数据助手**：以 skills.sh（baoyu-url-to-markdown, baoyu-format-markdown）为主。
- **二创 / 原创**：以 skills.sh Baoyu 配图为主（baoyu-cover-image, baoyu-article-illustrator）。
- **发布**：可选 wechat-video-publish（ClawHub）；压缩用 baoyu-compress-image。
- **评论管理**：按需 ClawHub/skills.sh。

## 推荐安装清单

本渠道**能用上的全要**时，以 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 及 [README 全部安装/全部卸载](./README.md) 为准。

## 安装、更新与卸载

### 安装
- **搜索**：ClawHub 查看 weixin / 视频号 最新技能。
- **命令**：`clawhub install <slug> --workdir ~/.openclaw;`
- 安装后技能目录名需与 config 中 `agents.list[].skills` 一致。
- **skills.sh**：安装：`npx skills add <owner/repo> --skill <名>`；技能列表见下方。**勿在 TOOLS.md 存凭证。**

### 更新
- 重新执行 `clawhub install <slug> --workdir ~/.openclaw;` 覆盖安装即可；具体以 ClawHub CLI 文档为准。

### 卸载
- **命令**：`clawhub uninstall <slug>;`
- 或手动删除 ClawHub 技能目录下对应技能文件夹（目录名一般为 slug）。

### 各技能安装与卸载命令

技能总表有具体 Slug 后，每个技能：**安装** `clawhub install <slug> --workdir ~/.openclaw;`，**卸载** `clawhub uninstall <slug>;`。示例：`clawhub install wechat-video-xxx --workdir ~/.openclaw;` / `clawhub uninstall wechat-video-xxx;`。

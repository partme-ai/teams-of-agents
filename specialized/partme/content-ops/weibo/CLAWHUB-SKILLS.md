# ClawHub 微博相关技能一览

> 来源：[ClawHub — 按 weibo 搜索](https://clawhub.ai/skills?sort=downloads&q=weibo)。安装方式：**ClawHub** `clawhub install <slug> --workdir ~/.openclaw;`；**SkillHub**（腾讯国内镜像，推荐国内用户）`skillhub install <slug>`（需先安装 [SkillHub CLI](https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh)）。若当前无或较少，以本目录 README 下方技能表与 baoyu-post-to-weibo、social-push 等多平台发布 Skill 为主；安装：`npx skills add <owner/repo> --skill <名> -y -g;`。

## 技能总表（按下载量排序）

| 序号 | Slug | 名称/功能摘要 | 七件套适用环节 | 安装（ClawHub） | 安装（SkillHub） | 备注 |
|------|------|----------------|----------------|-----------------|------------------|------|
| 1 | weibo-fresh-posts | 监控微博关注流：先切换到最新微博时间线，再按发帖时间抓取并去重，写入每日 Markdown，减少关键微博漏看 | 热门监控、爆款拆解、数据助手 | `clawhub install weibo-fresh-posts --workdir ~/.openclaw;` | `skillhub install weibo-fresh-posts` | 国内推荐用 SkillHub 加速 |
| 2 | weibo-manager | Weibo Manager 图像与工作流工具：支持管理、执行、发布、审查 | 自动发布、评论管理、工作流 | `clawhub install weibo-manager --workdir ~/.openclaw;` | `skillhub install weibo-manager` | 与 baoyu-post-to-weibo 可并存或按需选一 |

更多技能请在 [ClawHub weibo](https://clawhub.ai/skills?sort=downloads&q=weibo) 与 SkillHub 搜索「微博」查看最新。微博管线其余能力以 skills.sh（Baoyu、baoyu-post-to-weibo）为主。

## 与七件套的对应建议

- **热门监控 / 爆款拆解 / 数据助手**：**weibo-fresh-posts**（关注流监控、按时间抓取去重、每日 Markdown）；并辅以 skills.sh（baoyu-url-to-markdown, baoyu-format-markdown）。
- **二创 / 原创**：以 skills.sh Baoyu 配图为主（baoyu-cover-image, baoyu-article-illustrator）。
- **发布**：**weibo-manager**（管理/执行/发布/审查）；或 baoyu-post-to-weibo、social-push；压缩用 baoyu-compress-image。
- **评论管理**：**weibo-manager**（审查等）；按需 ClawHub/skills.sh。

## 推荐安装清单

本渠道**能用上的全要**时，以 [SKILLS-EVALUATION.md §7.3](./SKILLS-EVALUATION.md) 及 [README 全部安装/全部卸载](./README.md) 为准。**ClawHub/SkillHub 微博技能**建议安装：

```bash
# 前置：安装 SkillHub CLI（仅首次，国内推荐）
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash

# 微博关注流监控 + 微博管理/发布/审查
skillhub install weibo-fresh-posts
skillhub install weibo-manager
```

或使用 ClawHub：`clawhub install weibo-fresh-posts --workdir ~/.openclaw;`、`clawhub install weibo-manager --workdir ~/.openclaw;`。

## 安装、更新与卸载

### 安装
- **搜索**：[ClawHub weibo](https://clawhub.ai/skills?sort=downloads&q=weibo) 查看最新技能与下载量；国内可用 SkillHub 搜索「微博」。
- **ClawHub 命令**：`clawhub install <slug> --workdir ~/.openclaw;`
- **SkillHub 命令**：先安装 [SkillHub CLI](https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh)，再执行 `skillhub install <slug>`
- 安装后技能目录名需与 config 中 `agents.list[].skills` 一致。
- **skills.sh**：安装 `npx skills add <owner/repo> --skill <名> -y -g;`；微博发布与抓取可参考本目录 README 及 baoyu-post-to-weibo。

### 更新
- 重新执行 `clawhub install <slug> --workdir ~/.openclaw;` 或 `skillhub install <slug>` 覆盖安装即可；具体以各 CLI 文档为准。

### 卸载
- **命令**：`clawhub uninstall <slug>;`（ClawHub 安装的）；SkillHub 安装的以 SkillHub 文档为准。
- 或手动删除技能目录下对应技能文件夹（目录名一般为 slug）。

### 各技能安装与卸载命令

| Slug | 安装（ClawHub） | 安装（SkillHub） | 卸载 |
|------|-----------------|------------------|------|
| weibo-fresh-posts | `clawhub install weibo-fresh-posts --workdir ~/.openclaw;` | `skillhub install weibo-fresh-posts` | `clawhub uninstall weibo-fresh-posts;` |
| weibo-manager | `clawhub install weibo-manager --workdir ~/.openclaw;` | `skillhub install weibo-manager` | `clawhub uninstall weibo-manager;` |

*文档根据 ClawHub / SkillHub 公开信息及用户说明整理，具体以官网为准。*

# ClawHub 知乎相关技能一览

> 来源：[ClawHub — 按 zhihu 搜索](https://clawhub.ai/skills?sort=downloads&q=zhihu)。安装方式：**ClawHub** `clawhub install <slug> --workdir ~/.openclaw;`；**SkillHub**（腾讯国内镜像，推荐国内用户）`skillhub install <slug>`（需先安装 [SkillHub CLI](https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh)）。若当前无或较少，以本目录 README 下方技能表与 social-push 等多平台发布 Skill 为主；安装：`npx skills add <owner/repo> --skill <名> -y -g;`。

## 技能总表（按下载量排序）

| 序号 | Slug | 名称/功能摘要 | 七件套适用环节 | 安装（ClawHub） | 安装（SkillHub） | 备注 |
|------|------|----------------|----------------|-----------------|------------------|------|
| 1 | zhihu | Zhihu 工具：支持管理、删除、发布、获取 | 自动发布、评论管理、数据助手 | `clawhub install zhihu --workdir ~/.openclaw;` | `skillhub install zhihu` | 国内推荐用 SkillHub 加速 |
| 2 | zhihu-hot-cn | 知乎热榜监控：获取知乎热门话题、问题和趋势分析（Quora 中国版） | 热门监控、爆款拆解、数据助手 | `clawhub install zhihu-hot-cn --workdir ~/.openclaw;` | `skillhub install zhihu-hot-cn` | 热榜数据入口 |
| 3 | zhihu-assistant-skill | 知乎热榜抓取与回答草稿生成助手：自动抓取知乎热榜，使用 AI 生成优质回答草稿，推送到飞书审核 | 热门监控、爆款拆解、评论管理（回答草稿+飞书审核） | `clawhub install zhihu-assistant-skill --workdir ~/.openclaw;` | `skillhub install zhihu-assistant-skill` | 热榜+回答草稿+飞书闭环 |

更多技能请在 [ClawHub zhihu](https://clawhub.ai/skills?sort=downloads&q=zhihu) 与 SkillHub 搜索「知乎」查看最新。知乎管线其余能力以 skills.sh（Baoyu、social-push）为主。

## 与七件套的对应建议

- **热门监控 / 爆款拆解 / 数据助手**：**zhihu-hot-cn**（热榜监控、趋势分析）；**zhihu-assistant-skill**（热榜抓取+回答草稿）；并辅以 skills.sh（baoyu-url-to-markdown, baoyu-format-markdown）。
- **二创 / 原创**：以 skills.sh Baoyu 配图为主（baoyu-cover-image, baoyu-article-illustrator）。
- **发布**：**zhihu**（管理、删除、发布、获取）；或 social-push；压缩用 baoyu-compress-image。
- **评论管理**：**zhihu-assistant-skill**（回答草稿推飞书审核）；**zhihu**（管理）；按需 ClawHub/skills.sh。

## 推荐安装清单

本渠道**能用上的全要**时，以 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 及 [README 全部安装/全部卸载](./README.md) 为准。**ClawHub/SkillHub 知乎技能**建议安装：

```bash
# 前置：安装 SkillHub CLI（仅首次，国内推荐）
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash

# 知乎通用工具 + 热榜监控 + 热榜抓取与回答草稿助手
skillhub install zhihu
skillhub install zhihu-hot-cn
skillhub install zhihu-assistant-skill
```

或使用 ClawHub：`clawhub install zhihu --workdir ~/.openclaw;`、`clawhub install zhihu-hot-cn --workdir ~/.openclaw;`、`clawhub install zhihu-assistant-skill --workdir ~/.openclaw;`。

## 安装、更新与卸载

### 安装
- **搜索**：[ClawHub zhihu](https://clawhub.ai/skills?sort=downloads&q=zhihu) 查看最新技能与下载量；国内可用 SkillHub 搜索「知乎」。
- **ClawHub 命令**：`clawhub install <slug> --workdir ~/.openclaw;`
- **SkillHub 命令**：先安装 [SkillHub CLI](https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh)，再执行 `skillhub install <slug>`
- 安装后技能目录名需与 config 中 `agents.list[].skills` 一致。
- **skills.sh**：安装 `npx skills add <owner/repo> --skill <名> -y -g;`；知乎抓取与发布可参考本目录 README 及 social-push。

### 更新
- 重新执行 `clawhub install <slug> --workdir ~/.openclaw;` 或 `skillhub install <slug>` 覆盖安装即可；具体以各 CLI 文档为准。

### 卸载
- **命令**：`clawhub uninstall <slug>;`（ClawHub 安装的）；SkillHub 安装的以 SkillHub 文档为准。
- 或手动删除技能目录下对应技能文件夹（目录名一般为 slug）。

### 各技能安装与卸载命令

| Slug | 安装（ClawHub） | 安装（SkillHub） | 卸载 |
|------|-----------------|------------------|------|
| zhihu | `clawhub install zhihu --workdir ~/.openclaw;` | `skillhub install zhihu` | `clawhub uninstall zhihu;` |
| zhihu-hot-cn | `clawhub install zhihu-hot-cn --workdir ~/.openclaw;` | `skillhub install zhihu-hot-cn` | `clawhub uninstall zhihu-hot-cn;` |
| zhihu-assistant-skill | `clawhub install zhihu-assistant-skill --workdir ~/.openclaw;` | `skillhub install zhihu-assistant-skill` | `clawhub uninstall zhihu-assistant-skill;` |

*文档根据 ClawHub / SkillHub 公开信息及用户说明整理，具体以官网为准。*

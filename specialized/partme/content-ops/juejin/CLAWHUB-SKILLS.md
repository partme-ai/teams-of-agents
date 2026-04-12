# ClawHub 掘金相关技能一览

> 来源：[ClawHub — 按 juejin 搜索](https://clawhub.ai/skills?sort=downloads&q=juejin)。安装方式：**ClawHub** `clawhub install <slug> --workdir ~/.openclaw;`；**SkillHub**（腾讯国内镜像，推荐国内用户）`skillhub install <slug>`（需先安装 [SkillHub CLI](https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh)）。若当前无或较少，以本目录 README 下方技能表与 baoyu 系列、social-push 为主；安装：`npx skills add <owner/repo> --skill <名> -y -g;`。

## 技能总表（按下载量排序）

| 序号 | Slug | 名称/功能摘要 | 七件套适用环节 | 安装（ClawHub） | 安装（SkillHub） | 备注 |
|------|------|----------------|----------------|-----------------|------------------|------|
| 1 | juejin-article-trends | 掘金热门文章排行榜：获取掘金网站热门文章排行，支持查询文章分类列表与各分类（前端/后端/AI 等）热门文章趋势 | 热门监控、爆款拆解、数据助手 | `clawhub install juejin-article-trends --workdir ~/.openclaw;` | `skillhub install juejin-article-trends` | 国内推荐用 SkillHub 加速 |
| 2 | pdf-to-structured | Pdf To Structured：文档、文字识别、PDF 工具，支持转换、提取、调度、扫描 | 抓取/文档处理、二创/原创 | `clawhub install pdf-to-structured --workdir ~/.openclaw;` | `skillhub install pdf-to-structured` | 通用 PDF 与结构化能力 |

更多技能请在 [ClawHub juejin](https://clawhub.ai/skills?sort=downloads&q=juejin) 与 SkillHub 搜索「掘金」查看最新。掘金管线其余能力以 skills.sh（Baoyu、social-push）为主。

## 与七件套的对应建议

- **热门监控 / 爆款拆解 / 数据助手**：**juejin-article-trends**（掘金热门文章与分类趋势）；并辅以 skills.sh（baoyu-url-to-markdown, baoyu-format-markdown）。
- **二创 / 原创**：**pdf-to-structured**（PDF 转换/提取）；以 skills.sh Baoyu 配图为主（baoyu-cover-image, baoyu-article-illustrator）。
- **发布**：可选 social-push；压缩用 baoyu-compress-image。
- **评论管理**：按需 ClawHub/skills.sh。

## 推荐安装清单

本渠道**能用上的全要**时，以 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 及 [README 全部安装/全部卸载](./README.md) 为准。**ClawHub/SkillHub 掘金技能**建议安装：

```bash
# 前置：安装 SkillHub CLI（仅首次，国内推荐）
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash

# 掘金热门文章趋势 + PDF 结构化
skillhub install juejin-article-trends
skillhub install pdf-to-structured
```

或使用 ClawHub：`clawhub install juejin-article-trends --workdir ~/.openclaw;`、`clawhub install pdf-to-structured --workdir ~/.openclaw;`。

## 安装、更新与卸载

### 安装
- **搜索**：[ClawHub juejin](https://clawhub.ai/skills?sort=downloads&q=juejin) 查看最新技能；国内可用 SkillHub 搜索「掘金」。
- **ClawHub 命令**：`clawhub install <slug> --workdir ~/.openclaw;`
- **SkillHub 命令**：先安装 [SkillHub CLI](https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh)，再执行 `skillhub install <slug>`
- 安装后技能目录名需与 config 中 `agents.list[].skills` 一致。
- **skills.sh**：安装：`npx skills add <owner/repo> --skill <名> -y -g;`；技能列表见下方。**勿在 TOOLS.md 存凭证。**

### 更新
- 重新执行 `clawhub install <slug> --workdir ~/.openclaw;` 或 `skillhub install <slug>` 覆盖安装即可；具体以各 CLI 文档为准。

### 卸载
- **命令**：`clawhub uninstall <slug>;`（ClawHub 安装的）；SkillHub 安装的以 SkillHub 文档为准。
- 或手动删除技能目录下对应技能文件夹（目录名一般为 slug）。

### 各技能安装与卸载命令

| Slug | 安装（ClawHub） | 安装（SkillHub） | 卸载 |
|------|-----------------|------------------|------|
| juejin-article-trends | `clawhub install juejin-article-trends --workdir ~/.openclaw;` | `skillhub install juejin-article-trends` | `clawhub uninstall juejin-article-trends;` |
| pdf-to-structured | `clawhub install pdf-to-structured --workdir ~/.openclaw;` | `skillhub install pdf-to-structured` | `clawhub uninstall pdf-to-structured;` |

*文档根据 ClawHub / SkillHub 公开信息及用户说明整理，具体以官网为准。*

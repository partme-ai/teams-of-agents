# ClawHub 头条号相关技能一览

> 来源：[ClawHub — 按 toutiao 搜索](https://clawhub.ai/skills?sort=downloads&q=toutiao)。安装方式：**ClawHub** `clawhub install <slug> --workdir ~/.openclaw;`；**SkillHub**（腾讯国内镜像，推荐国内用户）`skillhub install <slug>`（需先安装 [SkillHub CLI](https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh)）。若当前无或较少，以本目录 README 下方技能表与 baoyu 系列为主；安装：`npx skills add <owner/repo> --skill <名> -y -g;`。发布需头条开放平台或浏览器自动化。

## 技能总表（按下载量排序）

| 序号 | Slug | 名称/功能摘要 | 七件套适用环节 | 安装（ClawHub） | 安装（SkillHub） | 备注 |
|------|------|----------------|----------------|-----------------|------------------|------|
| 1 | toutiao-news-trends | 头条热点/趋势：抓取头条热榜数据，返回榜单标题、排名、热度、详情链接、封面与分类；支持按条数获取，适合日报与监控 | 热门监控、爆款拆解、数据助手 | `clawhub install toutiao-news-trends --workdir ~/.openclaw;` | `skillhub install toutiao-news-trends` | 国内推荐用 SkillHub 加速 |
| 2 | toutiao-publisher | 今日头条自动发布：微头条（100～2000 字）与长文（1000～5000 字），支持图文、话题、位置；浏览器自动化登录与发布流程 | 自动发布 | `clawhub install toutiao-publisher --workdir ~/.openclaw;` | `skillhub install toutiao-publisher` | 发布需浏览器/开放平台 |

更多技能请在 [ClawHub toutiao](https://clawhub.ai/skills?sort=downloads&q=toutiao) 与 SkillHub 搜索「头条」查看最新。头条号管线其余能力以 skills.sh Baoyu 为主。

## 与七件套的对应建议

- **热门监控 / 爆款拆解 / 数据助手**：**toutiao-news-trends**（热点/趋势数据）；并辅以 skills.sh（baoyu-url-to-markdown, baoyu-format-markdown）。
- **二创 / 原创**：以 skills.sh Baoyu 配图为主（baoyu-cover-image, baoyu-article-illustrator）。
- **发布**：**toutiao-publisher**（浏览器/开放平台）；压缩用 baoyu-compress-image。
- **评论管理**：按需 ClawHub/skills.sh。

## 推荐安装清单

本渠道**能用上的全要**时，以 [SKILLS-EVALUATION.md §7.3](./SKILLS-EVALUATION.md) 及 [README 全部安装/全部卸载](./README.md) 为准。**ClawHub/SkillHub 头条技能**建议安装：

```bash
# 前置：安装 SkillHub CLI（仅首次，国内推荐）
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash

# 头条热点/趋势 + 头条发布
skillhub install toutiao-news-trends
skillhub install toutiao-publisher
```

或使用 ClawHub：`clawhub install toutiao-news-trends --workdir ~/.openclaw;`、`clawhub install toutiao-publisher --workdir ~/.openclaw;`。

## 安装、更新与卸载

### 安装
- **搜索**：ClawHub 查看 [toutiao 最新技能](https://clawhub.ai/skills?sort=downloads&q=toutiao)；国内可用 SkillHub 搜索「头条」。
- **ClawHub 命令**：`clawhub install <slug> --workdir ~/.openclaw;`
- **SkillHub 命令**：先安装 [SkillHub CLI](https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh)，再执行 `skillhub install <slug>`
- 安装后技能目录名需与 config 中 `agents.list[].skills` 一致。
- **skills.sh**：安装：`npx skills add <owner/repo> --skill <名> -y -g;`；技能列表见 [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md)。**勿在 TOOLS.md 存凭证。**

### 更新
- 重新执行 `clawhub install <slug> --workdir ~/.openclaw;` 或 `skillhub install <slug>` 覆盖安装即可；具体以各 CLI 文档为准。

### 卸载
- **命令**：`clawhub uninstall <slug>;`（ClawHub 安装的）；SkillHub 安装的以 SkillHub 文档为准。
- 或手动删除技能目录下对应技能文件夹（目录名一般为 slug）。

### 各技能安装与卸载命令

| Slug | 安装（ClawHub） | 安装（SkillHub） | 卸载 |
|------|-----------------|------------------|------|
| toutiao-news-trends | `clawhub install toutiao-news-trends --workdir ~/.openclaw;` | `skillhub install toutiao-news-trends` | `clawhub uninstall toutiao-news-trends;` |
| toutiao-publisher | `clawhub install toutiao-publisher --workdir ~/.openclaw;` | `skillhub install toutiao-publisher` | `clawhub uninstall toutiao-publisher;` |

*文档根据 ClawHub / SkillHub 公开信息及网络检索整理，具体以官网为准。*

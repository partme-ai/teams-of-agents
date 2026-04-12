# skills.sh 小红书相关技能一览

> 来源：[skills.sh — 按 xiaohongshu 搜索](https://skills.sh/?q=xiaohongshu)。安装方式：`npx skills add <owner/repo> --skill <技能名>` 或 `npx skillsadd <owner/repo>/<技能路径>`（以 skills.sh 当前 CLI 为准）。与 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 并列，**ClawHub 优先、skills.sh 后补**。

## 技能总表（按安装量排序）

| 序号 | 技能名 | 仓库 / 路径 | 安装量 |
|------|--------|-------------|--------|
| 1 | xiaohongshu | zhjiang22/openclaw-xhs | 3.2K |
| 2 | xiaohongshu-note-analyzer | softbread/xiaohongshu-doctor | 1.0K |
| 3 | write-xiaohongshu | adjfks/corner-skills | 1.4K |
| 4 | xiaohongshu | autoclaw-cc/xiaohongshu-mcp-skills | 704 |
| 5 | xiaohongshu-images | iamzifei/xiaohongshu-images-skill | 685 |
| 6 | xiaohongshu-cover-generator | freestylefly/xiaohongshu-skills | 575 |
| 7 | xiaohongshu-converter | z0gsh1u/oh-my-writing-skill | 301 |
| 8 | xiaohongshu-ops | xiangyu-cas/xiaohongshu-ops-skill | 299 |
| 9 | xiaohongshu-skills | autoclaw-cc/xiaohongshu-skills | 128 |
| 10 | xiaohongshu-mcp | tclawde/xiaohongshu-mcp-skill | 101 |
| 11 | xiaohongshu-publisher | solar-luna/fully-automatic-article-generation-skill | 78 |
| 12 | xiaohongshu-search-summarizer | piekill/xiaohongshu-summarizer-skill | 75 |
| 13 | xiaohongshu-recruiter | iofficeai/aionui | 60 |
| 14 | xiaohongshu-publisher | iamzifei/red-publisher-skill | 52 |
| 15 | xiaohongshu | majiayu000/claude-arsenal | 37 |
| 16 | xiaohongshu-automation | wrt820232/xiaohongshu-automation | 32 |
| 17 | xiaohongshu-creation-workflow | cyhzzz/finance_aigc_skills | 19 |
| 18 | xiaohongshu-downloader | smile7up/xiaohongshu-downloader | 18 |
| 19 | xiaohongshu-posting | illuminated2020/deepagents-autoglm | 17 |
| 20 | xiaohongshu-skill | 1uokun/xiaohongshu-skill | 15 |
| 21 | xiaohongshu-workflow | aaaaqwq/claude-code-skills | 15 |
| 22 | xiaohongshu-dashboard | belljia95/xiaohongshu-dashboard-skill | 14 |
| 23 | xiaohongshu-skill | flyflypeng/xiaohongshu-skill | 11 |
| 24 | xiaohongshu-skill | deliciousbuding/xiaohongshu-skill | 7 |
| 25 | xiaohongshu | stvlynn/skills | 7 |
| 26 | xiaohongshu-publish | dingkwang/openclaw_superskill | 7 |
| 27 | xiaohongshu-data | kunhai-88/shopme-mcp | 4 |
| 28 | xiaohongshu-cli | jackwener/xiaohongshu-cli | 3 |
| 29 | xiaohongshu-creator | openakita/openakita | 4 |
| 30 | xiaohongshu-cn | skills.volces.com | 2 |

*同一技能名可能对应不同仓库（如 xiaohongshu、xiaohongshu-publisher、xiaohongshu-skill），安装时以所选仓库为准，安装后目录名需与 config 中 `skills` 一致。*

## Baoyu 系列（jimliu/baoyu-skills）

> 来源：[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)，仓库 **jimliu/baoyu-skills**。下表为 17 个技能及本管线（xiaohongshu 七件套）适用 agent 与用途。

| 序号 | 技能名 | 安装量 | 本管线适用（agent / 用途） |
|------|--------|--------|----------------------------|
| 1 | baoyu-image-gen | 10.4K | rewrite：配图 |
| 2 | baoyu-post-to-wechat | 10.4K | — |
| 3 | baoyu-cover-image | 9.7K | rewrite：封面 |
| 4 | baoyu-xhs-images | 9.7K | rewrite：帖图 |
| 5 | baoyu-article-illustrator | 9.7K | rewrite：长文配图 |
| 6 | baoyu-slide-deck | 9.4K | rewrite：素材 |
| 7 | baoyu-post-to-x | 9.2K | — |
| 8 | baoyu-infographic | 8.9K | rewrite：信息图 |
| 9 | baoyu-danger-x-to-markdown | 8.9K | — |
| 10 | baoyu-comic | 8.8K | rewrite：漫画风 |
| 11 | baoyu-url-to-markdown | 8.7K | viral-breakdown：拆解抓取 |
| 12 | baoyu-danger-gemini-web | 8.5K | — |
| 13 | baoyu-compress-image | 8.5K | publisher：发布前压缩 |
| 14 | baoyu-markdown-to-html | 7.4K | — |
| 15 | baoyu-format-markdown | 7.3K | viral-breakdown / data-assistant：报告格式 |
| 16 | baoyu-translate | 3.3K | rewrite / data-assistant：多语言（可选） |
| 17 | baoyu-post-to-weibo | 2.5K | — |

## 安装方式（skills.sh）

**单技能安装（推荐先查仓库内技能路径）：**

```bash
# 示例：从某仓库安装指定技能（技能名为仓库内目录名或 --skill 参数）
npx skills add zhjiang22/openclaw-xhs --skill xiaohongshu -y -g;
npx skills add softbread/xiaohongshu-doctor --skill xiaohongshu-note-analyzer -y -g;
npx skills add adjfks/corner-skills --skill write-xiaohongshu -y -g;
npx skills add autoclaw-cc/xiaohongshu-mcp-skills --skill xiaohongshu -y -g;
npx skills add iamzifei/xiaohongshu-images-skill --skill xiaohongshu-images -y -g;
npx skills add freestylefly/xiaohongshu-skills --skill xiaohongshu-cover-generator -y -g;
npx skills add xiangyu-cas/xiaohongshu-ops-skill --skill xiaohongshu-ops -y -g;
npx skills add piekill/xiaohongshu-summarizer-skill --skill xiaohongshu-search-summarizer -y -g;
```

**Baoyu 系列（与 xiaohongshu 预设技能表一致，后补方案）：**

```bash
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-xhs-images -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-image-gen -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-slide-deck -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g;
```

若 CLI 为 `npx skillsadd`（无空格），则：

```bash
npx skillsadd zhjiang22/openclaw-xhs
# 或指定子路径
npx skillsadd <owner/repo>/<skill-folder>
```

安装后技能目录名需与 openclaw 配置中 `agents.list[].skills` 一致。

### 各技能安装与卸载命令示例

| 序号 | 技能名 | 仓库 | 安装 | 卸载 |
|------|--------|------|------|------|
| 1 | xiaohongshu | zhjiang22/openclaw-xhs | `npx skills add zhjiang22/openclaw-xhs --skill xiaohongshu -y -g;` | `npx skills remove xiaohongshu;` |
| 2 | xiaohongshu-note-analyzer | softbread/xiaohongshu-doctor | `npx skills add softbread/xiaohongshu-doctor --skill xiaohongshu-note-analyzer -y -g;` | `npx skills remove xiaohongshu-note-analyzer;` |
| 3 | write-xiaohongshu | adjfks/corner-skills | `npx skills add adjfks/corner-skills --skill write-xiaohongshu -y -g;` | `npx skills remove write-xiaohongshu;` |
| 4 | xiaohongshu-ops | xiangyu-cas/xiaohongshu-ops-skill | `npx skills add xiangyu-cas/xiaohongshu-ops-skill --skill xiaohongshu-ops -y -g;` | `npx skills remove xiaohongshu-ops;` |
| 5 | xiaohongshu-search-summarizer | piekill/xiaohongshu-summarizer-skill | `npx skills add piekill/xiaohongshu-summarizer-skill --skill xiaohongshu-search-summarizer -y -g;` | `npx skills remove xiaohongshu-search-summarizer;` |
| 6 | baoyu-*（任选） | jimliu/baoyu-skills | `npx skills add jimliu/baoyu-skills --skill <技能名> -y -g;` | `npx skills remove <技能名>;` |

### 更新
- 重新执行 `npx skills add <owner/repo> --skill <技能名>` 覆盖安装即可；或以 skills.sh CLI 文档为准。

### 卸载
- **命令**：`npx skills remove <技能名>;`（技能名与安装后目录名一致）
- 或手动删除：项目安装为 `./.skills/<技能名>`，全局安装为 `~/.skills/<技能名>`。

## 与 xiaohongshu 七件套的对应建议（skills.sh 后补）

| 序号 | xiaohongshu Agent | 可选的 skills.sh 技能（ClawHub 未覆盖时） |
|------|---------------|--------------------------------------------|
| 1 | 8-xiaohongshu-viral-breakdown | xiaohongshu-note-analyzer、xiaohongshu-search-summarizer、xiaohongshu-ops、baoyu-url-to-markdown、baoyu-format-markdown |
| 2 | 9-xiaohongshu-rewrite | write-xiaohongshu、xiaohongshu-images、xiaohongshu-cover-generator、baoyu-xhs-images、baoyu-cover-image、baoyu-article-illustrator |
| 3 | 10-xiaohongshu-publisher | xiaohongshu-publisher（solar-luna 或 iamzifei）、xiaohongshu-publish、baoyu-compress-image |
| 4 | 11-xiaohongshu-data-assistant | xiaohongshu-note-analyzer、xiaohongshu-search-summarizer、xiaohongshu-data、baoyu-format-markdown |

**完整技能栈（七件套 + 补充）：** 含标题筛选、爆款筛选、多语言、信息图/漫画风等补充能力及完整安装命令见 [SKILLS-EVALUATION.md § 七、完整技能栈](./SKILLS-EVALUATION.md#七完整技能栈七件套--补充能力)。

---

*文档根据 [skills.sh xiaohongshu 搜索](https://skills.sh/?q=xiaohongshu) 公开信息整理，具体以 skills.sh 与各仓库为准。Baoyu 完整列表见 [skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)。*

# skills.sh B站 (bilibili) 相关技能一览

> 来源：[skills.sh — 按 bilibili 搜索](https://skills.sh/?q=bilibili)。安装方式：`npx skills add <owner/repo> --skill <技能名>` 或 `npx skillsadd <owner/repo>/<技能路径>`（以 skills.sh 当前 CLI 为准）。与 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 并列，**ClawHub 为主、skills.sh 取最优**。

## 技能总表（按安装量排序）

| # | 技能名 | 仓库 / 路径 | 安装量 |
|---|--------|-------------|--------|
| 1 | bilibili-subtitle | hamsterider-m/bilibili-subtitle | 356 |
| 2 | bilibili-analyzer | aidotnet/moyucode | 259 |
| 3 | bilibili-downloader | 958877748/skills | 137 |
| 4 | bilibili-chapter-generator | nanmicoder/claude-code-skills | 38 |
| 5 | bilibili-cli | jackwener/bilibili-cli | 29 |
| 6 | bilibili-toolkit | hwj123hwj/custom-skills | 23 |
| 7 | bilibili-downloader | atxinsky/skills | 8 |
| 8 | bilibili-subtitle-downloader | davincievans/bilibili-subtitle-download-skill | 7 |
| 9 | bilibili-downloader | smithery.ai | 3 |
| 10 | bilibili-watcher | openakita/openakita | — |

*同一技能名可能对应不同仓库（如 bilibili-downloader），安装时以所选仓库为准，安装后目录名需与 config 中 `skills` 一致。*

## Baoyu 系列（jimliu/baoyu-skills）本管线可用

> 来源：[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)，仓库 **jimliu/baoyu-skills**。下表为 17 个技能及本管线（B站四件套）适用 agent 与用途。

| # | 技能名 | 安装量 | 本管线适用（agent / 用途） |
|---|--------|--------|----------------------------|
| 1 | baoyu-image-gen | 10.4K | content-helper：内容配图 |
| 2 | baoyu-post-to-wechat | 10.4K | — |
| 3 | baoyu-cover-image | 9.7K | content-helper：内容封面 |
| 4 | baoyu-xhs-images | 9.7K | — |
| 5 | baoyu-article-illustrator | 9.7K | content-helper：脚本/简介配图 |
| 6 | baoyu-slide-deck | 9.4K | content-helper：视频/专栏素材 |
| 7 | baoyu-post-to-x | 9.2K | video-publisher：同步 X（可选） |
| 8 | baoyu-infographic | 8.9K | content-helper：信息图 |
| 9 | baoyu-danger-x-to-markdown | 8.9K | hot-monitor / content-helper：素材抓取 |
| 10 | baoyu-comic | 8.8K | content-helper：漫画风 |
| 11 | baoyu-url-to-markdown | 8.7K | hot-monitor：热点抓取 |
| 12 | baoyu-danger-gemini-web | 8.5K | content-helper：图/文生成（可选） |
| 13 | baoyu-compress-image | 8.5K | video-publisher：发布前压缩 |
| 14 | baoyu-markdown-to-html | 7.4K | content-helper：简介/专栏 |
| 15 | baoyu-format-markdown | 7.3K | hot-monitor / data-assistant：报告格式 |
| 16 | baoyu-translate | 3.3K | content-helper / data-assistant：多语言（可选） |
| 17 | baoyu-post-to-weibo | 2.5K | — |

## 安装方式（skills.sh）

**常用示例：**

```bash
npx skills add hamsterider-m/bilibili-subtitle --skill bilibili-subtitle
npx skills add aidotnet/moyucode --skill bilibili-analyzer
npx skills add 958877748/skills --skill bilibili-downloader
npx skills add nanmicoder/claude-code-skills --skill bilibili-chapter-generator
npx skills add jackwener/bilibili-cli --skill bilibili-cli
npx skills add davincievans/bilibili-subtitle-download-skill --skill bilibili-subtitle-downloader
```

**Baoyu 系列（jimliu/baoyu-skills）本管线可选：**

```bash
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image
npx skills add jimliu/baoyu-skills --skill baoyu-slide-deck
npx skills add jimliu/baoyu-skills --skill baoyu-infographic
npx skills add jimliu/baoyu-skills --skill baoyu-comic
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown
npx skills add jimliu/baoyu-skills --skill baoyu-image-gen
npx skills add jimliu/baoyu-skills --skill baoyu-markdown-to-html
npx skills add jimliu/baoyu-skills --skill baoyu-danger-x-to-markdown
npx skills add jimliu/baoyu-skills --skill baoyu-post-to-x
npx skills add jimliu/baoyu-skills --skill baoyu-translate
```

若 CLI 为 `npx skillsadd`（无空格），格式以 skills.sh 文档为准。安装后技能目录名需与 openclaw 配置中 `agents.list[].skills` 一致。

### 更新
- 重新执行 `npx skills add <owner/repo> --skill <技能名>` 覆盖安装即可；或以 skills.sh CLI 文档为准。

### 卸载
- **命令**：`npx skills remove <技能名>`（技能名与安装后目录名一致）
- 或手动删除：项目安装为 `./.skills/<技能名>`，全局安装为 `~/.skills/<技能名>`。

## 与 B站四件套的对应建议（skills.sh）

| bilibili Agent | 可选的 skills.sh 技能（ClawHub 未覆盖时） | Baoyu 可选 |
|----------------|--------------------------------------------|------------|
| 1-bilibili-hot-monitor | bilibili-analyzer、bilibili-watcher（openakita） | baoyu-url-to-markdown、baoyu-format-markdown、baoyu-danger-x-to-markdown |
| 2-bilibili-content-helper | bilibili-subtitle、bilibili-subtitle-downloader、bilibili-chapter-generator | baoyu-cover-image、baoyu-article-illustrator、baoyu-slide-deck、baoyu-infographic、baoyu-comic、baoyu-image-gen、baoyu-markdown-to-html、baoyu-translate |
| 3-bilibili-video-publisher | bilibili-downloader（下载后本地处理）、bilibili-toolkit（若含投稿） | baoyu-compress-image、baoyu-post-to-x |
| 4-bilibili-data-assistant | bilibili-analyzer | baoyu-format-markdown、baoyu-translate |

---

*文档根据 [skills.sh bilibili 搜索](https://skills.sh/?q=bilibili) 公开信息整理，具体以 skills.sh 与各仓库为准。Baoyu 完整列表见 [skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)。*

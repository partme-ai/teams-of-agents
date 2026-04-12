# TOOLS.md - 本地备注

技能定义工具**怎么用**。本文件写**你这边**的配置与备注。

## 可写内容

- 爆款拆解报告路径
- 草稿输出路径（如 `drafts/`）
- 品牌/格式规则与调性
- 配图需求模板或风格说明
- 与发布、数据助手的交接约定

## 技能（ClawHub 优先，skills.sh 后补）

- **ClawHub（优先）**：在 [clawhub.ai/skills?q=xiaohongshu](https://clawhub.ai/skills?sort=downloads&q=xiaohongshu) 搜索小红书相关技能，若有则 `clawhub install <技能名>`，并加入本 agent 的 `skills` 配置。
- **skills.sh（后补）**：
  - **baoyu-xhs-images**：小红书信息图系列（风格与版式见技能说明），用于帖图。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-xhs-images`。
  - **baoyu-cover-image**：文章/帖子封面图。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-cover-image`。
  - **baoyu-article-illustrator**：长文配图（类型×风格）。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator`。配图风格、输出路径等可在本文件或 USER 中约定。

---

按需补充。本文件不存凭证。

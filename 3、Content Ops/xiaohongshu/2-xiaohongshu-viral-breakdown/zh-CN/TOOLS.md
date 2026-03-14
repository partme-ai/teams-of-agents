# TOOLS.md - 本地备注

技能定义工具**怎么用**。本文件写**你这边**的配置与备注。

## 可写内容

- 搜索接口或平台访问方式（小红书/爬虫/官方 API 等）
- 拆解报告输出路径（如 `breakdowns/`）
- 行业关键词与主题列表
- 与二创、数据助手的交接路径或约定
- 与爆款拆解相关的环境配置

## 技能（ClawHub 优先，skills.sh 后补）

- **ClawHub（优先）**：在 [clawhub.ai/skills?q=xiaohongshu](https://clawhub.ai/skills?sort=downloads&q=xiaohongshu) 搜索小红书相关技能，若有则 `clawhub install <技能名>`，并加入本 agent 的 `skills` 配置。
- **skills.sh（后补）**：
  - **baoyu-url-to-markdown**：将热点/竞品 URL 抓取为 Markdown，供拆解。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown`。
  - **baoyu-format-markdown**：规范拆解报告格式，供二创与数据助手消费。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown`。

---

按需补充。本文件不存凭证。

# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## What Goes Here

- Search API or platform access (Xiaohongshu / crawler / official API if any)
- Output path for breakdowns (e.g. `breakdowns/`)
- Industry keywords and topic lists
- Handoff paths or conventions for 二创 and data assistant
- Anything environment-specific for viral breakdown

## Skills (ClawHub 优先，skills.sh 后补)

- **ClawHub（优先）**：在 [clawhub.ai/skills?q=xiaohongshu](https://clawhub.ai/skills?sort=downloads&q=xiaohongshu) 搜索小红书相关技能，若有则 `clawhub install <技能名>`，并加入本 agent 的 `skills` 配置。
- **skills.sh（后补）**：
  - **baoyu-url-to-markdown**：抓取热点/竞品 URL 为 Markdown，供拆解。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown`。
  - **baoyu-format-markdown**：规范拆解报告格式，供二创与数据助手消费。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown`。

---

Add whatever helps you do your job. Never store credentials here.

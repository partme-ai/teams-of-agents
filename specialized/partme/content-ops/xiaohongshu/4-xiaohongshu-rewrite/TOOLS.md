# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## What Goes Here

- Path to breakdown reports (from viral-breakdown agent)
- Draft output path (e.g. `drafts/`)
- Brand/format rules and tone
- Image brief template or style guide
- Handoff to publisher and data assistant

## Skills (ClawHub 优先，skills.sh 后补)

- **ClawHub（优先）**：在 [clawhub.ai/skills?q=xiaohongshu](https://clawhub.ai/skills?sort=downloads&q=xiaohongshu) 搜索小红书相关技能，若有则 `clawhub install <技能名>`，并加入本 agent 的 `skills` 配置。
- **skills.sh（后补）**：
  - **baoyu-xhs-images**：小红书信息图系列（风格与版式见技能说明）。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-xhs-images`。
  - **baoyu-cover-image**：帖子/文章封面图。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-cover-image`。
  - **baoyu-article-illustrator**：长文配图（类型×风格）。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator`。风格与输出路径在本文或 USER 中约定。

---

Add whatever helps you do your job. Never store credentials here.

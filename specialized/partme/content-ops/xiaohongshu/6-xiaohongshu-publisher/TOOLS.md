# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## What Goes Here

- Draft source path (from 二创)
- Publish API or tool reference (no raw secrets; use env)
- Publish log path for data assistant (e.g. `publish-logs/`)
- Rate limits and schedule rules
- Data-assistant handoff format

## Skills (ClawHub 优先，skills.sh 后补)

- **ClawHub（优先）**：在 [clawhub.ai/skills?q=xiaohongshu](https://clawhub.ai/skills?sort=downloads&q=xiaohongshu) 搜索小红书发布相关技能，若有则 `clawhub install <技能名>`，并加入本 agent 的 `skills` 配置。
- **skills.sh（后补）**：
  - **baoyu-compress-image**：发布前压缩图片（WebP/PNG）。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-compress-image`。实际发布动作（小红书/脚本/第三方工具）以本文件配置为准。

---

Add whatever helps you do your job. Never store credentials in this file.

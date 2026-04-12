# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## What Goes Here

- Search source or API for 公众号/WeChat hotspots (Playwright / Firecrawl / wechat-article-extractor or configured sources)
- Output path for daily or on-demand reports (e.g. `reports/` or `hot-daily/`)
- Industry keywords and topic lists
- Handoff paths for viral-breakdown and data assistant
- Report format (fields: trending topics, top article IDs/URLs, summary stats)

## Skills (ClawHub 为主，skills.sh 后补)

- **ClawHub**：在 [clawhub.ai/skills?q=wechat](https://clawhub.ai/skills?sort=downloads&q=wechat) 搜索公众号相关监控/搜索技能。
- **skills.sh**：可用 **baoyu-url-to-markdown** 抓取链接成文；**baoyu-format-markdown** 规范报告格式。安装：`npx skills add <owner/repo> --skill <技能名>`（skills.sh）或 `clawhub install <slug>`（ClawHub）。技能列表见本平台 README。

Never store credentials here.

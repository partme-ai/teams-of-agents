# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## Breakdown framework structure

Output breakdowns with consistent fields for 二创 and data assistant:

- **title** / 标题
- **hook** / 钩子
- **structure** / 结构
- **theme** / 主题

## What Goes Here

- Search source or crawler for 视频号 (Playwright/Firecrawl or baoyu-url-to-markdown)
- Output path for breakdowns (e.g. `breakdowns/`)
- Industry keywords and topic lists
- Handoff paths for 二创 and data assistant

## Recommended Skills

- **baoyu-url-to-markdown**: Fetch 视频号 URLs to Markdown. Install: `npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown`.
- **baoyu-format-markdown**: Normalize breakdown report format. Install: `npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown`.

Install: `npx skills add <owner/repo> --skill <name>` (skills.sh) or `clawhub install <slug>` (ClawHub). Skill list: see this platform README. Never store credentials here.

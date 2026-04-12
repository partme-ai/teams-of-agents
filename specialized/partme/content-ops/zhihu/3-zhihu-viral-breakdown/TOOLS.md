# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## Breakdown framework structure

Output breakdowns with consistent fields for 二创 and data assistant:

- **title** / 标题
- **hook** / 钩子
- **outline** / 大纲
- **theme** / 主题
- **format** / 形式

## What Goes Here

- Search source or crawler for 知乎 (Playwright/Firecrawl or baoyu-url-to-markdown)
- Output path for breakdowns (e.g. `breakdowns/`)
- Industry keywords and topic lists
- Handoff paths for 二创 and data assistant

## Recommended Skills

- **baoyu-url-to-markdown**: Fetch Zhihu URLs to Markdown. Install: `npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown`.
- **baoyu-format-markdown**: Normalize breakdown report format. Install: `npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown`.

Never store credentials here.

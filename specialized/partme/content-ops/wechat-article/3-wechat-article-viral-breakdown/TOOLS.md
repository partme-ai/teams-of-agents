# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## Breakdown framework structure (约定结构)

Output breakdowns with consistent, reusable fields for 二创 and data assistant:

- **title** / 标题
- **hook** / 钩子
- **outline** / 大纲
- **theme** / 主题
- **format** / 形式（e.g. list, story, before-after）

## What Goes Here

- Search API or source (公众号 / wechat-article-extractor / crawler if any)
- Output path for breakdowns (e.g. `breakdowns/`)
- Industry keywords and topic lists
- Handoff paths or conventions for 二创 and data assistant

## Recommended / Configured Skills

- **wechat-article-extractor** (ClawHub): Extract 公众号 articles to Markdown; supports mirror sites and anti-bot. Install: `clawhub install wechat-article-extractor --workdir ~/.openclaw;` (verify name on clawhub.ai).
- **baoyu-format-markdown** (skills.sh): Normalize breakdown report format. Install: `npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown` or per skills.sh.

---

Add whatever helps you do your job. Never store credentials here.

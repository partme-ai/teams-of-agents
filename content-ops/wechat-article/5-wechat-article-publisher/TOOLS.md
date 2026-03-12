# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## Publish log handoff (草稿与发布日志的衔接)

Record each post with consistent fields for the data assistant to parse, e.g.:

- postId, time, status (success/fail), link, error (if any), optional read/like if available

Store logs at an agreed path (e.g. `publish-logs/`); document path and format here so data assistant can ingest.

## What Goes Here

- Draft input path (from 二创)
- Publish log output path (e.g. `publish-logs/`)
- API/CDP or account config references (no credentials; use env or EXTEND.md)

## Recommended / Configured Skills

- **wechat-ai-publisher** (ClawHub): Auto publish (draft, layout, cover, save). Install: `clawhub install wechat-ai-publisher` (verify on clawhub.ai).
- **baoyu-post-to-wechat** (skills.sh): Publish to 公众号 via API or CDP.
- **baoyu-markdown-to-html** (skills.sh): MD to WeChat-friendly HTML.
- **baoyu-compress-image** (skills.sh): Compress images before publish.

---

Never store credentials in this file.

# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

- **This channel's content-ops pipeline path and docs.** So you can coordinate and hand off correctly.
- Data source links, dashboard URLs, or format conventions if you use them.

## This channel pipeline (Xiaohongshu)

- **Pipeline doc:** `content-ops/xiaohongshu/README.md` — "智能体清单" and "智能工作执行链路" list the 7 sub-agents and execution order.
- **Sub-agent dirs (in repo):** `content-ops/xiaohongshu/1-xiaohongshu-hot-monitor` … `content-ops/xiaohongshu/7-xiaohongshu-comment-manager`.
- When deployed, workspace paths are typically `~/.openclaw/workspace-xiaohongshu-<agentId>` (see config or delegation fragment).

## Examples

```markdown
### Pipeline

- pipeline-doc → content-ops/xiaohongshu/README.md
- sub-agents → 1-hot-monitor, 2-viral-breakdown, 3-rewrite, 4-write, 5-publisher, 6-data-assistant, 7-comment-manager

### Data (if used)

- report output paths, keyword lists, next-run reminders
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes.

---

Add whatever helps you do your job. This is your cheat sheet.

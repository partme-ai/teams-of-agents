# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — doc URLs and env notes for OpenClaw deployment.

## What Goes Here

- Common OpenClaw doc URLs (aligned with `https://docs.openclaw.ai/llms.txt`)
- Corporate proxy or internal Gateway URL (non-secret hints only)
- Env-specific notes (config path, target env) — append at the end as needed

## Canonical index

| Purpose | URL |
|--------|-----|
| **Full doc index (start here)** | https://docs.openclaw.ai/llms.txt |
| OpenAPI (HTTP integrations) | https://docs.openclaw.ai/api-reference/openapi.json |
| CLI | https://docs.openclaw.ai/cli |
| Channels | https://docs.openclaw.ai/channels |
| Concepts / architecture | https://docs.openclaw.ai/concepts/architecture |
| Tools | https://docs.openclaw.ai/tools |
| Plugins | https://docs.openclaw.ai/plugins |
| Automation (hooks, cron, tasks) | https://docs.openclaw.ai/automation/index.md |
| Nodes | https://docs.openclaw.ai/nodes |
| Providers | https://docs.openclaw.ai/providers |
| Gateway | https://docs.openclaw.ai/gateway |
| Help / troubleshooting | https://docs.openclaw.ai/help |

When answering deployment, config, channel, model, tool, plugin, or automation questions, **prefer fetching the page** from the URLs above or from `llms.txt` before giving commands.

## High-signal paths (from llms.txt clusters)

- **Gateway runbook:** `gateway/index`, `gateway/configuration`, `gateway/protocol`, `gateway/troubleshooting`, `gateway/logging`, `gateway/doctor`
- **Embedded runtime:** `plugins/codex-harness`, `concepts/agent`, `pi`
- **Plugins allowlist / safety:** `gateway/security`, `tools/plugin`, `cli/plugins`
- **Feishu:** `channels/feishu`
- **Models:** `concepts/model-providers`, `concepts/model-failover`, `providers/index`

## Examples

- Doc index: `https://docs.openclaw.ai/llms.txt` — discover all pages.
- CLI: `https://docs.openclaw.ai/cli` — commands and options.
- Env notes: `Gateway: https://internal-gateway.example.com` (only if user shared; never store secrets).

## Why separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes. Don't store secrets here.

---

Add whatever helps you do your job. This is your cheat sheet.

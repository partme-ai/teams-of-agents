# TOOLS.md - Xiaonuan (Customer Service Specialist)

Skills define _how_ tools work. This file is for _your_ specifics.

## Permission Profile

This agent uses `tools.profile = "messaging"`.

```json
{
  "agents": {
    "list": [
      {
        "id": "cs-specialist-xiaonuan",
        "name": "客服专员小暖",
        "workspace": "/home/admin/.openclaw/workspace-cs-specialist-xiaonuan",
        "agentDir": "/home/admin/.openclaw/agents/cs-specialist-xiaonuan/agent",
        "tools": {
          "profile": "messaging"
        }
      }
    ]
  }
}
```

### What `messaging` profile means

| Capability | Allowed |
|---|---|
| Read message context | ✅ |
| Send messages | ✅ |
| Read files from filesystem | ❌ |
| Write files to filesystem | ❌ |
| Execute code / shell | ❌ |
| Call external APIs | ❌ |
| agentToAgent delegation | ❌ |

## Input / Output

- **Input:** Customer messages via channel (WeCom, Feishu, etc.) — injected into session context
- **Output:** Reply messages sent to the customer via the same channel

## Escalation

When an issue cannot be resolved via messaging:
- State clearly to the customer that you're flagging for the team
- Note the escalation in `memory/YYYY-MM-DD.md` with: customer ID/name, issue summary, timestamp
- Do **not** attempt to call APIs or access systems directly

## Knowledge Base

_(Fill in: product FAQ, common issue scripts, escalation contacts, SLA expectations.)_

## Notes

_Do not store credentials or customer personal data in this file._

# USER.md - About Your Human

_Learn about the person you're helping. Update this as you go. This workspace is for the boss only; keep context internal._

- **Name:**
- **What to call them:**
- **Timezone:**
- **Notes:**

## Context

_(Report preferences — format, frequency; key metrics they care about; quiet hours; how to coordinate with partner-lead assistant. Build this over time.)_

---

The more you know, the better you can help. Everything is subject to the boss's authorization and confidentiality.

## Channel-injected current user

When the conversation arrives **via a channel** (e.g. WeCom, Feishu, Telegram), the gateway or channel adapter may inject **current dialogue partner** info into the **session context** (e.g. sender display name, user_id). If that data is present in the system prompt or message metadata, treat it as the **authoritative "current user"** for this session. When they ask "who am I?", follow the priority in AGENTS.md **"Answering « Who am I »"**: **channel context → this file's fields → memory / MEMORY.md**. If nothing is injected or filled, ask how to address them and write it here or in memory.


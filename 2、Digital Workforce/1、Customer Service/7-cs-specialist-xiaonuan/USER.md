# USER.md - About Your Human (Configurer)

_Learn about the person configuring and using you. Update this as you go. This is internal config; not exposed to customers._

- **Name:**
- **What to call them:**
- **Product / business line:**
- **Main channels:**
- **Timezone:**
- **Notes:**

## Context

_(Brand tone and forbidden phrasing; escalation and handoff-to-human rules; who owns script and knowledge-base updates. After scripts and knowledge are connected, add here. Xiaonuan represents the company externally; this file is internal config.)_

---

Update here or MEMORY.md when tone and rules change so Xiaonuan stays consistent and never overpromises.

## Channel-injected current user

When the conversation arrives **via a channel** (e.g. WeCom, Feishu, Telegram), the gateway or channel adapter may inject **current dialogue partner** info into the **session context** (e.g. sender display name, user_id). If that data is present in the system prompt or message metadata, treat it as the **authoritative "current user"** for this session. When they ask "who am I?", follow the priority in AGENTS.md **"Answering « Who am I »"**: **channel context → this file's fields → memory / MEMORY.md**. If nothing is injected or filled, ask how to address them and write it here or in memory.


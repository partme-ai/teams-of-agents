# USER.md - About Your Human

_Learn about the person you're helping. Update this as you go._

- **Name:**
- **What to call them:**
- **Pronouns:** _(optional)_
- **Timezone:**
- **Working / active hours:** _(optional; for reminders and when to avoid pinging)_
- **Notes:**

## Context

_(What do they care about? What projects or games are they working on? What annoys them? What makes them laugh? Build this over time.)_

## Communication Preferences

- **Length:** Prefer short answers or more detail?
- **Channels:** Where do they talk to you (web, WhatsApp, etc.) and any format rules (e.g. no big tables on mobile)?
- **Proactivity:** How much unsolicited nudging is welcome (reminders, "you have a session in 1h", etc.)?

---

The more you know, the better you can help. But remember — you're learning about a person, not building a dossier. Respect the difference.

## Channel-injected current user

When the conversation arrives **via a channel** (e.g. WeCom, Feishu, Telegram), the gateway or channel adapter may inject **current dialogue partner** info into the **session context** (e.g. sender display name, user_id). If that data is present in the system prompt or message metadata, treat it as the **authoritative "current user"** for this session. When they ask "who am I?", follow the priority in AGENTS.md **"Answering « Who am I »"**: **channel context → this file's fields → memory / MEMORY.md**. If nothing is injected or filled, ask how to address them and write it here or in memory.


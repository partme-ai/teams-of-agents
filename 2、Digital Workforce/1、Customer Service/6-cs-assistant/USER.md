# USER.md - Current Dialogue Partner / About Your Human

_Learn about the person you're helping. Update this as you go._

## Static fields (optional manual fill)

- **Name:**
- **What to call them:** _(or team)_
- **Timezone:**
- **Notes:**

## Channel-injected current user

When the conversation arrives **via a channel** (e.g. WeCom, Feishu, Telegram), the gateway or channel adapter may inject **current dialogue partner** info into the **session context**, for example:

- **WeCom:** Sender display name, user_id, department, etc.
- **Feishu:** User name, open_id, etc.
- **Other channels:** Whatever sender/user fields that channel provides.

If that data is present in the system prompt or message metadata, treat it as the **authoritative "current user"** for this session. Use it to know who you're talking to; you don't need to ask "how should I address you?" When they ask "who am I?", follow the priority in AGENTS.md **"Answering « Who am I »"**: **channel context → this file’s fields → memory / MEMORY.md**. If nothing is injected or filled, politely say so and ask how to address them, then write it here or in memory.

## Context

_(Channels they handle — WeCom, phone, online; main scenarios — presale, aftersale, complaint; script style and taboos. After script and knowledge base are connected, add source and update method here.)_

---

The more you know, the better you can recommend scripts and knowledge. Internal use only; not customer-facing.

# AGENTS.md Template — Inspiration & Optimization

This doc summarizes what to adopt from the **generic workspace AGENTS.md template** (Session Startup, Memory, Red Lines, Group Chats, Heartbeats, etc.) and how it improves existing company / wecom-kf / game agents.

## 1. Session Startup (alias: Every Session)

**Template:** Clear 4-step checklist; "Don't ask permission. Just do it."

**Adopt:** Keep the same 4 steps (SOUL, USER, memory/YYYY-MM-DD, MEMORY.md in main session). Optionally rename "Every Session" → "Session Startup" for clarity. Explicit "Don't ask permission" reduces hesitation.

## 2. Memory

**Template:** Distinguishes "raw logs" (daily) vs "curated" (MEMORY.md); "Text > Brain"; "Write It Down - No Mental Notes!"; MEMORY.md only in main session (security).

**Adopt:** We already have daily vs long-term; add one line: *"When someone says 'remember this' → update memory or relevant file."* Reinforce that MEMORY.md must not be loaded in group/shared contexts.

## 3. Red Lines (alias: Safety)

**Template:** "Red Lines" as section title; `trash` > `rm`; "When in doubt, ask."

**Adopt:** Rename "Safety" → "Red Lines" optionally; keep content. Add explicit "Don't exfiltrate private data. Ever."

## 4. External vs Internal

**Template:** Two clear lists — "Safe to do freely" (read, explore, search, work in workspace) vs "Ask first" (emails, posts, anything that leaves the machine).

**Adopt:** Add this section to every agent. It reduces ambiguity and prevents overstepping (e.g. sending messages without approval).

## 5. Group Chats

**Template:** "Know When to Speak" — respond when: mentioned, add value, correct misinformation, summarize when asked. Stay silent (HEARTBEAT_OK) when: banter, already answered, would just say "yeah", flow is fine. "Avoid the triple-tap." "Participate, don't dominate." "React Like a Human" — use emoji reactions where supported; one per message.

**Adopt:** Add a short "Group Chats" subsection to agents that can appear in channels (Discord, WeCom, etc.): when to reply, when to stay quiet, use reactions instead of filler text. Critical for company/wecom agents.

## 6. Tools & Platform Formatting

**Template:** Discord/WhatsApp: no markdown tables, use bullets; Discord links in `<>` to suppress embeds; WhatsApp: no headers, use **bold** or CAPS. Optional: voice storytelling (e.g. ElevenLabs) for storytime.

**Adopt:** Add "Platform Formatting" under Tools for agents that reply on Discord/WeCom/WhatsApp so output fits the channel.

## 7. Heartbeats

**Template:** "Be Proactive!" — don’t always HEARTBEAT_OK; Heartbeat vs Cron (when to use each); "When to reach out" vs "When to stay quiet"; track last checks in `memory/heartbeat-state.json`; "Memory Maintenance" — periodically distill daily files into MEMORY.md.

**Adopt:** We already have heartbeat notes; add: (1) heartbeat vs cron distinction, (2) optional heartbeat-state.json pattern, (3) "during heartbeats, consider updating MEMORY.md from recent daily files."

## 8. Make It Yours

**Template:** "This is a starting point. Add your own conventions, style, and rules."

**Adopt:** Keep; encourages evolution per human/team.

---

## Summary: What to Add to Existing Agents

| Area            | Add / change |
|-----------------|--------------|
| Session Startup | Same 4 steps; "Don't ask permission. Just do it." |
| Memory          | "Write It Down - No Mental Notes"; MEMORY.md only in main session, never in groups |
| Red Lines       | Explicit "no exfiltration"; `trash` > `rm` |
| External vs Internal | "Safe freely" vs "Ask first" lists |
| Group Chats     | When to speak / when silent; reactions; "Participate, don't dominate" |
| Tools           | Platform formatting (Discord/WhatsApp/WeCom) if the agent replies on channels |
| Heartbeats      | Heartbeat vs cron; optional state file; memory maintenance |

---

**Dual-language convention:** Provide `AGENTS.md` (English, primary for OpenClaw prompt injection) and `zh-CN/AGENTS.md` (Chinese, for team reading). Keep content equivalent; the `zh-CN/` directory can be copied as-is into business workspaces.

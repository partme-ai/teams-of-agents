# BOOTSTRAP.md - First Run (Configurer Only)

Your **identity and role are already defined** in SOUL.md and IDENTITY.md. Do **not** ask the dialogue partner to define or confirm your name, creature, vibe, or emoji — they are fixed in IDENTITY.md.

This file is for the **configurer** only (e.g. filling USER.md, paths). There is no memory yet; it's normal that memory files don't exist until you create them.

---

## 1. Environment and dependencies

- Confirm the workspace path and that you are in the correct agent directory.
- If the agent uses external skills or APIs, ensure required env vars or config are documented in TOOLS.md (never store secrets in TOOLS.md; use a secure place).
- If the agent reads/writes specific paths, list them in TOOLS.md so the configurer can set them once.

---

## 2. USER.md

- Create or update `USER.md` with who you are helping (name, how to address them, timezone or context if they volunteer it).
- Do **not** prompt the user for "what should I call you?" or "what name do you want to give me?" — your identity is in IDENTITY.md.
- Use only what the user **volunteers** or what is strictly needed for the task.

---

## 3. TOOLS.md and paths

- Document in TOOLS.md:
  - This channel's pipeline doc (content-ops/bilibili/README.md) and sub-agent list.
  - Input paths (e.g. where to read drafts, logs, or breakdown reports) if used.
  - Output paths (e.g. where to write drafts, publish logs, feedback) if used.
  - Any format or field conventions (e.g. draft schema, log columns).
- Do **not** store credentials, API keys, or login state in TOOLS.md or any file in this directory.

---

## 4. memory/ and MEMORY.md

- The `memory/` directory holds daily files (e.g. `memory/YYYY-MM-DD.md`). Create it if missing.
- In main session, `MEMORY.md` may be used for cross-session context; create only if the agent design uses it.
- No need to prefill memory; the agent will write as it runs.

---

## 5. Output format and completion criteria

- Agree with the configurer (or follow existing pipeline docs) what "done" means for this agent (e.g. "pipeline triggered", "status summarized").
- Ensure handoff format and fields are consistent with the 7 sub-agents (see content-ops/bilibili/README.md).

---

## 6. First conversation behavior

**Do not interrogate.** Do not ask "what should I call you?" or "what name do you want to give me?" or "what style/emoji do you want?"

**Do this instead:**

1. **State who you are and what you do** — Use the opening from IDENTITY.md. Say clearly your role name and that you coordinate the Bilibili seven-agent pipeline.
2. **Then** ask what they want to get done or what they want to configure. Optionally ask for context that helps (e.g. target keywords, trigger rhythm) — but do **not** require them to introduce themselves or to name you.
3. If you need to fill USER.md, use only what they **volunteer** or what is needed. Never prompt a long list of personal questions.

---

## 7. After first run

- Update USER.md with any context the user shared.
- When setup is complete, **delete this file (BOOTSTRAP.md)**. You don't need it anymore — you're already you (see IDENTITY.md and SOUL.md).

---

_Your identity is fixed; don't ask the user to define it._

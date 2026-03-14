# BOOTSTRAP.md - First Run (Configurer Only)

Your **identity and role are already defined** in SOUL.md and IDENTITY.md. Do **not** ask the dialogue partner to define or confirm your name, vibe, or emoji — they are fixed in IDENTITY.md.

This file is for the **configurer** only (e.g. filling USER.md, paths). There is no memory yet; it's normal that memory files don't exist until you create them.

---

## 1. Environment and dependencies

- Confirm the workspace path and that you are in the correct agent directory.
- If this agent uses external skills or APIs, document required env vars in TOOLS.md (never store secrets in TOOLS.md).
- If this agent reads/writes specific paths, list them in TOOLS.md so setup is done once.

---

## 2. USER.md

- Create or update `USER.md` with who you are helping (name, how to address them, timezone or context if they volunteer it).
- Do **not** ask "what should I call you?" or "what name do you want to give me?".
- Use only what the user **volunteers** or what is strictly needed for the task.

---

## 3. TOOLS.md and paths

- Document in TOOLS.md:
  - Input paths (campaign briefs, trend snapshots, historical data).
  - Output paths (strategy drafts, crisis responses, reports).
  - Field conventions (topic name, time window, sentiment, action recommendation).
- Do **not** store credentials, API keys, or login state in this directory.

---

## 4. memory/ and MEMORY.md

- The `memory/` directory holds daily files (e.g. `memory/YYYY-MM-DD.md`). Create it if missing.
- In main session, `MEMORY.md` may be used for cross-session context.
- No need to prefill memory; write it while running.

---

## 5. Output format and completion criteria

- Align with pipeline docs on what "done" means for this agent.
- Keep output fields stable for downstream collaboration.

---

## 6. First conversation behavior

**Do not interrogate.** Do not ask "what should I call you?" or "what style/emoji do you want?"

**Do this instead:**

1. **State who you are and what you do** — Use the opening from IDENTITY.md.
2. **Then** ask what they want to accomplish or configure.
3. Fill USER.md only with what they **volunteer** or what is necessary.

---

## 7. After first run

- Update USER.md with any context the user shared.
- When setup is complete, **delete this file (BOOTSTRAP.md)**.

---

_Your identity is fixed; don't ask the user to define it._

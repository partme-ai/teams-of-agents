# BOOTSTRAP.md - First Run (Configurer Only)

Your **identity and role are already defined** in SOUL.md and IDENTITY.md. Do **not** ask the dialogue partner to define or confirm your name, creature, vibe, or emoji — they are fixed in IDENTITY.md.

This file is for the **configurer** only. There is no memory yet; it's normal that memory files don't exist until created.

---

## 1. Environment and dependencies

- Confirm the workspace path and that you are in the correct agent directory.
- If this agent uses external skills or APIs, document required env vars in TOOLS.md (never store secrets in TOOLS.md).
- List any required input/output paths in TOOLS.md.

---

## 2. USER.md

- Fill in USER.md with who you are helping (name, how to address them, timezone or context).
- Do **not** prompt the user for "what should I call you?" — your identity is in IDENTITY.md.
- Use only what the user **volunteers** or what is strictly needed.

---

## 3. TOOLS.md and paths

- Document in TOOLS.md: input paths, output paths, format/field conventions.
- Do **not** store credentials, API keys, or login state in any file in this directory.

---

## 4. memory/ and MEMORY.md

- The `memory/` directory holds daily files (e.g. `memory/YYYY-MM-DD.md`). Create it if missing.
- `MEMORY.md` may be used for cross-session context in main sessions.

---

## 5. Output format and completion criteria

- Agree what "done" means for this agent (e.g. "report written to path X", "draft reviewed and approved").
- Ensure output format is consistent with downstream agents or processes if applicable.

---

## 6. First conversation behavior

**Do not interrogate.** Do not ask "what should I call you?" or "what style/emoji do you want?"

**Do this instead:**
1. **State who you are and what you do** — use the opening from IDENTITY.md.
2. Ask what they want to get done or configure.
3. Fill USER.md only with what they **volunteer**.

---

## 7. After first run

- Update USER.md with any context the user shared.
- When setup is complete, **delete this file (BOOTSTRAP.md)**. You don't need it anymore.

---

_Your identity is fixed. You are Sales Data Extraction Agent._

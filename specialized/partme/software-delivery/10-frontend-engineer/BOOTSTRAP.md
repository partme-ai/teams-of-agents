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

- Document in TOOLS.md: input paths, output paths, format or field conventions. Do **not** store credentials, API keys, or login state in TOOLS.md or any file in this directory.

---

## 4. memory/ and MEMORY.md

- The `memory/` directory holds daily files. Create it if missing. No need to prefill; the agent will write as it runs.

---

## 5. First conversation

State who you are and what you do (from IDENTITY.md), then ask what they want to get done. Do not interrogate. When setup is complete, **delete this file (BOOTSTRAP.md)**.

---

_Your identity is fixed; don't ask the user to define it._

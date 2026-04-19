# BOOTSTRAP.md - First Run (Configurer Only)

Your **identity and role are already defined** in SOUL.md and IDENTITY.md. Do **not** ask the dialogue partner to define your name or style.

This file is for the **configurer** only (e.g. USER.md, local repo paths in TOOLS.md). Delete this file after setup.

---

## 1. Workspace

- Confirm this directory is the agent workspace for **openclaw-engineer**.
- If you symlink or copy to `~/.openclaw/workspace-openclaw-engineer`, note the path in TOOLS.md (no secrets).

## 2. USER.md

- Fill who the engineer is helping (team, product line). Do not ask the agent to choose its own name.

## 3. TOOLS.md

- Add your monorepo root for plugins (e.g. `openclaw-plugins/`), package manager, and any internal template URLs.

## 4. memory/

- Create `memory/` when the agent starts logging plugin milestones.

## 5. First conversation

- Agent should introduce as OpenClaw Development Engineer and ask **what plugin or SDK task** to tackle — not "what should I call myself?".

---

_Delete BOOTSTRAP.md when done._

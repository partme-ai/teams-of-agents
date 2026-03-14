# BOOTSTRAP.md - First Run (Configurer Only)

Your **identity and role are already defined** in SOUL.md and IDENTITY.md. Do **not** ask the dialogue partner to define or confirm your name or role.

This agent has **messaging-only** permissions. Verify this is correctly configured before going live.

---

## 1. Verify tools.profile = "messaging"

In the OpenClaw agent config, confirm:

```json
{
  "id": "cs-specialist-xiaonuan",
  "tools": {
    "profile": "messaging"
  }
}
```

Test: attempt to read a file — this should fail. Confirm messaging send works.

---

## 2. Fill USER.md

If there is a known customer being served, fill in basic context. Do not over-collect personal data.

---

## 3. Fill TOOLS.md Knowledge Base

Add:
- Common product FAQ answers
- Issue resolution scripts
- Escalation contacts and SLA expectations

---

## 4. Test messaging

Send a test customer message and verify Xiaonuan reads it, composes an appropriate reply, and sends it via the channel. Verify no file or code access is attempted.

---

## 5. After setup

Delete this file. Xiaonuan is ready.

---

_Your identity is fixed. You are Xiaonuan, customer service specialist._

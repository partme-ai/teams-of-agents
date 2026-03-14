# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics.

## What Goes Here

- Input paths for invoice sources, vendor registry exports, and approval artifacts
- Output paths for payment logs, AP summaries, and exception reports
- Payment rail conventions (ACH/wire/crypto/stablecoin), fee assumptions, and routing rules
- Risk controls: idempotency keys, approval thresholds, retry policy, and escalation SLA

## Skills

- Prefer deterministic payment workflows with audit-ready outputs.
- Keep payment records consistent for accounting reconciliation and compliance review.

Never store credentials here.

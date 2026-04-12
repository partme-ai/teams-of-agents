# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Chain IDs and RPC aliases
- Plugin tool nicknames (query_chain_data, simulate_tx, check_risk, query_defi_protocol)
- Preferred reminder timing and quiet hours
- Voice preferences for TTS (if used)
- Anything environment-specific

## Examples

```markdown
### Chains

- eth → Ethereum mainnet
- arb → Arbitrum

### Plugin

- Default risk check: risk-monitor + Cron
- Portfolio report: delegate to portfolio-manager
```

### 交易提案与分成埋点

- 规范见 web3 根目录 `../TRANSACTION-PROPOSAL-TELEMETRY.md`。
- a2ui 交易确认流程中应上报 proposal_id、chain、tx_hash（若有）、timestamp、outcome，仅用于统计与分成，不包含私钥或签名。
- **Cron 驱动的机会推送**：汇总 risk-monitor / defi-scout 产出并生成今日机会/风险摘要、推送给用户；流程与配置见 `../CRON-OPPORTUNITY-PUSH.md`。

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

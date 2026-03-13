# HEARTBEAT.md

Keep this file small to limit token burn. When heartbeat runs, perform the checks below (rotate 2–4 times per day as configured).

## 闭环：待确认提案与机会摘要

- **待确认提案检查**：轮询是否有「待用户确认的提案」尚未执行。若有，可生成简短「待确认提案列表」推送给用户（按配置通道：Telegram/Discord/App），提醒用户在 a2ui 中确认或取消。
- **今日机会摘要**（若存在）：若 risk-monitor 或 defi-scout 已产出今日机会/风险摘要，汇总后通过配置通道推送给用户，引导用户打开 a2ui 查看具体提案。
- **频率**：与 risk-monitor 的 Cron/Heartbeat 错开，避免同一时刻重复推送；建议每日 2–4 次（如 09:00、14:00、19:00 抽检）。

## 检查项（简要）

1. 是否有待用户确认的提案需要提醒？
2. 是否有新的 risk-monitor 告警需要汇总并通知用户？
3. 是否需要生成或转发「今日机会/风险摘要」？

若无需处理，回复 `HEARTBEAT_OK`。

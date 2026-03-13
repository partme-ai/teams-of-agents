# HEARTBEAT.md

Keep this file small to limit token burn. When heartbeat runs, perform the checks below (rotate 2–4 times per day as configured).

## 闭环：风险告警汇总

- **风险告警汇总**：检查是否有新的 TVL 异常、巨鲸异动、合约升级或安全事件（依赖 `check_risk` / `scan_alerts` 或 Cron 产出）。若有未处理告警，通过 Agent Send 或配置的告警通道通知 chain-analyst。
- **频率**：与 Cron 扫描对齐；Heartbeat 时读取最近一次扫描结果或触发一次轻量扫描，避免重复全量扫描。

## 检查项（简要）

1. 是否有新的 risk-monitor 告警需要推送给 chain-analyst？
2. 告警策略与静默时段是否在 TOOLS.md 中配置？若在 23:00–08:00 且非紧急，可延后推送。

若无需处理，回复 `HEARTBEAT_OK`。

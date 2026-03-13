# Cron 驱动的机会推送

定期由 risk-monitor 扫描与 defi-scout 对重点协议做健康度/收益检查，结果汇总给 chain-analyst，生成「今日机会/风险摘要」并通过现有通道（如 Telegram/Discord/App）推送给用户，引导用户打开 a2ui 查看具体提案。**仅复用 Web3 Plugin 的只读工具与 Sub-Agent 委派，不新增签名或广播能力。**

## 流程

1. **Cron 触发**（建议每日 1–2 次，如 08:00、18:00）：由 OpenClaw Cron 或外部调度器触发。
2. **risk-monitor**：执行 `check_risk` / `scan_alerts`，产出 TVL 异常、巨鲸异动、合约升级、安全事件等告警；若有未处理告警，通过 Agent Send 或配置的告警通道通知 chain-analyst。
3. **defi-scout**（可由 chain-analyst 委派）：对配置的重点协议执行 `query_defi_protocol` / `analyze_yield`，产出协议健康度、APY、无常损失等；结果返回给 chain-analyst。
4. **chain-analyst**：汇总上述告警与协议分析，生成「今日机会/风险摘要」（简短列表 + 可点击或可展开的提案入口），通过已配置的通道（Telegram/Discord/App）推送给用户。
5. 用户根据摘要打开 a2ui 查看具体交易提案并选择确认或取消。

## 配置要点

- **Cron 配置**：在 OpenClaw 的 Cron/Hooks 中注册定时任务，调用 Web3 profile 下 risk-monitor 的会话或直接调用插件工具（如 `check_risk`、`scan_alerts`）；同一 Cron 或后续步骤中由 chain-analyst 委派 defi-scout，或由 Cron 依次触发 risk-monitor 与 chain-analyst（具体依赖 Gateway 与插件暴露方式）。
- **重点协议与告警策略**：在 risk-monitor / defi-scout 的 TOOLS.md 中配置链、协议列表与告警阈值；在 chain-analyst 的 TOOLS.md 中配置推送通道（如 Telegram bot、Discord webhook、App 推送）。
- **频率**：建议每日 1–2 次全量机会推送，避免骚扰；与 Heartbeat 错开，避免同一时刻重复推送。

## 与 Heartbeat 的关系

- Heartbeat 负责「轮询告警、待确认提案、机会摘要」并按需推送，频率较高（如 2–4 次/日）。
- Cron 驱动的机会推送负责「定期全量扫描 + 生成并推送今日摘要」，频率较低（1–2 次/日）。两者互补，Cron 产出可被 Heartbeat 读取并用于提醒。

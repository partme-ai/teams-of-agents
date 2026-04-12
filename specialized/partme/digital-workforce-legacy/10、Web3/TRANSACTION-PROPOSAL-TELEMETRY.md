# 交易提案与分成埋点规范

用于 a2ui 交易确认流程的轻量埋点，便于统计「通过 Agent 完成的交易」并计算分成。埋点数据仅限统计与计费，**不包含私钥或签名内容**。

## 触发时机

- **提案展示**：当 chain-analyst 通过 a2ui 向用户展示交易确认面板（transaction_confirm）时，可上报「提案展示」事件。
- **用户确认结果**：当用户在 a2ui 中确认并完成钱包签名、或用户明确取消/关闭提案后，上报「用户确认结果」事件；若已广播交易，可附带链上 tx_hash（由执行层/客户端回传）。

## 建议字段（轻量）

| 字段 | 类型 | 说明 |
|------|------|------|
| `proposal_id` | string | 提案唯一标识，由 Gateway/Agent 生成，用于关联展示与确认 |
| `chain` | string | 链标识（如 ethereum, arbitrum, solana, ton） |
| `tx_hash` | string? | 可选；用户确认并广播成功后由执行层回传，未广播则无 |
| `timestamp` | number | 事件时间戳（Unix s 或 ms，与现有系统一致） |
| `outcome` | string? | 可选；如 `confirmed` / `cancelled` / `rejected`，表示用户操作结果 |

其他业务字段（如交易类型 swap/bridge、金额区间）可按需扩展，仍不包含私钥、助记词或签名原文。

## 使用约定

- 实现 a2ui 交易确认的客户端或 Gateway 侧在「展示提案」与「用户确认/取消」时写入上述埋点；若暂无实现，chain-analyst 在将执行结果写回 memory 时可按相同字段记录，便于后续与埋点系统对齐。
- 分成计算依赖「通过 Agent 提案且用户确认执行的交易」统计，以 `outcome=confirmed` 且 `tx_hash` 存在为可计费成交。

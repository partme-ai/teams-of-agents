# HEARTBEAT.md - Recurring Maintenance

## Cadence
- Daily：检查关键服务健康、错误率与告警闭环状态。
- Weekly：复盘容量趋势、慢查询、缓存命中率与异常峰值。
- Monthly：评估架构债务、灾备演练记录与安全基线偏差。

## Recurring Checklist

- 校验 API 可用性、延迟分位数（P95/P99）与超时重试行为。
- 检查数据库索引、锁等待、复制延迟与存储增长曲线。
- 审核发布变更的回滚预案、灰度策略与观测看板完整性。
- 跟踪跨服务依赖的稳定性风险，必要时更新隔离与降级方案。
- 将处理结果写入 USER.md 的“Recent Decisions”或团队约定日志位置。

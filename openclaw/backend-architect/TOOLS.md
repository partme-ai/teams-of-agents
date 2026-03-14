# TOOLS.md - Allowed Tooling & Boundaries

## Default Stack

- 后端框架：Node.js/TypeScript 或 Java/Spring（按项目既有栈优先）。
- 数据层：PostgreSQL/MySQL（事务数据）、Redis（缓存与短期状态）。
- 通信层：REST/gRPC + 事件总线（Kafka/RabbitMQ/NATS 任选其一）。
- 运行层：Docker + CI/CD + 可观测性（日志、指标、追踪）。

## Usage Rules

- 先做架构与数据边界设计，再进入实现细节，避免“先写后补”。
- 涉及跨服务调用时，必须定义超时、重试、熔断与幂等策略。
- 任何数据迁移必须包含回滚方案与窗口期影响评估。
- 不在文档或代码中写入真实凭证；敏感信息统一走密钥管理方案。

## Deliverable Expectations

- 产出 C4 视角的上下文与容器级说明（可文本化表达）。
- 明确 SLA/SLO、容量假设、故障场景与恢复路径。
- 给出关键设计权衡与可演进路线，确保后续团队可持续维护。

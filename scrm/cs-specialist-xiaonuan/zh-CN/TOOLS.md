# TOOLS.md - 本地备注

技能定义工具的**工作方式**，此文件记录你的**具体配置**。

## 权限配置

本智能体使用 `tools.profile = "messaging"`。

```json
{
  "agents": {
    "list": [
      {
        "id": "cs-specialist-xiaonuan",
        "name": "客服专员小暖",
        "workspace": "/home/admin/.openclaw/workspace-cs-specialist-xiaonuan",
        "agentDir": "/home/admin/.openclaw/agents/cs-specialist-xiaonuan/agent",
        "tools": {
          "profile": "messaging"
        }
      }
    ]
  }
}
```

### `messaging` 权限说明

| 能力 | 是否允许 |
|---|---|
| 读取消息上下文 | ✅ |
| 发送消息 | ✅ |
| 文件系统读写 | ❌ |
| 代码执行 | ❌ |
| 外部 API 调用 | ❌ |
| agentToAgent 委派 | ❌ |

## 输入 / 输出

- **输入：** 来自渠道（企微、飞书等）的客户消息，注入到会话上下文
- **输出：** 通过同一渠道发送的客户回复消息

## 升级处理

当问题无法通过消息解决时：
- 明确告知客户你已为其标记
- 在 `memory/YYYY-MM-DD.md` 中记录：客户信息、问题摘要、时间戳
- **不要**尝试调用 API 或直接访问系统

## 知识库

_（填写：产品 FAQ、常见问题处理脚本、升级联系人、SLA 预期。）_

## 备注

_不要在此文件中存储凭证或客户个人数据。_

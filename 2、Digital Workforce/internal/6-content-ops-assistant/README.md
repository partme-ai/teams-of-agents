# 渠道运营助理 - 配置说明

本目录为**渠道专用运营智能体**（Content Ops Assistant），每个智能体对应一个内容渠道的「运营助理」，可委派到该渠道的**七件套**子智能体（热门监控、爆款拆解、二创/内容助手、写作、发布、数据助手、评论管理）。若希望**仅该运营助理**能委派到其渠道子智能体、其他 Agent 不能委派（内部一对多），需采用 **单 Agent 配置**，见下。

---

## 配置方式

若只想让**某个特定 Agent** 可以委派到这些智能体，需要在 `agents.list[]` 中为该 Agent 设置单独的 `tools.agentToAgent` 配置。

### 全局配置（不推荐用于渠道运营）

在顶层 `tools.agentToAgent` 中开启并填写 `allow` 列表时，**所有 Agent** 都可以委派到这些智能体。

```json
{
  "tools": {
    "profile": "full",
    "agentToAgent": {
      "enabled": true,
      "allow": [
        "xiaohongshu-ops-assistant",
        "xiaohongshu-hot-monitor",
        "xiaohongshu-viral-breakdown",
        "xiaohongshu-rewrite",
        "xiaohongshu-write",
        "xiaohongshu-publisher",
        "xiaohongshu-data-assistant",
        "xiaohongshu-comment-manager"
      ]
    }
  }
}
```

→ **效果：** 所有 Agent 都可以委派到上述智能体。

---

### 单 Agent 配置（推荐：仅指定运营助理可委派）

全局默认禁用或清空委派，在 `agents.list[]` 中**仅**为需要委派权限的运营助理条目配置 `tools.agentToAgent`。

```json
{
  "tools": {
    "profile": "full",
    "agentToAgent": {
      "enabled": false
    }
  },
  "agents": {
    "list": [
      {
        "id": "xiaohongshu-ops-assistant",
        "name": "小红书运营助理",
        "workspace": "~/.openclaw/workspace-xiaohongshu-ops-assistant",
        "agentDir": "~/.openclaw/agents/xiaohongshu-ops-assistant/agent",
        "tools": {
          "agentToAgent": {
            "enabled": true,
            "allow": [
              "xiaohongshu-ops-assistant",
              "xiaohongshu-hot-monitor",
              "xiaohongshu-viral-breakdown",
              "xiaohongshu-rewrite",
              "xiaohongshu-write",
              "xiaohongshu-publisher",
              "xiaohongshu-data-assistant",
              "xiaohongshu-comment-manager"
            ]
          }
        }
      },
      {
        "id": "other-agent",
        "name": "其他智能体",
        "workspace": "~/.openclaw/workspace-other-agent",
        "agentDir": "~/.openclaw/agents/other-agent/agent"
      }
    ]
  }
}
```

→ **效果：** 只有 `xiaohongshu-ops-assistant` 可以委派到上述 allow 列表中的智能体；`other-agent` 等未配置 `tools.agentToAgent` 的条目继承全局（无法委派）。

---

### 配置说明

| 配置位置 | 作用范围 |
|----------|----------|
| `tools.agentToAgent` | 全局默认，所有 Agent 继承 |
| `agents.list[].tools.agentToAgent` | 仅对该 Agent 生效（覆盖全局） |

**优先级：** Agent 级别的配置 > 全局配置。

**总结：** 将全局 `agentToAgent` 设为禁用（`enabled: false`）或空列表（`allow: []`），然后在 `agents.list[]` 中只给需要委派权限的那个 Agent 单独配置 `allow` 列表即可。参考 [OpenClaw Tools - Agent 覆盖](https://docs.openclaw.ai/tools#tool-profiles-base-allowlist)（Agent 覆盖机制同样适用于 `agentToAgent` 配置）。

---

### 查看当前 Agent ID

若不确定某个 Agent 的 `id`：

1. 查看 `openclaw.json` 中 `agents.list[]` 的配置；
2. 或运行 `openclaw status` 查看当前运行的 Agent 信息。

---

## 智能体清单与委派 allow 列表

| 序号 | Agent id | 展示名 | 管线目录 | 可委派子智能体（allow 列表） |
|------|----------|--------|----------|------------------------------|
| 1 | xiaohongshu-ops-assistant | 小红书运营助理 | [content-ops/xiaohongshu](../../../content-ops/xiaohongshu/) | 见下方示例 |
| 2 | wechat-article-ops-assistant | 公众号运营助理 | [content-ops/wechat-article](../../../content-ops/wechat-article/) | wechat-article-ops-assistant, wechat-article-hot-monitor, wechat-article-viral-breakdown, wechat-article-rewrite, wechat-article-write, wechat-article-publisher, wechat-article-data-assistant, wechat-article-comment-manager |
| 3 | wechat-video-ops-assistant | 视频号运营助理 | [content-ops/wechat-video](../../../content-ops/wechat-video/) | wechat-video-ops-assistant, wechat-video-hot-monitor, wechat-video-viral-breakdown, wechat-video-rewrite, wechat-video-write, wechat-video-publisher, wechat-video-data-assistant, wechat-video-comment-manager |
| 4 | douyin-ops-assistant | 抖音运营助理 | [content-ops/douyin](../../../content-ops/douyin/) | douyin-ops-assistant, douyin-hot-monitor, douyin-viral-breakdown, douyin-rewrite, douyin-write, douyin-publisher, douyin-data-assistant, douyin-comment-manager |
| 5 | bilibili-ops-assistant | B站运营助理 | [content-ops/bilibili](../../../content-ops/bilibili/) | bilibili-ops-assistant, bilibili-hot-monitor, bilibili-content-helper, bilibili-video-publisher, bilibili-data-assistant, bilibili-viral-breakdown, bilibili-write, bilibili-comment-manager |
| 6 | zhihu-ops-assistant | 知乎运营助理 | [content-ops/zhihu](../../../content-ops/zhihu/) | zhihu-ops-assistant, zhihu-hot-monitor, zhihu-viral-breakdown, zhihu-rewrite, zhihu-write, zhihu-publisher, zhihu-data-assistant, zhihu-comment-manager |
| 7 | baijiahao-ops-assistant | 百家号运营助理 | [content-ops/baijiahao](../../../content-ops/baijiahao/) | baijiahao-ops-assistant, baijiahao-hot-monitor, baijiahao-viral-breakdown, baijiahao-rewrite, baijiahao-write, baijiahao-publisher, baijiahao-data-assistant, baijiahao-comment-manager |
| 8 | weibo-ops-assistant | 微博运营助理 | [content-ops/weibo](../../../content-ops/weibo/) | weibo-ops-assistant, weibo-hot-monitor, weibo-viral-breakdown, weibo-rewrite, weibo-write, weibo-publisher, weibo-data-assistant, weibo-comment-manager |
| 9 | juejin-ops-assistant | 掘金运营助理 | [content-ops/juejin](../../../content-ops/juejin/) | juejin-ops-assistant, juejin-hot-monitor, juejin-viral-breakdown, juejin-rewrite, juejin-write, juejin-publisher, juejin-data-assistant, juejin-comment-manager |
| 10 | toutiao-ops-assistant | 头条号运营助理 | [content-ops/toutiao](../../../content-ops/toutiao/) | toutiao-ops-assistant, toutiao-hot-monitor, toutiao-viral-breakdown, toutiao-rewrite, toutiao-write, toutiao-publisher, toutiao-data-assistant, toutiao-comment-manager |
| 11 | kuaishou-ops-assistant | 快手运营助理 | [content-ops/kuaishou](../../../content-ops/kuaishou/) | kuaishou-ops-assistant, kuaishou-hot-monitor, kuaishou-viral-breakdown, kuaishou-rewrite, kuaishou-write, kuaishou-publisher, kuaishou-data-assistant, kuaishou-comment-manager |

**说明：** B站七件套中第二个子智能体为「内容创作助手」`bilibili-content-helper`，第三个为「视频发布」`bilibili-video-publisher`，与其他渠道的「二创」「自动发布」命名不同，但职责对应。

---

## 配置示例（单 Agent 委派）

以下为单 Agent 委派的完整片段示例：全局关闭委派，仅在运营助理条目上设置 `tools.agentToAgent.enabled: true` 和 `allow` 列表。

```json
{
  "tools": {
    "profile": "full",
    "agentToAgent": {
      "enabled": false
    }
  },
  "agents": {
    "list": [
      {
        "id": "xiaohongshu-ops-assistant",
        "default": true,
        "name": "小红书运营助理",
        "workspace": "~/.openclaw/workspace-xiaohongshu-ops-assistant",
        "agentDir": "~/.openclaw/agents/xiaohongshu-ops-assistant/agent",
        "subagents": {
          "allowAgents": [
            "xiaohongshu-ops-assistant",
            "xiaohongshu-hot-monitor",
            "xiaohongshu-viral-breakdown",
            "xiaohongshu-rewrite",
            "xiaohongshu-write",
            "xiaohongshu-publisher",
            "xiaohongshu-data-assistant",
            "xiaohongshu-comment-manager"
          ]
        }
      }
    ]
  }
}
```

### 多渠道仅启用部分运营助理示例

若只启用「小红书」与「公众号」两个渠道的运营助理，其余 Agent 不配置委派：

```json
{
  "tools": {
    "profile": "full",
    "agentToAgent": { "enabled": false }
  },
  "agents": {
    "list": [
      {
        "id": "xiaohongshu-ops-assistant",
        "name": "小红书运营助理",
        "workspace": "~/.openclaw/workspace-xiaohongshu-ops-assistant",
        "agentDir": "~/.openclaw/agents/xiaohongshu-ops-assistant/agent",
        "subagents": {
          "allowAgents": [
            "xiaohongshu-ops-assistant",
            "xiaohongshu-hot-monitor",
            "xiaohongshu-viral-breakdown",
            "xiaohongshu-rewrite",
            "xiaohongshu-write",
            "xiaohongshu-publisher",
            "xiaohongshu-data-assistant",
            "xiaohongshu-comment-manager"
          ]
        }
      },
      {
        "id": "wechat-article-ops-assistant",
        "name": "公众号运营助理",
        "workspace": "~/.openclaw/workspace-wechat-article-ops-assistant",
        "agentDir": "~/.openclaw/agents/wechat-article-ops-assistant/agent",
        "subagents": {
          "allowAgents": [
            "wechat-article-ops-assistant",
            "wechat-article-hot-monitor",
            "wechat-article-viral-breakdown",
            "wechat-article-rewrite",
            "wechat-article-write",
            "wechat-article-publisher",
            "wechat-article-data-assistant",
            "wechat-article-comment-manager"
          ]
        }
      }
    ]
  }
}
```

### Workspace 与仓库路径对应

| 类型 | 路径示例 |
|------|----------|
| 运营助理 workspace | `~/.openclaw/workspace-xiaohongshu-ops-assistant` → 仓库 `company/internal/6-content-ops-assistant/xiaohongshu-ops-assistant` |
| 渠道七件套 workspace | `~/.openclaw/workspace-xiaohongshu-hot-monitor` 等 → 仓库 `content-ops/xiaohongshu/1-xiaohongshu-hot-monitor` 等 |

部署时将本仓库对应目录复制或软链到上述 workspace；各渠道七件套目录见 [config/README.md](../../../config/README.md) 片段列表与各 `content-ops/<channel>/README.md`。

---

## 相关配置片段

- **小红书单 Agent 委派示例（可直接合并）：** [config/openclaw-xiaohongshu-ops-delegation-example.json](../../../config/openclaw-xiaohongshu-ops-delegation-example.json)
- **各渠道七件套片段：** [config/README.md](../../../config/README.md) 中的 `openclaw-xiaohongshu-fragment.json`、`openclaw-wechat-article-fragment.json`、`openclaw-bilibili-fragment.json` 等。

合并时需同时包含：① 运营助理条目（含 `tools.agentToAgent`）；② 该渠道七件套的 `agents.list` 条目；③ 全局 `tools.agentToAgent.enabled: false`（或不在全局开放委派）。

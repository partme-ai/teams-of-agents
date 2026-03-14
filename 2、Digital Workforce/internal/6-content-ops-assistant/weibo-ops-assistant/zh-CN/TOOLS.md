# TOOLS.md - 本地备注

技能定义的是工具**如何**工作。本文件用于**你的**个性化配置——只属于你当前环境的内容。

## 可填写内容

- **本渠道内容运营管线路径与文档。** 便于正确协调与交接。
- 若使用，可写数据源链接、看板 URL 或格式约定。

## 本渠道管线（微博）

- **管线文档：** `content-ops/weibo/README.md` —「智能体清单」与「智能工作执行链路」列出 7 个子智能体及执行顺序。
- **子智能体目录（仓库内）：** `content-ops/weibo/1-weibo-hot-monitor` … `content-ops/weibo/7-weibo-comment-manager`。
- 部署后，工作区路径通常为 `~/.openclaw/workspace-weibo-<agentId>`（见 config 或委派片段）。

## 示例

```markdown
### 管线

- pipeline-doc → content-ops/weibo/README.md
- sub-agents → 1-hot-monitor, 2-viral-breakdown, 3-rewrite, 4-publisher, 5-data-assistant, 6-write, 7-comment-manager

### 数据（若使用）

- 报告输出路径、关键词列表、下次运行提醒
```

## 为何分开？

技能是共享的，你的环境是你自己的。分开存放便于更新技能时不丢失备注。

---

按需添加对你工作有帮助的内容。这是你的速查表。

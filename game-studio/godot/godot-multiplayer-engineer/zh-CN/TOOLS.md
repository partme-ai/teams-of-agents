# TOOLS.md - 本地备注

技能定义工具的**工作方式**，此文件记录你的**具体配置**。

## 交付物

### Server Setup (ENet)
```gdscript

## 工作流程

### 1. Architecture Planning
- Choose topology: client-server (peer 1 = dedicated/host server) or P2P (each peer is authority of their own entities)
- Define which nodes are server-owned vs. peer-owned — diagram this before coding
- Map all RPCs: who calls them, who executes them, what validation is required

### 2. Network Manager Setup
- Build the `NetworkManager` Autoload with `create_server` / `join_server` / `disconnect` functions


_[truncated]_

## 输入 / 输出路径

- **输入：** _（填写：从哪里读取来源材料、报告或任务定义）_
- **输出：** _（填写：将交付物、日志或报告写入哪里）_

## 技能

按需安装适合此智能体任务的技能：

```bash
# 示例 — 替换为 Godot 多人联网工程师 实际所需的技能 slug
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## 备注

_在此添加特定环境配置、字段约定或 API 端点。不要存储凭证。_

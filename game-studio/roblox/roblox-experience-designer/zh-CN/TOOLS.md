# TOOLS.md - 本地备注

技能定义工具的**工作方式**，此文件记录你的**具体配置**。

## 交付物

### Game Pass Purchase and Gate Pattern
```lua
-- ServerStorage/Modules/PassManager.lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local PassManager = {}

-- Centralized pass ID registry — change here, not scattered across codebase
local PASS_IDS = {
    VIP = 123456789,
    DoubleXP = 987654321,
    ExtraLives = 111222333,
}

-- Cache ownership to avoid excessive API calls


_[truncated]_

## 工作流程

### 1. Experience Brief
- Define the core fantasy: what is the player doing and why is it fun?
- Identify the target age range and Roblox genre (simulator, roleplay, obby, shooter, etc.)
- Define the three things a player will say to their friend about the experience

### 2. Engagement Loop Design
- Map the full engagement ladder: first session → daily return → weekly retention
- Design each loop tier with a clear reward at each closure


_[truncated]_

## 输入 / 输出路径

- **输入：** _（填写：从哪里读取来源材料、报告或任务定义）_
- **输出：** _（填写：将交付物、日志或报告写入哪里）_

## 技能

按需安装适合此智能体任务的技能：

```bash
# 示例 — 替换为 Roblox 体验设计师 实际所需的技能 slug
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## 备注

_在此添加特定环境配置、字段约定或 API 端点。不要存储凭证。_

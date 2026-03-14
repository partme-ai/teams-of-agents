# Spatial Computing / 空间计算

> XR interface designers and immersive runtime engineers
>
> XR 交互架构师与沉浸式运行时工程师

## Agents / 智能体列表

| ID | Name | 中文名 | Sub-scenario | Role |
|---|---|---|---|---|
| macos-spatial-metal-engineer | macOS Spatial/Metal Engineer | macOS Metal 空间工程师 | immersive-runtime | undefined |
| terminal-integration-specialist | Terminal Integration Specialist | 终端集成专家 | immersive-runtime | undefined |
| visionos-spatial-engineer | visionOS Spatial Engineer | visionOS 空间工程师 | immersive-runtime | undefined |
| xr-cockpit-interaction-specialist | XR Cockpit Interaction Specialist | XR 座舱交互专家 | xr-interface | undefined |
| xr-immersive-developer | XR Immersive Developer | XR 沉浸式开发者 | immersive-runtime | undefined |
| xr-interface-architect | XR Interface Architect | XR 交互架构师 | xr-interface | undefined |

## Structure / 目录结构

Each agent has one directory containing the OpenClaw 7-file set:

```
<agent-id>/
├── AGENTS.md      # Role, rules, session startup, memory
├── SOUL.md        # Values, beliefs, tone
├── IDENTITY.md    # Self-introduction card
├── TOOLS.md       # Deliverables, workflow, skills
├── USER.md        # About the human being served
├── HEARTBEAT.md   # Periodic tasks (empty = HEARTBEAT_OK)
├── BOOTSTRAP.md   # First-run guide (delete after setup)
└── zh-CN/         # Chinese mirror of all 7 files
```

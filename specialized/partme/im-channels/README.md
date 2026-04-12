# 1、IM Channels / 1、IM Channels

> 
>
> 

## Agents / 智能体列表

| ID | Name | 中文名 | Sub-scenario | Role |
|---|---|---|---|---|
| study-abroad-advisor | Study Abroad Advisor | 留学顾问 | education | undefined |

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

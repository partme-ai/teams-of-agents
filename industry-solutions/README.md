# Industry Solutions / 行业解决方案

> Domain specialists for government, healthcare, education, supply chain and cross-cultural contexts
>
> 政务、医疗、教育、供应链及跨文化领域专家

## Agents / 智能体列表

| ID | Name | 中文名 | Sub-scenario | Role |
|---|---|---|---|---|
| government-digital-presales-consultant | Government Digital Presales Consultant | 政务数字化售前顾问 | government | undefined |
| healthcare-marketing-compliance | Healthcare Marketing Compliance Specialist | 医疗健康营销合规专家 | healthcare | undefined |
| cultural-intelligence-strategist | Cultural Intelligence Strategist | 文化智能策略师 | cross-cultural | undefined |
| study-abroad-advisor | Study Abroad Advisor | 留学顾问 | education | undefined |
| supply-chain-strategist | Supply Chain Strategist | 供应链策略师 | supply-chain | undefined |

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

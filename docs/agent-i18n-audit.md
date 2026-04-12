# OpenClaw 智能体中英对照审计清单（7 件套）

生成时间：2026-03-15

> **路径说明（2026-04）**：本清单表格中的智能体路径为迁移前目录（`1、IM Channels` / `2、Digital Workforce` / `3、Content Ops`）。仓库已按与 `research/agency-agents` 一致的分类重组；标准角色请按 kebab-case slug 在 `engineering/`、`marketing/` 等一级目录下查找，其余见 `specialized/partme/`。批量迁移脚本：`scripts/migrate_to_agency_layout.py`。

## 标准 7 件套

| # | 文件名 | 说明 |
|---|--------|------|
| 1 | AGENTS.md | 智能体人格与工作区说明 |
| 2 | BOOTSTRAP.md | 配置/首次运行说明 |
| 3 | HEARTBEAT.md | 心跳/调度说明 |
| 4 | IDENTITY.md | 身份、名字、形态、调性、产出与边界 |
| 5 | SOUL.md | 信念、边界、沟通风格 |
| 6 | TOOLS.md | 工具与路径说明 |
| 7 | USER.md | 用户/对话对象说明 |

## 汇总统计

- **智能体总数（有 zh-CN 目录）**：338
- **AGENTS.md 缩水**（zh-CN 行数 < EN 的 50%，且 EN>20 行）：**90** 个
- **缺失 zh-CN**（仅 EN 无 zh-CN）：IDENTITY/BOOTSTRAP/HEARTBEAT/TOOLS 各 **19** 个（同一批：product/*, scrm/*, web3/*）

## 90 个 AGENTS.md 缩水智能体

| 智能体路径 | AGENTS EN:zh-CN |
|------------|-----------------|
| 1、IM Channels/feishu/feishu-integration-developer |      553:     118 |
| 2、Digital Workforce/2、Sales/1-account-strategist |      189:      48 |
| 2、Digital Workforce/2、Sales/3-sales-coach |      231:      92 |
| 2、Digital Workforce/2、Sales/6-discovery-coach |      206:      92 |
| 2、Digital Workforce/2、Sales/9-pipeline-analyst |      233:      92 |
| 2、Digital Workforce/3、Finance & Ops/2-finance-tracker |      407:      92 |
| 2、Digital Workforce/3、Finance & Ops/3-recruitment-specialist |      456:      92 |
| 2、Digital Workforce/3、Finance & Ops/5-legal-compliance-checker |      553:      92 |
| 2、Digital Workforce/3、Finance & Ops/6-support-responder |      550:      92 |
| 2、Digital Workforce/3、Finance & Ops/7-feedback-synthesizer |      112:      45 |
| 2、Digital Workforce/3、Finance & Ops/8-analytics-reporter |      330:      42 |
| 2、Digital Workforce/4、Game & Media/10-unity-editor-tool-developer |      269:      21 |
| 2、Digital Workforce/4、Game & Media/11-unity-multiplayer-engineer |      277:      21 |
| 2、Digital Workforce/4、Game & Media/12-unity-shader-graph-artist |      226:      21 |
| 2、Digital Workforce/4、Game & Media/13-unreal-multiplayer-architect |      269:      92 |
| 2、Digital Workforce/4、Game & Media/14-unreal-systems-engineer |      258:      92 |
| 2、Digital Workforce/4、Game & Media/15-unreal-technical-artist |      213:      92 |
| 2、Digital Workforce/4、Game & Media/16-unreal-world-builder |      229:      92 |
| 2、Digital Workforce/4、Game & Media/17-godot-gameplay-scripter |      272:      92 |
| 2、Digital Workforce/4、Game & Media/18-godot-multiplayer-engineer |      255:      92 |
| 2、Digital Workforce/4、Game & Media/19-godot-shader-developer |      223:      92 |
| 2、Digital Workforce/4、Game & Media/20-blender-add-on-engineer |      190:      92 |
| 2、Digital Workforce/4、Game & Media/22-studio-operations |      165:      33 |
| 2、Digital Workforce/4、Game & Media/3-narrative-designer |      200:      92 |
| 2、Digital Workforce/4、Game & Media/4-game-audio-engineer |      222:      92 |
| 2、Digital Workforce/4、Game & Media/5-technical-artist |      187:      92 |
| 2、Digital Workforce/4、Game & Media/6-roblox-avatar-creator |      254:      92 |
| 2、Digital Workforce/4、Game & Media/7-roblox-experience-designer |      263:      92 |
| 2、Digital Workforce/4、Game & Media/8-roblox-systems-scripter |      281:      92 |
| 2、Digital Workforce/4、Game & Media/9-unity-architect |      226:      21 |
| 2、Digital Workforce/5、XR & Spatial/5-macos-spatial-metal-engineer |      294:      92 |
| 2、Digital Workforce/6、Compliance & Risk/2-agentic-identity-trust-architect |      327:      49 |
| 2、Digital Workforce/6、Compliance & Risk/3-healthcare-marketing-compliance-specialist |      347:      92 |
| 2、Digital Workforce/6、Compliance & Risk/4-government-digital-presales-consultant |      317:      92 |
| 2、Digital Workforce/6、Compliance & Risk/5-blockchain-security-auditor |      418:      92 |
| 2、Digital Workforce/6、Compliance & Risk/6-threat-detection-engineer |      493:      92 |
| 2、Digital Workforce/6、Compliance & Risk/7-incident-response-commander |      384:      92 |
| 2、Digital Workforce/7、Ad & Creative/2-brand-guardian |      266:      92 |
| 2、Digital Workforce/7、Ad & Creative/3-image-prompt-engineer |      201:      92 |
| 2、Digital Workforce/8、Research & Strategy/1-trend-researcher |      152:      47 |
| 2、Digital Workforce/8、Research & Strategy/11-agents-orchestrator |      331:      10 |
| 2、Digital Workforce/8、Research & Strategy/12-identity-graph-operator |      224:      92 |
| 2、Digital Workforce/8、Research & Strategy/13-zk-steward |      164:      32 |
| 2、Digital Workforce/8、Research & Strategy/14-developer-advocate |      281:      92 |
| 2、Digital Workforce/8、Research & Strategy/17-whimsy-injector |      404:      35 |
| 2、Digital Workforce/8、Research & Strategy/18-accessibility-auditor |      274:      97 |
| 2、Digital Workforce/8、Research & Strategy/19-ai-data-remediation-engineer |      161:      46 |
| 2、Digital Workforce/8、Research & Strategy/2-model-qa-specialist |      448:      92 |
| 2、Digital Workforce/8、Research & Strategy/4-study-abroad-advisor |      240:      92 |
| 2、Digital Workforce/8、Research & Strategy/6-supply-chain-strategist |      537:      92 |
| 2、Digital Workforce/8、Research & Strategy/7-china-e-commerce-operator |      249:      92 |
| 2、Digital Workforce/8、Research & Strategy/8-cross-border-e-commerce-specialist |      209:      92 |
| 2、Digital Workforce/software-delivery/15-frontend-developer | — 已并入 10-frontend-engineer |
| 2、Digital Workforce/software-delivery/16-backend-architect |      201:      30 |
| 2、Digital Workforce/software-delivery/18-api-tester |      269:      49 |
| 2、Digital Workforce/software-delivery/20-security-engineer |      242:      92 |
| 2、Digital Workforce/software-delivery/21-devops-automator |      340:      92 |
| 2、Digital Workforce/software-delivery/23-mobile-app-builder |      458:      92 |
| 2、Digital Workforce/software-delivery/24-rapid-prototyper |      427:      92 |
| 2、Digital Workforce/software-delivery/27-technical-writer |      357:      92 |
| 2、Digital Workforce/software-delivery/29-infrastructure-maintainer |      583:      92 |
| 2、Digital Workforce/software-delivery/31-data-engineer |      270:      92 |
| 2、Digital Workforce/software-delivery/32-ai-engineer |      118:      42 |
| 2、Digital Workforce/software-delivery/33-performance-benchmarker |      232:      92 |
| 2、Digital Workforce/software-delivery/34-test-results-analyzer |      268:      92 |
| 2、Digital Workforce/software-delivery/35-tool-evaluator |      357:      92 |
| 2、Digital Workforce/software-delivery/36-evidence-collector |      189:      92 |
| 2、Digital Workforce/software-delivery/37-reality-checker |      217:      92 |
| 2、Digital Workforce/software-delivery/38-ui-designer |      348:      31 |
| 2、Digital Workforce/software-delivery/39-ux-architect |      434:      40 |
| 2、Digital Workforce/software-delivery/40-ux-researcher |      294:      31 |
| 2、Digital Workforce/software-delivery/41-jira-workflow-steward |      185:      92 |
| 2、Digital Workforce/software-delivery/46-workflow-optimizer |      413:      37 |
| 2、Digital Workforce/software-delivery/48-solidity-smart-contract-engineer |      478:      92 |
| 2、Digital Workforce/software-delivery/49-lsp-index-engineer |      273:      92 |
| 2、Digital Workforce/software-delivery/51-wechat-mini-program-developer |      316:      34 |
| 3、Content Ops/baidu/2-seo-specialist |      246:      92 |
| 3、Content Ops/baidu/baidu-seo-specialist |      192:      36 |
| 3、Content Ops/bilibili/bilibili-content-strategist |      165:      44 |
| 3、Content Ops/growth/4-short-video-editing-coach |      354:      92 |
| 3、Content Ops/growth/5-livestream-commerce-coach |      261:      92 |
| 3、Content Ops/growth/6-visual-storyteller |      121:      37 |
| 3、Content Ops/growth/7-private-domain-operator |      269:      92 |
| 3、Content Ops/growth/8-app-store-optimizer |      286:      77 |
| 3、Content Ops/kuaishou/8-kuaishou-strategist |      189:      92 |
| 3、Content Ops/podcast/1-podcast-strategist |      233:      92 |
| 3、Content Ops/tiktok/1-tiktok-strategist |      100:      39 |
| 3、Content Ops/wechat-article/8-wechat-official-account-manager |      111:      35 |
| 3、Content Ops/xiaohongshu/8-xiaohongshu-specialist |      105:      43 |
| 3、Content Ops/zhihu/zhihu-strategist |      125:      56 |

## 19 个缺失 zh-CN（IDENTITY/BOOTSTRAP/HEARTBEAT/TOOLS）

| 智能体路径 | 缺失项 |
|------------|--------|
| product/0-main | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| product/architect-advisor | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| product/business-agent | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| product/devops-agent | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| product/doc-writer | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| product/pm-assistant | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| product/report-agent | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| product/requirement-analyst | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| product/test-engineer | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| scrm/0-main | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| scrm/acquisition | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| scrm/connection | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| scrm/customer-assets | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| scrm/lead-gen | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| scrm/private-domain | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| web3/chain-analyst | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| web3/defi-scout | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| web3/portfolio-manager | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |
| web3/risk-monitor | IDENTITY BOOTSTRAP HEARTBEAT TOOLS  |

## 全量 338 智能体 × 7 件套（EN:zh-CN 行数）

| 智能体路径 | AGENTS | BOOTSTRAP | HEARTBEAT | IDENTITY | SOUL | TOOLS | USER | 问题 |
|------------|--------|-----------|-----------|----------|------|-------|------|------|
| 1、IM Channels/assistant/1-openclaw-assistant |      139:     136 |       69:      69 |        8:       8 |       85:      19 |       51:      50 |       41:      41 |       22:      22 | - |
| 1、IM Channels/discord/1-discord-mod |      127:     113 |       69:      69 |        5:       5 |       85:      19 |       51:      50 |       18:      18 |        8:      21 | - |
| 1、IM Channels/discord/2-discord-community |      127:     113 |       69:      69 |        3:       3 |       85:      19 |       51:      50 |       19:      19 |        8:      21 | - |
| 1、IM Channels/discord/3-discord-support |      127:     113 |       69:      69 |        3:       3 |       85:      19 |       51:      50 |       18:      18 |        8:      21 | - |
| 1、IM Channels/education/0-main |      123:     120 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       15:      18 |       22:      21 | - |
| 1、IM Channels/education/comment-writer |      124:     113 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       40:      18 |       22:      21 | - |
| 1、IM Channels/education/edu-assistant |      124:     113 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       40:      18 |       22:      21 | - |
| 1、IM Channels/education/parent-liaison |      124:     113 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       40:      18 |       22:      21 | - |
| 1、IM Channels/education/subject-chinese |      124:     113 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       40:      18 |       22:      21 | - |
| 1、IM Channels/education/subject-math |      124:     113 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       40:      18 |       22:      21 | - |
| 1、IM Channels/feishu/feishu-integration-developer |      553:     118 |       69:      69 |        3:       3 |        2:      19 |       40:      40 |       18:      18 |        8:      21 |  AGENTS短 |
| 1、IM Channels/partner/0-main |      123:     122 |       69:      69 |        5:       3 |       85:      19 |       51:      51 |       15:      18 |       22:      21 | - |
| 1、IM Channels/partner/companion |      124:     123 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       40:      18 |       22:      21 | - |
| 1、IM Channels/partner/growth-reporter |      139:     117 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       40:      18 |       22:      21 | - |
| 1、IM Channels/partner/reminder-scheduler |      139:     117 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       40:      18 |       22:      21 | - |
| 1、IM Channels/partner/storyteller |      139:     117 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       40:      18 |       22:      21 | - |
| 1、IM Channels/telegram/1-telegram-bot-developer |      129:     114 |       69:      69 |        3:       3 |       85:      19 |       51:      50 |       19:      19 |        8:      21 | - |
| 1、IM Channels/telegram/2-telegram-community |      127:     113 |       69:      69 |        3:       3 |       85:      19 |       51:      50 |       18:      18 |        8:      21 | - |
| 1、IM Channels/telegram/3-telegram-support |      127:     113 |       69:      69 |        3:       3 |       85:      19 |       51:      50 |       18:      18 |        8:      21 | - |
| 1、IM Channels/wecom-kf/0-main |      124:     132 |       69:      69 |        7:       3 |       85:      19 |       51:      51 |       40:      18 |       23:      21 | - |
| 1、IM Channels/wecom-kf/aftersale |      114:     118 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       27:      18 |       22:      21 | - |
| 1、IM Channels/wecom-kf/presale |      115:     119 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       28:      18 |       22:      21 | - |
| 1、IM Channels/wecom-kf/tech |      115:     119 |       69:      69 |        5:       3 |       85:      19 |       51:      50 |       33:      18 |       22:      21 | - |
| 2、Digital Workforce/1、Customer Service/6-cs-assistant |      139:     149 |       69:      69 |        8:       8 |       85:      19 |       51:      50 |       35:      35 |       28:      28 | - |
| 2、Digital Workforce/1、Customer Service/7-cs-specialist-xiaonuan |      140:     150 |       69:      69 |        8:       8 |       85:      19 |       51:      50 |       40:      40 |       23:      23 | - |
| 2、Digital Workforce/2、Sales/1-account-strategist |      189:      48 |       18:      18 |        3:       3 |        2:       3 |       32:      30 |       17:      17 |        7:       7 |  AGENTS短 |
| 2、Digital Workforce/2、Sales/10-tracking-measurement-specialist |       63:      92 |       69:      69 |        3:       3 |        2:       3 |        1:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/11-search-query-analyst |       63:      92 |       69:      69 |        3:       3 |        2:       3 |        1:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/12-paid-media-auditor |       63:      92 |       69:      69 |        3:       3 |        2:       3 |        1:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/13-paid-social-strategist |       63:      92 |       69:      69 |        3:       3 |        2:       3 |        1:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/14-ppc-campaign-strategist |       63:      92 |       69:      69 |        3:       3 |        2:       3 |        1:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/15-programmatic-display-buyer |       63:      92 |       69:      69 |        3:       3 |        2:       3 |        1:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/2-deal-strategist |      166:      92 |       69:      69 |        3:       3 |        2:       3 |        8:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/3-sales-coach |      231:      92 |       69:      69 |        3:       3 |        2:       3 |       34:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/2、Sales/4-sales-engineer |      168:      92 |       69:      69 |        3:       3 |        2:       3 |        8:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/5-sales-data-extraction-agent |       43:      92 |       69:      69 |        3:       3 |        2:       3 |       19:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/6-discovery-coach |      206:      92 |       69:      69 |        3:       3 |        2:       3 |       14:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/2、Sales/7-outbound-strategist |      182:      92 |       69:      69 |        3:       3 |        2:       3 |       14:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/8-proposal-strategist |      182:      92 |       69:      69 |        3:       3 |        2:       3 |       29:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/2、Sales/9-pipeline-analyst |      233:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/3、Finance & Ops/1-accounts-payable-agent |      154:     152 |       18:      18 |        3:       3 |        2:       2 |       26:      24 |       17:      17 |        7:       7 | - |
| 2、Digital Workforce/3、Finance & Ops/10-executive-summary-generator |      177:      92 |       69:      69 |        3:       3 |        2:       3 |       29:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/3、Finance & Ops/11-report-distribution-agent |       41:      92 |       69:      69 |        3:       3 |        2:       3 |       19:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/3、Finance & Ops/2-finance-tracker |      407:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/3、Finance & Ops/3-recruitment-specialist |      456:      92 |       69:      69 |        3:       3 |        2:       3 |       47:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/3、Finance & Ops/4-compliance-auditor |      126:      92 |       69:      69 |        3:       3 |        2:       3 |       27:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/3、Finance & Ops/5-legal-compliance-checker |      553:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/3、Finance & Ops/6-support-responder |      550:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/3、Finance & Ops/7-feedback-synthesizer |      112:      45 |       18:      18 |        3:       3 |        2:       2 |        1:       2 |       17:      17 |        7:       7 |  AGENTS短 |
| 2、Digital Workforce/3、Finance & Ops/8-analytics-reporter |      330:      42 |       18:      18 |        3:       3 |        2:       2 |       28:      26 |       17:      17 |        7:       7 |  AGENTS短 |
| 2、Digital Workforce/3、Finance & Ops/9-data-consolidation-agent |       36:      34 |       20:      20 |        3:       3 |        2:       2 |       19:      17 |       17:      17 |        7:       7 | - |
| 2、Digital Workforce/4、Game & Media/1-game-designer |      132:     101 |       69:      69 |        3:       3 |        2:       3 |       30:      35 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/4、Game & Media/10-unity-editor-tool-developer |      269:      21 |       69:      69 |        3:       3 |        2:       3 |       36:      42 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/11-unity-multiplayer-engineer |      277:      21 |       69:      69 |        3:       3 |        2:       3 |       39:      34 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/12-unity-shader-graph-artist |      226:      21 |       69:      69 |        3:       3 |        2:       3 |       38:      33 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/13-unreal-multiplayer-architect |      269:      92 |       69:      69 |        3:       3 |        2:       3 |       39:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/14-unreal-systems-engineer |      258:      92 |       69:      69 |        3:       3 |        2:       3 |       47:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/15-unreal-technical-artist |      213:      92 |       69:      69 |        3:       3 |        2:       3 |       38:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/16-unreal-world-builder |      229:      92 |       69:      69 |        3:       3 |        2:       3 |       39:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/17-godot-gameplay-scripter |      272:      92 |       69:      69 |        3:       3 |        2:       3 |       57:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/18-godot-multiplayer-engineer |      255:      92 |       69:      69 |        3:       3 |        2:       3 |       37:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/19-godot-shader-developer |      223:      92 |       69:      69 |        3:       3 |        2:       3 |       38:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/2-level-designer |      167:      92 |       69:      69 |        3:       3 |        2:       3 |       36:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/4、Game & Media/20-blender-add-on-engineer |      190:      92 |       69:      69 |        3:       3 |        2:       3 |       39:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/21-studio-producer |      168:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/4、Game & Media/22-studio-operations |      165:      33 |       69:      69 |        3:       3 |        2:       3 |       28:      31 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/3-narrative-designer |      200:      92 |       69:      69 |        3:       3 |        2:       3 |       38:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/4-game-audio-engineer |      222:      92 |       69:      69 |        3:       3 |        2:       3 |       37:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/5-technical-artist |      187:      92 |       69:      69 |        3:       3 |        2:       3 |       37:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/6-roblox-avatar-creator |      254:      92 |       69:      69 |        3:       3 |        2:       3 |       38:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/7-roblox-experience-designer |      263:      92 |       69:      69 |        3:       3 |        2:       3 |       37:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/8-roblox-systems-scripter |      281:      92 |       69:      69 |        3:       3 |        2:       3 |       39:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/4、Game & Media/9-unity-architect |      226:      21 |       69:      69 |        3:       3 |        2:       3 |       40:      46 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/5、XR & Spatial/1-xr-interface-architect |       20:      20 |       69:      69 |        3:       3 |        2:       3 |        7:       8 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/5、XR & Spatial/2-xr-immersive-developer |       20:      20 |       69:      69 |        3:       3 |        2:       3 |        7:       8 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/5、XR & Spatial/3-xr-cockpit-interaction-specialist |       20:      20 |       69:      69 |        3:       3 |        2:       3 |        7:       8 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/5、XR & Spatial/4-visionos-spatial-engineer |       48:      42 |       69:      69 |        3:       3 |        2:       3 |        1:      11 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/5、XR & Spatial/5-macos-spatial-metal-engineer |      294:      92 |       69:      69 |        3:       3 |        2:       3 |       37:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/6、Compliance & Risk/1-automation-governance-architect |      204:     202 |       18:      18 |        3:       3 |        2:       2 |        7:       5 |       17:      17 |        7:       7 | - |
| 2、Digital Workforce/6、Compliance & Risk/2-agentic-identity-trust-architect |      327:      49 |       18:      16 |        3:       3 |        2:       2 |       54:      31 |       17:      17 |        7:       7 |  AGENTS短 |
| 2、Digital Workforce/6、Compliance & Risk/3-healthcare-marketing-compliance-specialist |      347:      92 |       69:      69 |        3:       3 |        2:       3 |       43:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/6、Compliance & Risk/4-government-digital-presales-consultant |      317:      92 |       69:      69 |        3:       3 |        2:       3 |       41:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/6、Compliance & Risk/5-blockchain-security-auditor |      418:      92 |       69:      69 |        3:       3 |        2:       3 |       37:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/6、Compliance & Risk/6-threat-detection-engineer |      493:      92 |       69:      69 |        3:       3 |        2:       3 |       35:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/6、Compliance & Risk/7-incident-response-commander |      384:      92 |       69:      69 |        3:       3 |        2:       3 |       52:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/7、Ad & Creative/1-ad-creative-strategist |       63:      57 |       16:      16 |        3:       3 |        2:       2 |        1:      20 |       17:      17 |        7:       7 | - |
| 2、Digital Workforce/7、Ad & Creative/2-brand-guardian |      266:      92 |       69:      69 |        3:       3 |        2:       3 |       49:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/7、Ad & Creative/3-image-prompt-engineer |      201:      92 |       69:      69 |        3:       3 |        2:       3 |       29:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/7、Ad & Creative/4-inclusive-visuals-specialist |       48:      92 |       69:      69 |        3:       3 |        2:       3 |       18:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/8、Research & Strategy/1-trend-researcher |      152:      47 |       69:      69 |        3:       3 |        2:       3 |        1:       7 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/10-autonomous-optimization-architect |       84:      92 |       69:      69 |        3:       3 |        2:       3 |       18:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/8、Research & Strategy/11-agents-orchestrator |      331:      10 |       16:      16 |        3:       3 |        2:       2 |       28:      26 |       19:      19 |        7:       7 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/12-identity-graph-operator |      224:      92 |       69:      69 |        3:       3 |        2:       3 |       30:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/13-zk-steward |      164:      32 |       69:      69 |        3:       3 |        2:       3 |       37:      41 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/14-developer-advocate |      281:      92 |       69:      69 |        3:       3 |        2:       3 |       29:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/15-book-co-author |       82:      92 |       69:      69 |        3:       3 |        2:       3 |       23:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/8、Research & Strategy/16-corporate-training-designer |      141:      92 |       69:      69 |        3:       3 |        2:       3 |       46:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/8、Research & Strategy/17-whimsy-injector |      404:      35 |       69:      69 |        3:       3 |        2:       3 |       28:      31 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/18-accessibility-auditor |      274:      97 |       18:      16 |        3:       3 |        2:       2 |       36:      33 |       17:      17 |        7:       7 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/19-ai-data-remediation-engineer |      161:      46 |       18:      18 |        3:       3 |        2:       2 |       36:      31 |       17:      17 |        7:       7 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/2-model-qa-specialist |      448:      92 |       69:      69 |        3:       3 |        2:       3 |       33:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/3-document-generator |       30:      92 |       69:      69 |        3:       3 |        2:       3 |       20:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/8、Research & Strategy/4-study-abroad-advisor |      240:      92 |       69:      69 |        3:       3 |        2:       3 |       37:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/5-cultural-intelligence-strategist |       64:      92 |       69:      69 |        3:       3 |        2:       3 |       19:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/8、Research & Strategy/6-supply-chain-strategist |      537:      92 |       69:      69 |        3:       3 |        2:       3 |       38:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/7-china-e-commerce-operator |      249:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/8-cross-border-e-commerce-specialist |      209:      92 |       69:      69 |        3:       3 |        2:       3 |       45:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/8、Research & Strategy/9-behavioral-nudge-engine |       57:      92 |       69:      69 |        3:       3 |        2:       3 |       18:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/internal/1-admin-assistant |      188:     188 |       69:      69 |        8:       8 |       85:      19 |       51:      50 |       40:      40 |       22:      22 | - |
| 2、Digital Workforce/internal/2-ops-assistant |      143:     153 |       69:      69 |        8:      19 |       85:      19 |       51:      50 |       34:      80 |       21:      21 | - |
| 2、Digital Workforce/internal/3-business-assistant |      139:     149 |       69:      69 |        8:      19 |       85:      19 |       51:      50 |       35:      35 |       21:      21 | - |
| 2、Digital Workforce/internal/4-boss-assistant |      138:     151 |       69:      69 |        8:      19 |       85:      19 |       51:      50 |       39:      39 |       21:      21 | - |
| 2、Digital Workforce/internal/5-boss-wife-assistant |      139:     149 |       69:      69 |        8:      19 |       85:      19 |       51:      51 |       34:      34 |       21:      21 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/baijiahao-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/bilibili-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/douyin-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/juejin-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/kuaishou-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/toutiao-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/wechat-article-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/wechat-video-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/weibo-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/xiaohongshu-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/internal/6-content-ops-assistant/zhihu-ops-assistant |      141:     152 |       70:      70 |        8:      19 |       12:      19 |       51:      47 |       35:      35 |       20:      20 | - |
| 2、Digital Workforce/software-delivery/0-main |      123:     115 |       43:       9 |        5:       5 |       85:      19 |       51:      50 |       40:      15 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/1-technical-director |      263:     134 |       69:      17 |        5:       5 |       19:      19 |       51:      53 |       40:      22 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/10-frontend-engineer |      118:     140 |       43:      10 |        5:       6 |       85:      19 |       51:      51 |       84:      84 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/11-mobile-engineer |      138:     126 |       69:      10 |        5:       6 |       85:      19 |       51:      51 |       20:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/12-qa-engineer |      129:     117 |       69:      10 |        5:       6 |       85:      19 |       51:      51 |       20:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/13-ops-engineer |      126:     148 |       69:      10 |        5:       6 |       85:      19 |       51:      51 |       20:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/14-data-analyst |      134:     124 |       69:      10 |        5:       6 |       85:      19 |       51:      51 |       20:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/15-frontend-developer | — | — | — | — | — | — | — | **已并入** `10-frontend-engineer`；独立目录已移除；下列为历史快照 |
| 2、Digital Workforce/software-delivery/16-backend-architect |      201:      30 |       18:      18 |       14:      14 |        2:       2 |       28:      26 |       21:      21 |       18:      18 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/17-code-reviewer |       50:      29 |       18:      16 |        3:       3 |        2:       3 |       21:      22 |       17:      17 |        7:       7 | - |
| 2、Digital Workforce/software-delivery/18-api-tester |      269:      49 |       18:      18 |        3:       3 |        2:       2 |       30:      28 |       17:      17 |        7:       7 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/19-database-optimizer | — | — | — | — | — | — | — | **已并入** `9-database-engineer`（能力合并，独立目录已移除）；下列行数为历史快照，勿再跑数 |
| 2、Digital Workforce/software-delivery/2-project-manager |      125:     126 |       69:       9 |        5:       5 |       85:      19 |       51:      53 |       40:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/20-security-engineer |      242:      92 |       69:      69 |        3:       3 |        2:       3 |       29:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/21-devops-automator |      340:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/22-sre-site-reliability-engineer |       65:      92 |       69:      69 |        3:       3 |        2:       3 |       20:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/software-delivery/23-mobile-app-builder |      458:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/24-rapid-prototyper |      427:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/25-senior-developer |      141:      92 |       69:      69 |        3:       3 |        2:       3 |       29:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/software-delivery/26-software-architect |       56:      92 |       69:      69 |        3:       3 |        2:       3 |       20:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/software-delivery/27-technical-writer |      357:      92 |       69:      69 |        3:       3 |        2:       3 |       29:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/28-git-workflow-master |       59:      92 |       69:      69 |        3:       3 |        2:       3 |       20:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/software-delivery/29-infrastructure-maintainer |      583:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/3-product-manager |      124:     125 |       69:      10 |        5:       6 |       85:      19 |       51:      53 |       40:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/30-mcp-builder |       37:      29 |       18:      16 |        3:       3 |        2:       3 |       21:      22 |       17:      17 |        7:       7 | - |
| 2、Digital Workforce/software-delivery/31-data-engineer |      270:      92 |       69:      69 |        3:       3 |        2:       3 |       30:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/32-ai-engineer |      118:      42 |       18:      18 |        3:       3 |        2:       3 |       22:      20 |       17:      17 |        7:       7 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/33-performance-benchmarker |      232:      92 |       69:      69 |        3:       3 |        2:       3 |       29:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/34-test-results-analyzer |      268:      92 |       69:      69 |        3:       3 |        2:       3 |       30:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/35-tool-evaluator |      357:      92 |       69:      69 |        3:       3 |        2:       3 |       30:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/36-evidence-collector |      189:      92 |       69:      69 |        3:       3 |        2:       3 |       14:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/37-reality-checker |      217:      92 |       69:      69 |        3:       3 |        2:       3 |       14:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/38-ui-designer |      348:      31 |       69:      69 |        3:       3 |        2:       3 |       28:      31 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/39-ux-architect |      434:      40 |       69:      69 |        3:       3 |        2:       3 |       28:      31 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/4-system-architect |      165:     165 |       69:      10 |        5:       6 |       85:      19 |       51:      53 |       34:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/40-ux-researcher |      294:      31 |       69:      69 |        3:       3 |        2:       3 |       28:      31 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/41-jira-workflow-steward |      185:      92 |       69:      69 |        3:       3 |        2:       3 |       39:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/42-sprint-prioritizer |      133:      92 |       69:      69 |        3:       3 |        2:       3 |       15:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/software-delivery/43-project-shepherd |      159:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/software-delivery/44-senior-project-manager |      100:      92 |       69:      69 |        3:       3 |        2:       3 |       29:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/software-delivery/45-experiment-tracker |      161:      92 |       69:      69 |        3:       3 |        2:       3 |       30:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/software-delivery/46-workflow-optimizer |      413:      37 |       69:      69 |        3:       3 |        2:       3 |       30:      33 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/47-embedded-firmware-engineer |      134:      92 |       69:      69 |        3:       3 |        2:       3 |       34:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/software-delivery/48-solidity-smart-contract-engineer |      478:      92 |       69:      69 |        3:       3 |        2:       3 |       38:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/49-lsp-index-engineer |      273:      92 |       69:      69 |        3:       3 |        2:       3 |       35:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/5-domain-expert |      165:     165 |       69:      10 |        5:       6 |       85:      19 |       51:      53 |       33:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/50-terminal-integration-specialist |       64:      92 |       69:      69 |        3:       3 |        2:       3 |        1:      36 |       18:      18 |        8:      20 | - |
| 2、Digital Workforce/software-delivery/51-wechat-mini-program-developer |      316:      34 |       69:      69 |        3:       3 |        2:       3 |       28:      31 |       18:      18 |        8:      20 |  AGENTS短 |
| 2、Digital Workforce/software-delivery/6-ux-designer |      165:     165 |       69:      10 |        5:       6 |       85:      19 |       51:      53 |       34:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/7-ui-designer |      166:     166 |       69:      10 |        5:       6 |       85:      19 |       51:      53 |       35:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/8-backend-engineer |      147:     133 |       69:      10 |        5:       6 |       85:      19 |       51:      52 |       41:       3 |       22:      21 | - |
| 2、Digital Workforce/software-delivery/9-database-engineer |      118:     138 |       69:      10 |        5:       6 |       85:      19 |       51:      51 |       23:       3 |       22:      21 | - |
| 3、Content Ops/baidu/2-seo-specialist |      246:      92 |       69:      69 |        3:       3 |        2:       3 |       27:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 3、Content Ops/baidu/baidu-seo-specialist |      192:      36 |       69:      69 |        3:       3 |        2:      19 |       28:      31 |       18:      18 |        8:      21 |  AGENTS短 |
| 3、Content Ops/baijiahao/1-baijiahao-hot-monitor |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       5 |        8:      21 | - |
| 3、Content Ops/baijiahao/2-baijiahao-viral-breakdown |      113:     115 |       69:      69 |        2:       2 |       19:      19 |       50:      50 |        2:       2 |        8:      21 | - |
| 3、Content Ops/baijiahao/3-baijiahao-rewrite |      114:     114 |       69:      69 |        2:       2 |       19:      19 |       50:      50 |        2:       2 |        8:      21 | - |
| 3、Content Ops/baijiahao/4-baijiahao-write |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       4 |        8:      21 | - |
| 3、Content Ops/baijiahao/5-baijiahao-publisher |      113:     113 |       69:      69 |        2:       2 |       19:      19 |       49:      49 |        2:       2 |        8:      21 | - |
| 3、Content Ops/baijiahao/6-baijiahao-data-assistant |      114:     114 |       69:      69 |        2:       2 |       19:      19 |       50:      50 |        2:       2 |        8:      21 | - |
| 3、Content Ops/baijiahao/7-baijiahao-comment-manager |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       4 |        8:      21 | - |
| 3、Content Ops/bilibili/1-bilibili-hot-monitor |      113:     115 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       17:      17 |        8:      21 | - |
| 3、Content Ops/bilibili/2-bilibili-content-helper |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       5 |        8:      21 | - |
| 3、Content Ops/bilibili/3-bilibili-video-publisher |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        6:       6 |        8:      21 | - |
| 3、Content Ops/bilibili/4-bilibili-data-assistant |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       5 |        8:      21 | - |
| 3、Content Ops/bilibili/5-bilibili-viral-breakdown |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       3 |        8:      21 | - |
| 3、Content Ops/bilibili/6-bilibili-write |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       3 |        8:      21 | - |
| 3、Content Ops/bilibili/7-bilibili-comment-manager |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       4 |        8:      21 | - |
| 3、Content Ops/bilibili/8-carousel-growth-engine |      154:      85 |       19:      19 |        3:       3 |        2:       2 |       33:      31 |       18:      18 |       12:      12 | - |
| 3、Content Ops/bilibili/bilibili-content-strategist |      165:      44 |       69:      69 |        3:       3 |        2:      19 |       28:      31 |       18:      18 |        8:      21 |  AGENTS短 |
| 3、Content Ops/douyin/1-douyin-hot-monitor |      113:     115 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       5 |        8:      21 | - |
| 3、Content Ops/douyin/2-douyin-viral-breakdown |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       26:       4 |        8:      21 | - |
| 3、Content Ops/douyin/3-douyin-rewrite |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       4 |        8:      21 | - |
| 3、Content Ops/douyin/4-douyin-publisher |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/douyin/5-douyin-data-assistant |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/douyin/6-douyin-write |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       5 |        8:      21 | - |
| 3、Content Ops/douyin/7-douyin-comment-manager |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       7 |        8:      21 | - |
| 3、Content Ops/douyin/8-douyin-strategist |      116:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 | - |
| 3、Content Ops/growth/1-growth-hacker |       47:      92 |       69:      69 |        3:       3 |        2:       3 |        1:      36 |       18:      18 |        8:      20 | - |
| 3、Content Ops/growth/2-content-creator |       47:      51 |       69:      69 |        3:       3 |        2:       3 |        1:      50 |       18:      18 |        8:      20 | - |
| 3、Content Ops/growth/3-social-media-strategist |      112:      92 |       69:      69 |        3:       3 |        2:       3 |        7:      36 |       18:      18 |        8:      20 | - |
| 3、Content Ops/growth/4-short-video-editing-coach |      354:      92 |       69:      69 |        3:       3 |        2:       3 |       53:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 3、Content Ops/growth/5-livestream-commerce-coach |      261:      92 |       69:      69 |        3:       3 |        2:       3 |       39:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 3、Content Ops/growth/6-visual-storyteller |      121:      37 |       69:      69 |        3:       3 |        2:       3 |       22:      24 |       18:      18 |        8:      20 |  AGENTS短 |
| 3、Content Ops/growth/7-private-domain-operator |      269:      92 |       69:      69 |        3:       3 |        2:       3 |       34:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 3、Content Ops/growth/8-app-store-optimizer |      286:      77 |       18:      16 |        3:       3 |        2:       2 |       28:      26 |       17:      17 |        7:       7 |  AGENTS短 |
| 3、Content Ops/instagram/1-instagram-curator |       88:      92 |       69:      69 |        3:       3 |        2:       3 |       20:      36 |       18:      18 |        8:      20 | - |
| 3、Content Ops/juejin/1-juejin-hot-monitor |      113:     110 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       5 |        8:      21 | - |
| 3、Content Ops/juejin/2-juejin-viral-breakdown |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       26:      26 |        8:      21 | - |
| 3、Content Ops/juejin/3-juejin-rewrite |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       3 |        8:      21 | - |
| 3、Content Ops/juejin/4-juejin-publisher |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       3 |        8:      21 | - |
| 3、Content Ops/juejin/5-juejin-data-assistant |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/juejin/6-juejin-write |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       4 |        8:      21 | - |
| 3、Content Ops/juejin/7-juejin-comment-manager |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       7 |        8:      21 | - |
| 3、Content Ops/kuaishou/1-kuaishou-hot-monitor |      113:     110 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       5 |        8:      21 | - |
| 3、Content Ops/kuaishou/2-kuaishou-viral-breakdown |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       26:       5 |        8:      21 | - |
| 3、Content Ops/kuaishou/3-kuaishou-rewrite |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       4 |        8:      21 | - |
| 3、Content Ops/kuaishou/4-kuaishou-publisher |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       4 |        8:      21 | - |
| 3、Content Ops/kuaishou/5-kuaishou-data-assistant |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/kuaishou/6-kuaishou-write |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/kuaishou/7-kuaishou-comment-manager |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/kuaishou/8-kuaishou-strategist |      189:      92 |       69:      69 |        3:       3 |        2:       3 |       28:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 3、Content Ops/linkedin/1-linkedin-content-creator |      174:      92 |       69:      69 |        3:       3 |        2:       3 |       34:      36 |       18:      18 |        8:      20 | - |
| 3、Content Ops/podcast/1-podcast-strategist |      233:      92 |       69:      69 |        3:       3 |        2:       3 |       39:      36 |       18:      18 |        8:      20 |  AGENTS短 |
| 3、Content Ops/reddit/1-reddit-community-builder |       98:      92 |       69:      69 |        3:       3 |        2:       3 |       20:      36 |       18:      18 |        8:      20 | - |
| 3、Content Ops/tiktok/1-tiktok-strategist |      100:      39 |       69:      69 |        3:       3 |        2:       3 |       20:      23 |       18:      18 |        8:      20 |  AGENTS短 |
| 3、Content Ops/toutiao/1-toutiao-hot-monitor |      113:     110 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       5 |        8:      21 | - |
| 3、Content Ops/toutiao/2-toutiao-viral-breakdown |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       26:       4 |        8:      21 | - |
| 3、Content Ops/toutiao/3-toutiao-rewrite |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       4 |        8:      21 | - |
| 3、Content Ops/toutiao/4-toutiao-publisher |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/toutiao/5-toutiao-data-assistant |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/toutiao/6-toutiao-write |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/toutiao/7-toutiao-comment-manager |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/twitter/1-twitter-engager |      101:     116 | 0:      69 | 0:       3 |        2:       3 |       20:      23 | 0:      18 | 0:      20 | - |
| 3、Content Ops/wechat-article/1-wechat-article-hot-monitor |      113:     110 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       18:      18 |        8:      21 | - |
| 3、Content Ops/wechat-article/2-wechat-article-viral-breakdown |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       29:      29 |        8:      21 | - |
| 3、Content Ops/wechat-article/3-wechat-article-rewrite |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       18:      18 |        8:      21 | - |
| 3、Content Ops/wechat-article/4-wechat-article-write |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       4 |        8:      21 | - |
| 3、Content Ops/wechat-article/5-wechat-article-publisher |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       49:      49 |       28:      28 |        8:      21 | - |
| 3、Content Ops/wechat-article/6-wechat-article-data-assistant |      112:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       29:      29 |        8:      21 | - |
| 3、Content Ops/wechat-article/7-wechat-article-comment-manager |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       7 |        8:      21 | - |
| 3、Content Ops/wechat-article/8-wechat-official-account-manager |      111:      35 |       69:      69 |        3:       3 |        2:       3 |       29:      33 |       18:      18 |        8:      20 |  AGENTS短 |
| 3、Content Ops/wechat-video/1-wechat-video-hot-monitor |      113:     115 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       5 |        8:      21 | - |
| 3、Content Ops/wechat-video/2-wechat-video-viral-breakdown |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       26:      26 |        8:      21 | - |
| 3、Content Ops/wechat-video/3-wechat-video-rewrite |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       5 |        8:      21 | - |
| 3、Content Ops/wechat-video/4-wechat-video-publisher |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/wechat-video/5-wechat-video-data-assistant |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       4 |        8:      21 | - |
| 3、Content Ops/wechat-video/6-wechat-video-write |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       5 |        8:      21 | - |
| 3、Content Ops/wechat-video/7-wechat-video-comment-manager |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       5 |        8:      21 | - |
| 3、Content Ops/weibo/1-weibo-hot-monitor |      113:     110 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       5 |        8:      21 | - |
| 3、Content Ops/weibo/2-weibo-viral-breakdown |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       26:      26 |        8:      21 | - |
| 3、Content Ops/weibo/3-weibo-rewrite |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       3 |        8:      21 | - |
| 3、Content Ops/weibo/4-weibo-publisher |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       3 |        8:      21 | - |
| 3、Content Ops/weibo/5-weibo-data-assistant |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        4:       3 |        8:      21 | - |
| 3、Content Ops/weibo/6-weibo-write |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       4 |        8:      21 | - |
| 3、Content Ops/weibo/7-weibo-comment-manager |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       4 |        8:      21 | - |
| 3、Content Ops/weibo/8-weibo-strategist |      197:     125 |       69:      66 |        3:       3 |        2:       3 |       38:      36 |       18:      18 |        7:      12 | - |
| 3、Content Ops/xiaohongshu/1-xiaohongshu-hot-monitor |      113:     110 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       18:      18 |        8:      21 | - |
| 3、Content Ops/xiaohongshu/2-xiaohongshu-viral-breakdown |      114:     114 |       69:      69 |        6:       6 |       19:      19 |       50:      50 |       22:      22 |       21:      21 | - |
| 3、Content Ops/xiaohongshu/3-xiaohongshu-rewrite |      113:     113 |       69:      69 |        5:       5 |       19:      19 |       50:      50 |       23:      23 |       21:      21 | - |
| 3、Content Ops/xiaohongshu/4-xiaohongshu-write |      113:     113 |       69:      69 |        2:       2 |       19:      19 |       50:      50 |        5:       3 |        8:      21 | - |
| 3、Content Ops/xiaohongshu/5-xiaohongshu-publisher |      109:     109 |       69:      69 |        5:       5 |       19:      19 |       47:      47 |       21:      21 |       21:      21 | - |
| 3、Content Ops/xiaohongshu/6-xiaohongshu-data-assistant |      113:     113 |       69:      69 |        5:       5 |       19:      19 |       50:      50 |       22:      22 |       21:      21 | - |
| 3、Content Ops/xiaohongshu/7-xiaohongshu-comment-manager |      113:     113 |       69:      69 |        2:       2 |       19:      19 |       50:      50 |        6:       6 |        8:      21 | - |
| 3、Content Ops/xiaohongshu/8-xiaohongshu-specialist |      105:      43 |       69:      69 |        3:       3 |        2:       3 |       28:      32 |       18:      18 |        8:      20 |  AGENTS短 |
| 3、Content Ops/zhihu/1-zhihu-hot-monitor |      113:     110 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       5 |        8:      21 | - |
| 3、Content Ops/zhihu/2-zhihu-viral-breakdown |      114:     114 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |       27:      27 |        8:      21 | - |
| 3、Content Ops/zhihu/3-zhihu-rewrite |      113:     113 |       69:      69 |        2:       2 |       19:      19 |       50:      50 |        4:       2 |        8:      21 | - |
| 3、Content Ops/zhihu/4-zhihu-write |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        5:       4 |        8:      21 | - |
| 3、Content Ops/zhihu/5-zhihu-publisher |      114:     114 |       69:      69 |        2:       2 |       19:      19 |       49:      49 |        3:       2 |        8:      21 | - |
| 3、Content Ops/zhihu/6-zhihu-data-assistant |      112:     113 |       69:      69 |        2:       2 |       19:      19 |       50:      50 |        3:       2 |        8:      21 | - |
| 3、Content Ops/zhihu/7-zhihu-comment-manager |      113:     113 |       69:      69 |        3:       3 |       19:      19 |       50:      50 |        7:       4 |        8:      21 | - |
| 3、Content Ops/zhihu/zhihu-strategist |      125:      56 |       69:      69 |        3:       3 |        2:      19 |       32:      36 |       18:      18 |        8:      21 |  AGENTS短 |
| docs/template-agent |      231:     230 |       26:      26 |        5:      25 |       31:      31 |       36:      50 |       40:      40 |       22:      22 | - |
| game-studio/art-tech-audio/game-audio-engineer |      117:      89 |       64:      64 |        7:       7 |       77:       3 |       57:      49 |       46:      41 |       21:      21 | - |
| game-studio/art-tech-audio/technical-artist |      116:      87 |       64:      64 |        7:       7 |       77:       3 |       57:      49 |       46:      41 |       21:      21 | - |
| game-studio/game-design/game-designer |      119:      90 |       64:      64 |        7:       7 |       78:       3 |       57:      49 |       46:      43 |       21:      21 | - |
| game-studio/game-design/level-designer |      120:      88 |       64:      64 |        7:       7 |       77:       3 |       57:      49 |       49:      44 |       21:      21 | - |
| game-studio/game-design/narrative-designer |      115:      88 |       64:      64 |        7:       7 |       88:       3 |       57:      49 |       62:      54 |       21:      21 | - |
| game-studio/game-tools/blender-addon-engineer |      113:      88 |       64:      64 |        7:       7 |       91:       3 |       57:      49 |       66:      60 |       21:      21 | - |
| game-studio/godot/godot-gameplay-scripter |      115:      89 |       64:      64 |        7:       7 |       79:       3 |       57:      49 |       48:      45 |       21:      21 | - |
| game-studio/godot/godot-multiplayer-engineer |      116:      88 |       64:      64 |        7:       7 |       77:       3 |       57:      49 |       45:      40 |       21:      21 | - |
| game-studio/godot/godot-shader-developer |      113:      88 |       64:      64 |        7:       7 |       91:       3 |       57:      49 |       61:      55 |       21:      21 | - |
| game-studio/roblox/roblox-avatar-creator |      117:      90 |       64:      64 |        7:       7 |       77:       3 |       57:      49 |       47:      43 |       21:      21 | - |
| game-studio/roblox/roblox-experience-designer |      114:      87 |       64:      64 |        7:       7 |       93:       3 |       57:      49 |       66:      58 |       21:      21 | - |
| game-studio/roblox/roblox-systems-scripter |      116:      91 |       64:      64 |        7:       7 |       88:       3 |       57:      49 |       58:      52 |       21:      21 | - |
| game-studio/unity/unity-architect |      114:      88 |       64:      64 |        7:       7 |      102:       3 |       56:      48 |       74:      63 |       21:      21 | - |
| game-studio/unity/unity-editor-tool-developer |      115:      89 |       64:      64 |        7:       7 |       91:       3 |       57:      49 |       65:      56 |       21:      21 | - |
| game-studio/unity/unity-multiplayer-engineer |      118:      90 |       64:      64 |        7:       7 |       89:       3 |       57:      49 |       66:      58 |       21:      21 | - |
| game-studio/unity/unity-shader-graph-artist |      117:      90 |       64:      64 |        7:       7 |       88:       3 |       57:      49 |       62:      55 |       21:      21 | - |
| game-studio/unreal/unreal-multiplayer-architect |      114:      88 |       64:      64 |        7:       7 |       92:       3 |       57:      49 |       70:      60 |       21:      21 | - |
| game-studio/unreal/unreal-systems-engineer |      115:      89 |       64:      64 |        7:       7 |       90:       3 |       49:      41 |       63:      56 |       21:      21 | - |
| game-studio/unreal/unreal-technical-artist |      117:      88 |       64:      64 |        7:       7 |       88:       3 |       57:      49 |       63:      54 |       21:      21 | - |
| game-studio/unreal/unreal-world-builder |      114:      86 |       64:      64 |        7:       7 |       77:       3 |       57:      49 |       47:      43 |       21:      21 | - |
| game/0-main |      213:     213 |       69:      69 |        5:       5 |       85:      19 |       51:      53 |       43:      43 |       29:      29 | - |
| game/1-game-master |      171:     171 |       69:      69 |        5:       5 |       85:      19 |       51:      51 |       35:      35 |       22:      22 | - |
| game/2-game-designer |      113:     113 |       69:      69 |        5:       5 |       85:       3 |       51:      51 |       33:      33 |       22:      22 | - |
| game/3-game-architect |      113:     154 |       69:      69 |        5:       5 |       85:      19 |       51:      51 |       32:      32 |       22:      22 | - |
| game/4-game-developer |      138:     148 |       69:      69 |        5:       5 |       85:      19 |       51:      51 |       35:      35 |       22:      22 | - |
| game/5-game-ops |      139:     149 |       69:      69 |        5:       5 |       85:      19 |       51:      51 |       35:      35 |       22:      22 | - |
| industry-solutions/cross-cultural/cultural-intelligence-strategist |      106:      85 |       64:      64 |        7:       7 |       87:       3 |       52:      45 |       50:      47 |       21:      21 | - |
| industry-solutions/education/study-abroad-advisor |      117:      89 |       64:      64 |        7:       7 |       78:       3 |       57:      49 |       44:      41 |       21:      21 | - |
| industry-solutions/government/government-digital-presales-consultant |      116:      91 |       64:      64 |        7:       7 |       78:       3 |       56:      49 |       45:      39 |       21:      21 | - |
| industry-solutions/healthcare/healthcare-marketing-compliance |      114:      89 |       64:      64 |        7:       7 |       76:       3 |       56:      49 |       43:      37 |       21:      21 | - |
| industry-solutions/supply-chain/supply-chain-strategist |      115:      90 |       64:      64 |        7:       7 |       77:       3 |       57:      49 |       34:      32 |       21:      21 | - |
| product/0-main |      124:     125 |       69:0 |        5:0 |       85:0 |       51:      51 |       15:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| product/architect-advisor |      124:     113 |       69:0 |        5:0 |       85:0 |       51:      50 |       15:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| product/business-agent |      123:     113 |       69:0 |        5:0 |       85:0 |       51:      50 |       40:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| product/devops-agent |      123:     113 |       69:0 |        5:0 |       85:0 |       51:      50 |       40:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| product/doc-writer |      123:     113 |       69:0 |        5:0 |       85:0 |       51:      50 |       40:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| product/pm-assistant |      135:     113 |       69:0 |        5:0 |       85:0 |       51:      50 |       15:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| product/report-agent |      123:     113 |       69:0 |        5:0 |       85:0 |       51:      50 |       40:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| product/requirement-analyst |      123:     113 |       69:0 |        5:0 |       85:0 |       51:      50 |       40:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| product/test-engineer |      123:     113 |       69:0 |        5:0 |       85:0 |       51:      50 |       40:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| scrm/0-main |      134:     135 |       69:0 |        5:0 |       85:0 |       51:      51 |       40:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| scrm/acquisition |      139:     117 |       69:0 |        5:0 |       85:0 |       51:      50 |       15:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| scrm/connection |      139:     117 |       69:0 |        5:0 |       85:0 |       51:      50 |       15:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| scrm/cs-specialist-xiaonuan |      104:     104 |       53:      53 |        8:       8 |       78:      19 |       48:      48 |       57:      56 |       21:      21 | - |
| scrm/customer-assets |      139:     117 |       69:0 |        5:0 |       85:0 |       51:      50 |       15:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| scrm/lead-gen |      139:     117 |       69:0 |        5:0 |       85:0 |       51:      50 |       15:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| scrm/private-domain |      139:     117 |       69:0 |        5:0 |       85:0 |       51:      50 |       15:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| spatial-computing/immersive-runtime/macos-spatial-metal-engineer |      118:      97 |       64:      64 |        7:       7 |       89:       3 |       58:      49 |       54:      51 |       21:      21 | - |
| spatial-computing/immersive-runtime/terminal-integration-specialist |       88:      79 |       64:      64 |        7:       7 |       72:       3 |       50:      49 |       32:      30 |       21:      21 | - |
| spatial-computing/immersive-runtime/visionos-spatial-engineer |       88:      79 |       64:      64 |        7:       7 |       72:       3 |       50:      49 |       32:      30 |       21:      21 | - |
| spatial-computing/immersive-runtime/xr-immersive-developer |       98:      84 |       64:      64 |        7:       7 |       77:       3 |       57:      49 |       32:      30 |       21:      21 | - |
| spatial-computing/xr-interface/xr-cockpit-interaction-specialist |       98:      84 |       64:      64 |        7:       7 |       77:       3 |       58:      49 |       32:      30 |       21:      21 | - |
| spatial-computing/xr-interface/xr-interface-architect |       98:      84 |       64:      64 |        7:       7 |       75:       3 |       58:      49 |       32:      30 |       21:      21 | - |
| web3/chain-analyst |      241:     159 |       69:0 |       17:0 |       85:0 |       51:      51 |       41:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| web3/defi-scout |      116:     115 |       69:0 |        5:0 |       85:0 |       51:      50 |       20:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| web3/portfolio-manager |      126:     114 |       69:0 |        5:0 |       85:0 |       51:      50 |       20:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| web3/protocol-engineering/solidity-smart-contract-engineer |      119:      91 |       64:      64 |        7:       7 |       87:       3 |       57:      49 |       56:      50 |       21:      21 | - |
| web3/protocol-security/blockchain-security-auditor |      114:      89 |       64:      64 |        7:       7 |       89:       3 |       57:      49 |       63:      53 |       21:      21 | - |
| web3/risk-monitor |      126:     114 |       69:0 |       15:0 |       85:0 |       51:      50 |       21:0 |       22:      21 |  缺IDENTITY 缺BOOT 缺HEART 缺TOOLS |
| web3/zero-knowledge/zk-steward |      123:      95 |       64:      64 |        7:       7 |       85:      19 |       56:      49 |       57:      54 |       21:      21 | - |

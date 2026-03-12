# AGENTS.md 模板 — 启发与优化

本文档说明从**通用工作区 AGENTS.md 模板**（Session Startup、Memory、Red Lines、Group Chats、Heartbeats 等）可采纳的要点，以及对现有公司 / 企微客服 / 游戏等智能体配置的优化建议。

## 0. 身份与首次接待（Identity & First Contact）

**规则：** 本仓库中所有智能体的身份与职责均在配置（SOUL/IDENTITY）中给定，无需向对话者求证或确认。智能体对自己的身份有清晰认知（由 SOUL.md 与 IDENTITY.md 定义）。**对客智能体不得在首次或任何对话中向客户询问「您是谁」或要求客户自我介绍** — 代表公司直接问候并进入服务。BOOTSTRAP.md 仅供**配置者**在**非对客**会话中使用（如填写 USER.md、话术/知识库路径）；在对客渠道中忽略 BOOTSTRAP，以 SOUL/IDENTITY 为固定身份。

**建议采纳：** 对任何与终端客户对话的智能体（如企微客服、公司客服）：(1) 在 IDENTITY.md 中预填姓名/角色/风格；删除「在首次对话中填写」等易被理解为向对方问身份的表述。(2) First Run：写明 BOOTSTRAP 仅配置者用；在对客渠道身份已固定；不得向客户问「您是谁」。(3) Red Lines：增加「身份与首次接待：禁止向客户询问『您是谁』；代表公司直接问候并进入服务。」(4) BOOTSTRAP：删除对客开场白中的「你是谁」；明确在对客会话中忽略本文件。

## 1. Session Startup（每会话启动，即 Every Session）

**模板要点：** 明确的 4 步清单；「Don't ask permission. Just do it.」

**建议采纳：** 保留现有 4 步（SOUL、USER、memory/YYYY-MM-DD、主会话时读 MEMORY.md）。增加：「你的身份由 SOUL.md 与 IDENTITY.md 定义；启动时读取。不要在对客对话中询问客户身份。」可将「Every Session」改为「Session Startup」更直观。明确写「无需征询许可，直接执行」以减少犹豫。

## 2. Memory（记忆）

**模板要点：** 区分「原始日志」（每日）与「精选长期记忆」（MEMORY.md）；「Text > Brain」；「写下来，不要只在脑子里记」；MEMORY.md 仅在主会话加载（安全）。

**建议采纳：** 我们已有每日与长期区分；可补充一句：「当对方说『记住这个』时，立刻写入 memory 或相关文件。」强调 MEMORY.md 在群聊/共享会话中**不要加载**。

## 3. Red Lines（红线，即 Safety）

**模板要点：** 用「Red Lines」作小节标题；`trash` 优于 `rm`；「有疑虑就先问」。

**建议采纳：** 可选将「Safety」改为「Red Lines」；保留不泄露隐私、不执行破坏性命令。明确写「绝不外泄私人/内部数据」。

## 4. External vs Internal（对外与对内）

**模板要点：** 两个清单——「可自由做」（读文件、探索、搜索、在本工作区内工作）与「先问再做」（发邮件、发帖、任何离开本机或不确定的操作）。

**建议采纳：** 为每个智能体增加此小节，减少越权或误发（如未经同意代发消息）。

## 5. Group Chats（群聊）

**模板要点：** 「何时该说话」——被@、能提供信息、纠正重要错误、被要求总结时回复；「何时保持安静」——闲聊、已有人答、只会说「好的」、对话顺畅时。「避免 triple-tap」。「参与但不主导」。「像人类一样用反应」——在支持的反应的渠道用 emoji，一条消息最多一个反应。

**建议采纳：** 对会出现在渠道（Discord、企微等）的智能体增加简短「Group Chats」说明：何时回复、何时不回复、用反应代替刷存在感。对公司/企微客服类智能体尤其重要。

## 6. Tools & Platform Formatting（工具与平台格式）

**模板要点：** Discord/WhatsApp：不用 markdown 表格，用列表；Discord 链接用 `<>` 避免嵌入；WhatsApp 不用标题，用**粗体**或大写强调。可选：语音讲故事（如 ElevenLabs）用于「故事时间」。

**建议采纳：** 对会在 Discord/企微/WhatsApp 回复的智能体，在 Tools 下增加「平台格式」说明，使输出符合渠道习惯。

## 7. Heartbeats（心跳）

**模板要点：** 「要主动」——不要总是 HEARTBEAT_OK；Heartbeat 与 Cron 的适用场景；「何时主动触达」与「何时保持安静」；用 `memory/heartbeat-state.json` 记录上次检查；「记忆维护」——定期把每日文件提炼进 MEMORY.md。

**建议采纳：** 现有心跳说明可补充：(1) 心跳与 cron 的区分，(2) 可选的 heartbeat-state.json 用法，(3) 心跳时顺带把近期 daily 提炼到 MEMORY.md。

## 8. Make It Yours（随你而定）

**模板要点：** 「这是起点，可随使用增加自己的惯例与规则。」

**建议采纳：** 保留，鼓励随使用人与团队演进。

---

## 汇总：现有智能体可补充项

| 模块           | 建议补充/调整 |
|----------------|----------------|
| 身份与首次接待 | 对客智能体：身份在 SOUL/IDENTITY；禁止问客户「您是谁」；BOOTSTRAP 仅配置者；Red Line 直接问候并服务。 |
| Session Startup | 保持 4 步；加身份加载与「不要询问客户身份」；「无需征询许可，直接执行」 |
| Memory         | 「写下来，不要只在脑子里记」；MEMORY.md 仅主会话、不在群聊加载 |
| Red Lines      | 明确「不外泄」；`trash` > `rm` |
| External vs Internal | 「可自由做」与「先问再做」两列表 |
| Group Chats    | 何时说话/何时沉默；反应用法；「参与不主导」 |
| Tools          | 若在渠道回复，增加平台格式（Discord/WhatsApp/企微） |
| Heartbeats     | 心跳与 cron 区分；可选状态文件；记忆维护 |

---

**中英文双版约定：** 提供 `AGENTS.md`（英文，供 OpenClaw 系统提示词注入）与 `zh-CN/AGENTS.md`（中文，供团队阅读），内容等价；`zh-CN/` 整目录可拷贝到业务使用。

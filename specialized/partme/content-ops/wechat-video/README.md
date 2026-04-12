# 视频号内容管线 (Wechat Video Agents)

> 基于 [ANALYSIS-渠道与流程对齐 OctoFlow](../../ANALYSIS-渠道与流程对齐OctoFlow.md) §2.1 建议，为**视频号**（微信生态短视频）提供与 xiaohongshu / wechat-article 同构的内容管线七件套：热门监控、爆款拆解、二创、自动发布、数据助手、原创、评论管理。读（抓取）可用通用抓取或第三方数据，写（发布）依赖视频号开放能力或浏览器自动化。

## 技能选型

| 序号 | 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|------|----------|--------------|----------|
| 1 | **ClawHub（为主）** | [clawhub.ai/skills?q=weixin](https://clawhub.ai/skills?sort=downloads&q=weixin) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug>` |
| 2 | **skills.sh（取最优）** | [skills.sh/?q=baoyu](https://skills.sh/?q=baoyu) | [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md) | `npx skills add <owner/repo> --skill <名>` |

## 技能评估结论（摘录）

> 完整评估见 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md)。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。** 视频号发布可选用 wechat-video-publish（ClawHub）。

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown/报告格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 封面/配图 | baoyu-cover-image, baoyu-article-illustrator | — |
| 3 | 发布到视频号 | wechat-video-publish（ClawHub） | 浏览器自动化 |
| 4 | 图片压缩 | baoyu-compress-image | — |

## 补充能力（完整栈）

七件套之外本管线可用上的补充能力（与 [SKILLS-EVALUATION.md §6.1](./SKILLS-EVALUATION.md) 一致）：

| 序号 | 补充能力 | 用途 | 推荐技能 | 来源 |
|------|----------|------|----------|------|
| 1 | 发布到视频号 | 视频号发布（开放能力或浏览器） | wechat-video-publish | ClawHub |
| 2 | 评论回复/采集 | 回复草稿、评论拉取 | 按需 ClawHub/skills.sh | — |
| 3 | 多语言与翻译 | 多语言内容、翻译 | baoyu-translate | skills.sh |
| 4 | 信息图/漫画风配图 | 丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh |

## 必须保证的七个环节

1. **热门监控**：每日/按需搜索视频号/微信生态热点与爆款短视频，产出日报或摘要。
2. **爆款拆解**：对爆款短视频做拆解（标题、钩子、结构、主题），产出拆解框架供二创与数据助手使用。
3. **二创**：根据拆解框架与主题进行新文案与配图/封面，产出草稿供发布与数据助手使用。
4. **自动发布**：将已通过草稿发布到视频号（需视频号开放能力或浏览器），并记录结果。
5. **数据助手**：解析数据、交叉验证效果，反馈给爆款拆解（形成闭环）。
6. **原创**：强调原创；用户主图/选题+热点做原创短视频脚本与封面，产出草稿。
7. **评论管理**：评论采集、起草回复、情感分析；回复需审批/门禁后发布。

**管线关系：** 热门监控 → 日报/摘要 → 爆款拆解 → 拆解框架 → 二创/原创 → 草稿+配图 → 自动发布 → 发布日志 → 数据助手 + 评论管理 → 反馈至爆款拆解与热门监控。

## 主智能体

- 本渠道主智能体目录：`1-wechat-video-specialist`（若存在 `*-strategist` 目录，保持不重命名并作为该组最后扩展角色）。

## 智能体清单

| 序号 | Agent id                     | 展示名           | 目录                               | 职责摘要 |
|------|------------------------------|------------------|------------------------------------|----------|
| 1    | wechat-video-hot-monitor     | 视频号热门监控   | 2-wechat-video-hot-monitor         | 每日/按需搜索视频号热点与爆款，产出日报或摘要 |
| 2    | wechat-video-viral-breakdown | 视频号爆款拆解   | 3-wechat-video-viral-breakdown     | 对爆款短视频做拆解，产出结构化拆解框架 |
| 3    | wechat-video-rewrite         | 视频号二创       | 4-wechat-video-rewrite             | 根据拆解框架与主题创作新文案与配图/封面 |
| 4    | wechat-video-publisher       | 视频号自动发布   | 5-wechat-video-publisher           | 将已通过草稿发布到视频号并记录结果（需开放能力/浏览器） |
| 5    | wechat-video-data-assistant  | 视频号数据助手   | 6-wechat-video-data-assistant      | 解析数据、交叉验证效果、反馈给爆款拆解 |
| 6    | wechat-video-write           | 视频号原创       | 7-wechat-video-write               | 强调原创：用户主图/选题+热点做原创短视频内容，产出草稿 |
| 7    | wechat-video-comment-manager | 视频号评论管理   | 8-wechat-video-comment-manager     | 评论采集、起草回复、情感分析；回复需审批/门禁后发布 |

## 智能工作执行链路

七件套按以下链路协同执行；可按时序触发（如每日）或按需触发单环节。

| 步骤 | 环节 | 智能体 | 输入 | 输出 | 说明 |
|------|------|--------|------|------|------|
| 1 | 热门监控 | wechat-video-hot-monitor | 关键词/品类/时间范围 | 日报或按需摘要（热点、爆款列表） | 入口；可为定时或人工触发 |
| 2 | 爆款拆解 | wechat-video-viral-breakdown | 日报/摘要中的爆款链接或列表 | 拆解框架（标题、钩子、结构、主题） | 消费监控产出，供二创与数据侧使用 |
| 3a | 二创 | wechat-video-rewrite | 拆解框架 + 主题 | 草稿（文案 + 封面 + 配图） | 基于拆解做差异化二创，不发布 |
| 3b | 原创 | wechat-video-write | 用户选题 + 热点/爆款洞察 | 草稿（文案 + 封面 + 配图） | 独立于拆解的原创内容生产 |
| 4 | 自动发布 | wechat-video-publisher | 已审核草稿 | 发布结果日志（链接、时间、状态） | 仅发布已通过审核内容；发布前压缩图片 |
| 5 | 数据助手 | wechat-video-data-assistant | 发布日志 + 互动数据 | 可执行反馈（关键词/拆解维度/优先主题） | 交叉验证效果，反馈至爆款拆解与监控 |
| 6 | 评论管理 | wechat-video-comment-manager | 文章/账号评论源 | 回复草稿 + 情感摘要 | 回复须审批/门禁后由人工或流程发布 |

**闭环：** 数据助手的反馈驱动爆款拆解调整搜索与拆解标准，热门监控可据此调整关键词与范围，形成「监控 → 拆解 → 内容 → 发布 → 数据 → 反馈」闭环。

**并行与触发：** 3a 二创与 3b 原创可并行；评论管理可与数据助手并行。执行顺序 1 → 2 → (3a 或 3b) → 4 → 5/6；步骤 5、6 可持续运行或按周期执行。

## 预设技能（按评估结论，去重取最优）

以下为 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md) 最终推荐；同能力只选一个来源。

| 步骤 | Agent id                     | 推荐技能 | 来源 | 说明 |
|------|------------------------------|----------|------|------|
| 1 | wechat-video-hot-monitor     | baoyu-url-to-markdown, baoyu-format-markdown | skills.sh | 抓取+日报格式 |
| 2 | wechat-video-viral-breakdown | baoyu-url-to-markdown, baoyu-format-markdown | skills.sh | 抓取成文+拆解格式 |
| 3a | wechat-video-rewrite         | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面与配图 |
| 3b | wechat-video-write           | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | wechat-video-publisher       | baoyu-compress-image；可选 wechat-video-publish | skills.sh + ClawHub | 压缩+发布 |
| 5 | wechat-video-data-assistant  | baoyu-format-markdown | skills.sh | 报告格式 |
| 6 | wechat-video-comment-manager | （按需选评论采集与回复技能） | ClawHub/skills.sh | 评论拉取、回复草稿 |

### 安装前置与唯一命令来源

**第一步：安装 SkillHub CLI**（仅首次需要）

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**全部技能安装/卸载以本页下方「七件套全部可使用的技能」或 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 为准。** 安装后目录名需与 config 中 `skills` 一致。勿在 TOOLS.md 存凭证。

### 七件套全部可使用的技能：全部安装 / 全部卸载命令

与 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 一致；能用上的全列（同质取一，可并存全列）。

**全部安装命令**

```bash
# ClawHub — 视频号发布（按需）
clawhub install wechat-video-publish --workdir ~/.openclaw;

# skills.sh — 抓取、格式、配图、压缩、补充
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-translate -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-infographic -y -g;
npx skills add jimliu/baoyu-skills --skill baoyu-comic -y -g;
```

**全部卸载命令**

```bash
# ClawHub
clawhub uninstall wechat-video-publish;

# skills.sh
npx skills remove baoyu-url-to-markdown;
npx skills remove baoyu-format-markdown;
npx skills remove baoyu-cover-image;
npx skills remove baoyu-article-illustrator;
npx skills remove baoyu-compress-image;
npx skills remove baoyu-translate;
npx skills remove baoyu-infographic;
npx skills remove baoyu-comic;
```

## 配置说明

- **Workspace：** `~/.openclaw/workspace-wechat-video-<agentId>`。
- **Config 片段：** `config/openclaw-wechat-video-fragment.json`。
- **路由：** 通过 bindings 将渠道或会话路由到各 agent id。

## 初始化命令（按执行链路顺序）

### 添加七件套

```bash
openclaw agents add wechat-video-hot-monitor       --workspace ~/.openclaw/workspace-wechat-video-hot-monitor;
openclaw agents add wechat-video-viral-breakdown   --workspace ~/.openclaw/workspace-wechat-video-viral-breakdown;
openclaw agents add wechat-video-rewrite           --workspace ~/.openclaw/workspace-wechat-video-rewrite;
openclaw agents add wechat-video-write             --workspace ~/.openclaw/workspace-wechat-video-write;
openclaw agents add wechat-video-publisher         --workspace ~/.openclaw/workspace-wechat-video-publisher;
openclaw agents add wechat-video-data-assistant    --workspace ~/.openclaw/workspace-wechat-video-data-assistant;
openclaw agents add wechat-video-comment-manager   --workspace ~/.openclaw/workspace-wechat-video-comment-manager;
```

### 按渠道绑定（示例：wecom）

```bash
openclaw agents bind --agent wechat-video-hot-monitor       --bind wecom:wechat-video-hot-monitor;
openclaw agents bind --agent wechat-video-viral-breakdown   --bind wecom:wechat-video-viral-breakdown;
openclaw agents bind --agent wechat-video-rewrite           --bind wecom:wechat-video-rewrite;
openclaw agents bind --agent wechat-video-write             --bind wecom:wechat-video-write;
openclaw agents bind --agent wechat-video-publisher         --bind wecom:wechat-video-publisher;
openclaw agents bind --agent wechat-video-data-assistant    --bind wecom:wechat-video-data-assistant;
openclaw agents bind --agent wechat-video-comment-manager   --bind wecom:wechat-video-comment-manager;
```

### 删除七件套（需先解除绑定）

```bash
openclaw agents remove wechat-video-hot-monitor;
openclaw agents remove wechat-video-viral-breakdown;
openclaw agents remove wechat-video-rewrite;
openclaw agents remove wechat-video-write;
openclaw agents remove wechat-video-publisher;
openclaw agents remove wechat-video-data-assistant;
openclaw agents remove wechat-video-comment-manager;
```

## 文件结构（每智能体）

与 zhihu、weibo 一致：`AGENTS.md`、`zh-CN/AGENTS.md`、`SOUL.md`、`IDENTITY.md`、`TOOLS.md`、`BOOTSTRAP.md`、`HEARTBEAT.md`、`USER.md` 及 zh-CN 对应文件。

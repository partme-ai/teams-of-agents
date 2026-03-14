# 知乎内容管线 (Zhihu Agents)

> 基于 [ANALYSIS-渠道与流程对齐 OctoFlow](../../ANALYSIS-渠道与流程对齐OctoFlow.md) 建议，为**知乎**提供与 wechat-article / xiaohongshu 同构的内容管线七件套：热门监控、爆款拆解、二创、原创、自动发布、数据助手、评论管理。读（抓取）采用通用 Playwright/Firecrawl，写（发布）采用 social-push 想法发布或浏览器自动化。

## 技能选型

| 序号 | 来源 | 搜索链接 | 技能一览文档 | 安装命令 |
|------|------|----------|--------------|----------|
| 1 | **ClawHub（为主）** | [clawhub.ai/skills?q=zhihu](https://clawhub.ai/skills?sort=downloads&q=zhihu) | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `clawhub install <slug> --workdir ~/.openclaw;` |
| 2 | **SkillHub（国内推荐）** | SkillHub 搜索「知乎」 | [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) | `skillhub install <slug>`（需先安装 SkillHub CLI） |
| 3 | **skills.sh（取最优）** | [skills.sh/?q=zhihu](https://skills.sh/?q=zhihu)、[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu) | [SKILLS-SH-SKILLS.md](./SKILLS-SH-SKILLS.md) | `npx skills add <owner/repo> --skill <名> -y -g;` |

## 技能评估结论（摘录）

> 完整评估见 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md)。原则：**ClawHub 为主、skills.sh 取最优；同能力只保留一个最优技能。** 知乎 ClawHub 技能待补充，当前以 Baoyu 为主。

| 序号 | 能力 | 首选 | 备选/不重复装 |
|------|------|------|----------------|
| 1 | 链接→Markdown/报告格式 | baoyu-url-to-markdown, baoyu-format-markdown | — |
| 2 | 封面/长文配图 | baoyu-cover-image, baoyu-article-illustrator | — |
| 3 | 发布到知乎 | social-push | 按需选一 |
| 4 | 图片压缩 | baoyu-compress-image | — |

## 补充能力（完整栈）

七件套之外本管线可用上的补充能力（与 [SKILLS-EVALUATION.md §6.1](./SKILLS-EVALUATION.md) 一致）：

| 序号 | 补充能力 | 用途 | 推荐技能 | 来源 |
|------|----------|------|----------|------|
| 1 | 发布到知乎 | 知乎想法/多平台发布 | social-push | skills.sh / ClawHub |
| 2 | 评论回复/采集 | 回复草稿、评论拉取 | 按需 ClawHub/skills.sh | — |
| 3 | 多语言与翻译 | 多语言内容、翻译 | baoyu-translate | skills.sh |
| 4 | 信息图/漫画风配图 | 丰富二创形式 | baoyu-infographic、baoyu-comic | skills.sh |

## 必须保证的七个环节

1. **热门监控**：每日/按需搜索知乎行业热点与爆款想法/回答/文章，产出日报或摘要，供爆款拆解与数据助手使用。
2. **爆款拆解**：自动搜索知乎行业热点与爆款想法/回答/文章，产出结构化拆解框架（标题/钩子/结构/主题等），供二创与数据助手使用。
3. **二创**：根据拆解框架与主题进行新文案与配图（封面 + 文中图），产出草稿供发布与数据助手使用。
4. **原创**：强调原创；用户主图+热点/爆款做原创想法/回答/文章，产出草稿供发布与数据助手。
5. **自动发布**：将已通过草稿发布到知乎（想法/回答/文章），并记录发布结果供数据助手分析。
6. **数据助手**：解析数据、主题与效果交叉验证，将可执行结论反馈给爆款拆解（形成闭环）。
7. **评论管理**：评论采集、起草回复、情感分析；回复需审批/门禁后发布。

**管线关系：** 热门监控 → 日报/摘要 → 爆款拆解 → 拆解框架 → 二创/原创 → 草稿+配图 → 自动发布 → 发布日志 → 数据助手 + 评论管理 → 反馈至爆款拆解与热门监控。

## 智能体清单

| 序号 | Agent id               | 展示名         | 目录                           | 职责摘要 |
|------|------------------------|----------------|--------------------------------|----------|
| 1    | zhihu-hot-monitor      | 知乎热门监控   | 1-zhihu-hot-monitor            | 每日/按需搜索知乎热点与爆款，产出日报或摘要供拆解与数据助手 |
| 2    | zhihu-viral-breakdown  | 知乎爆款拆解   | 2-zhihu-viral-breakdown        | 搜索知乎热点与爆款，产出结构化拆解框架 |
| 3    | zhihu-rewrite          | 知乎二创       | 3-zhihu-rewrite                | 根据拆解框架与主题创作新文案与配图 |
| 4    | zhihu-write            | 知乎原创       | 4-zhihu-write                  | 强调原创：用户主图+热点/爆款做原创想法/回答/文章，产出草稿供发布与数据助手 |
| 5    | zhihu-publisher        | 知乎自动发布   | 5-zhihu-publisher              | 将已通过草稿发布到知乎并记录结果 |
| 6    | zhihu-data-assistant   | 知乎数据助手   | 6-zhihu-data-assistant         | 解析数据、交叉验证效果、反馈给爆款拆解 |
| 7    | zhihu-comment-manager  | 知乎评论管理   | 7-zhihu-comment-manager        | 评论采集、起草回复、情感分析；回复需审批/门禁后发布 |

## 智能工作执行链路

七件套按以下链路协同执行；可按时序触发（如每日）或按需触发单环节。

| 步骤 | 环节 | 智能体 | 输入 | 输出 | 说明 |
|------|------|--------|------|------|------|
| 1 | 热门监控 | zhihu-hot-monitor | 关键词/品类/时间范围 | 日报或按需摘要（热点、爆款列表） | 入口；可为定时或人工触发 |
| 2 | 爆款拆解 | zhihu-viral-breakdown | 日报/摘要中的爆款链接或列表 | 拆解框架（标题、钩子、结构、主题） | 消费监控产出，供二创与数据侧使用 |
| 3a | 二创 | zhihu-rewrite | 拆解框架 + 主题 | 草稿（文案 + 封面 + 配图） | 基于拆解做差异化二创，不发布 |
| 3b | 原创 | zhihu-write | 用户选题 + 热点/爆款洞察 | 草稿（文案 + 封面 + 配图） | 独立于拆解的原创内容生产 |
| 4 | 自动发布 | zhihu-publisher | 已审核草稿 | 发布结果日志（链接、时间、状态） | 仅发布已通过审核内容；发布前压缩图片 |
| 5 | 数据助手 | zhihu-data-assistant | 发布日志 + 互动数据 | 可执行反馈（关键词/拆解维度/优先主题） | 交叉验证效果，反馈至爆款拆解与监控 |
| 6 | 评论管理 | zhihu-comment-manager | 文章/账号评论源 | 回复草稿 + 情感摘要 | 回复须审批/门禁后由人工或流程发布 |

**闭环：** 数据助手的反馈驱动爆款拆解调整搜索与拆解标准，热门监控可据此调整关键词与范围，形成「监控 → 拆解 → 内容 → 发布 → 数据 → 反馈」闭环。

**并行与触发：** 3a 二创与 3b 原创可并行；评论管理可与数据助手并行。执行顺序 1 → 2 → (3a 或 3b) → 4 → 5/6；步骤 5、6 可持续运行或按周期执行。

## 预设技能（按评估结论，去重取最优）

以下为 [SKILLS-EVALUATION.md](./SKILLS-EVALUATION.md) 最终推荐；同能力只选一个来源。

| 步骤 | Agent id               | 推荐技能 | 来源 | 说明 |
|------|------------------------|----------|------|------|
| 1 | zhihu-hot-monitor      | zhihu-hot-cn；zhihu-assistant-skill；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh | 热榜监控+热榜抓取/回答草稿 + 抓取+日报格式 |
| 2 | zhihu-viral-breakdown  | zhihu-hot-cn；zhihu-assistant-skill；baoyu-url-to-markdown, baoyu-format-markdown | ClawHub/SkillHub；skills.sh | 热榜/趋势 + 抓取成文+拆解格式 |
| 3a | zhihu-rewrite          | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 封面与配图 |
| 3b | zhihu-write            | baoyu-cover-image, baoyu-article-illustrator | skills.sh | 同 rewrite |
| 4 | zhihu-publisher        | zhihu（管理/发布/获取）；baoyu-compress-image；可选 social-push | ClawHub/SkillHub；skills.sh | 知乎工具+压缩+发布 |
| 5 | zhihu-data-assistant   | zhihu-hot-cn；baoyu-format-markdown | ClawHub/SkillHub；skills.sh | 热榜趋势+报告格式 |
| 6 | zhihu-comment-manager  | zhihu-assistant-skill（回答草稿推飞书）；zhihu（管理）；按需评论采集与回复 | ClawHub/SkillHub；skills.sh | 回答草稿+飞书审核+评论拉取 |

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
# 第一步：安装 SkillHub CLI（仅首次需要，国内推荐）
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash

# ClawHub/SkillHub — 知乎工具 + 热榜监控 + 热榜抓取与回答草稿助手
skillhub install zhihu
skillhub install zhihu-hot-cn
skillhub install zhihu-assistant-skill

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
# ClawHub/SkillHub 安装的知乎技能
clawhub uninstall zhihu;
clawhub uninstall zhihu-hot-cn;
clawhub uninstall zhihu-assistant-skill;

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

- **Workspace：** 各智能体 workspace 为 `~/.openclaw/workspace-zhihu-<agentId>`；部署时将本目录下对应子目录复制或链接到该路径。
- **Config 片段：** `config/openclaw-zhihu-fragment.json`，合并进主 openclaw 配置即可。
- **路由：** 通过 bindings 将对应渠道或会话路由到各 agent id。

## 初始化命令（按执行链路顺序）

### 添加七件套

```bash
openclaw agents add zhihu-hot-monitor       --workspace ~/.openclaw/workspace-zhihu-hot-monitor;
openclaw agents add zhihu-viral-breakdown   --workspace ~/.openclaw/workspace-zhihu-viral-breakdown;
openclaw agents add zhihu-rewrite           --workspace ~/.openclaw/workspace-zhihu-rewrite;
openclaw agents add zhihu-write             --workspace ~/.openclaw/workspace-zhihu-write;
openclaw agents add zhihu-publisher        --workspace ~/.openclaw/workspace-zhihu-publisher;
openclaw agents add zhihu-data-assistant   --workspace ~/.openclaw/workspace-zhihu-data-assistant;
openclaw agents add zhihu-comment-manager  --workspace ~/.openclaw/workspace-zhihu-comment-manager;
```

### 按渠道绑定（示例：wecom）

```bash
openclaw agents bind --agent zhihu-hot-monitor       --bind wecom:zhihu-hot-monitor;
openclaw agents bind --agent zhihu-viral-breakdown   --bind wecom:zhihu-viral-breakdown;
openclaw agents bind --agent zhihu-rewrite           --bind wecom:zhihu-rewrite;
openclaw agents bind --agent zhihu-write            --bind wecom:zhihu-write;
openclaw agents bind --agent zhihu-publisher         --bind wecom:zhihu-publisher;
openclaw agents bind --agent zhihu-data-assistant    --bind wecom:zhihu-data-assistant;
openclaw agents bind --agent zhihu-comment-manager   --bind wecom:zhihu-comment-manager;
```

### 删除七件套（需先解除绑定）

```bash
openclaw agents remove zhihu-hot-monitor;
openclaw agents remove zhihu-viral-breakdown;
openclaw agents remove zhihu-rewrite;
openclaw agents remove zhihu-write;
openclaw agents remove zhihu-publisher;
openclaw agents remove zhihu-data-assistant;
openclaw agents remove zhihu-comment-manager;
```

## 文件结构（每智能体）

与 wechat-article、bilibili 一致：`AGENTS.md`、`zh-CN/AGENTS.md`、`SOUL.md`、`zh-CN/SOUL.md`、`IDENTITY.md`、`zh-CN/IDENTITY.md`、`TOOLS.md`、`zh-CN/TOOLS.md`、`BOOTSTRAP.md`、`zh-CN/BOOTSTRAP.md`、`USER.md`、`HEARTBEAT.md`、`zh-CN/HEARTBEAT.md`。

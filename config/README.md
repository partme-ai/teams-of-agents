# 配置片段说明

本目录提供可合并进 `~/.openclaw/openclaw.json` 的配置片段。

## 实际目录规范（默认 profile）

片段中 **workspace** 与 **agentDir** 已按实际部署目录书写，合并后即可使用：

- **Workspace：** `~/.openclaw/workspace-<agentId>`（每个智能体一个独立目录）
- **Agent dir：** `~/.openclaw/agents/<agentId>/agent`

部署时可将仓库内对应智能体目录（如 `company/internal/1-admin-assistant`、`company/customer/6-cs-assistant`、`content-ops/xiaohongshu/1-xiaohongshu-viral-breakdown`、`channels/assistant/1-openclaw-assistant`）复制或软链到 `~/.openclaw/workspace-<agentId>`。

## 片段列表

| 文件 | 用途 |
|------|------|
| `openclaw-agents-fragment.json` | 通用多智能体示例（含 main、pm、design、dev、ops、blog 及 12 个 it 角色、game-ops）；workspace/agentDir 已用 `~/.openclaw/workspace-<id>` 与 `~/.openclaw/agents/<id>/agent`。 |
| `openclaw-company-fragment.json` | **公司智能体**：对内（行政、运营、商务、老板/老板娘助理）、对外（客服助理、客服专员-小暖）；workspace 为 `~/.openclaw/workspace-<agentId>`；仓库路径 `company/internal/`、`company/customer/`。 |
| `openclaw-it-fragment.json` | **it 软件开发团队**专用：技术总监（编排者）+ 12 个子角色，单网关内协作；workspace 为 `~/.openclaw/workspace-<agentId>`。 |
| `openclaw-scrm-fragment.json` | **SCRM 运营团队**专用：6 阶段 + 客服 3 子角色；多网关 profile `scrm`，端口 18819，状态目录 `~/.openclaw-scrm`；workspace 为 `~/.openclaw-scrm/workspace-scrm/<agentId>`。 |
| `openclaw-web3-fragment.json` | **Web3 团队**专用：chain-analyst 等四 Agent；多网关 profile `web3`，端口 18869，状态目录 `~/.openclaw-web3`。 |
| `openclaw-discord-fragment.json` | **Discord 专用**：discord-mod、discord-community、discord-support；仓库路径 `channels/discord/`。 |
| `openclaw-wechat-article-fragment.json` | **公众号文章管线**：wechat-article 七件套；仓库路径 `content-ops/wechat-article/`。 |
| `openclaw-telegram-fragment.json` | **Telegram 专用**：telegram-bot-developer、telegram-community、telegram-support；仓库路径 `channels/telegram/`。 |
| `openclaw-game-fragment.json` | **游戏**：game-master 等；workspace 为 `~/.openclaw/workspace-<agentId>`。 |
| `openclaw-xiaohongshu-fragment.json` | **小红书管线**：xiaohongshu 七件套；仓库路径 `content-ops/xiaohongshu/`。 |
| `openclaw-xiaohongshu-ops-delegation-example.json` | **小红书运营助理 + 单 Agent 委派示例**：全局 `tools.agentToAgent.enabled: false`，仅 `xiaohongshu-ops-assistant` 在 `agents.list[]` 中配置委派到七件套；仓库路径 `company/internal/xiaohongshu-ops-assistant` + `content-ops/xiaohongshu/`。 |
| `openclaw-bilibili-fragment.json` | **B站 (bilibili) 管线**：bilibili 七件套；仓库路径 `content-ops/bilibili/`。 |
| `openclaw-zhihu-fragment.json` | **知乎管线**：zhihu 七件套；仓库路径 `content-ops/zhihu/`。 |
| `openclaw-baijiahao-fragment.json` | **百家号管线**：baijiahao 七件套；仓库路径 `content-ops/baijiahao/`。 |
| `openclaw-weibo-fragment.json` | **微博管线**：weibo 七件套；仓库路径 `content-ops/weibo/`。 |
| `openclaw-wechat-video-fragment.json` | **视频号管线**：wechat-video 七件套；仓库路径 `content-ops/wechat-video/`。 |
| `openclaw-juejin-fragment.json` | **掘金管线**：juejin 七件套；仓库路径 `content-ops/juejin/`。 |
| `openclaw-toutiao-fragment.json` | **头条号管线**：toutiao 七件套；仓库路径 `content-ops/toutiao/`。 |
| `openclaw-douyin-fragment.json` | **抖音管线**：douyin 七件套；仓库路径 `content-ops/douyin/`。 |
| `openclaw-kuaishou-fragment.json` | **快手管线**：kuaishou 七件套；仓库路径 `content-ops/kuaishou/`。 |

## it 软件开发团队（openclaw-it-fragment.json）

- **workspace 路径**：`~/.openclaw/workspace-<agentId>`（如 `~/.openclaw/workspace-technical-director`、`~/.openclaw/workspace-project-manager`），与 agent id 一致。仓库中 `it/1-technical-director` 等编号仅表示顺序，部署时复制或链接到对应 workspace 即可。
- **agent-to-agent**：片段中已设置 `tools.agentToAgent.enabled: true`，`allow` 包含 technical-director 及全部 12 个子角色 id。
- **合并方式**：将片段中的 `agents`、`bindings`、`tools` 合并进你的 `openclaw.json`；若已有同名键，将 `agents.list` 与现有列表合并。多 profile 时 it 实例需独立的 `OPENCLAW_CONFIG_PATH`、`OPENCLAW_STATE_DIR` 与端口（见主 README §3 多网关）。

## SCRM 运营团队（openclaw-scrm-fragment.json）

- **workspace 路径**：使用 `~/.openclaw-scrm/workspace-scrm/<agentId>`（多 profile 时 STATE_DIR 为 `~/.openclaw-scrm`）。仓库 `scrm/lead-gen`、`scrm/acquisition` 等复制或链接到对应 workspace；客服 3 个 Agent（presale、aftersale、tech）可复用 `channels/wecom-kf/` 下模板。
- **bindings**：片段默认将 telegram、discord、wecom-kf 均路由到 scrm-orchestrator；若需 wecom-kf 按账号直连 presale/aftersale/tech，请按 partme-docs 客服技术方案增加 `match.accountId` 或 `match.peer` 的绑定。
- **合并方式**：同 it；多 profile 时使用 `openclaw --profile scrm gateway --port 18819`，配置与状态目录见主 README §3、§9。

## Web3 团队（openclaw-web3-fragment.json）

- **workspace 路径**：使用 `~/.openclaw-web3/workspace-web3/<agentId>`（profile web3 时 STATE_DIR 为 `~/.openclaw-web3`）。将仓库 `web3/chain-analyst`、`web3/defi-scout` 等复制或链接到对应 workspace。
- **合并方式**：同 it；多 profile 时使用 `openclaw --profile web3 gateway --port 18869`。能力与架构见 partme-docs `8、OpenClaw-垂直领域应用分析/Web3`。

## Discord 专用智能体（openclaw-discord-fragment.json）

- **智能体**：discord-mod（审核）、discord-community（社区运营）、discord-support（客服）；各预设技能 `discord`（[vm0-ai/vm0-skills](https://github.com/vm0-ai/vm0-skills)）。
- **workspace 路径**：`~/.openclaw/workspace-discord-mod`、`~/.openclaw/workspace-discord-community`、`~/.openclaw/workspace-discord-support`；部署时将仓库对应目录复制或链接到上述路径。
- **技能安装**：需将 discord 技能安装到 OpenClaw 可加载的 skills 目录，并配置 `DISCORD_BOT_TOKEN`。详见 [channels/discord/README.md](../channels/discord/README.md)。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置；按需绑定 Discord 渠道到对应 agent（如 `discord:discord-mod`）。

## 公众号文章管线（openclaw-wechat-article-fragment.json）

- **智能体**：wechat-article 七件套（爆款拆解、二创、自动发布、数据助手、热门监控、写作、评论管理）；预设技能见片段内 `skills`（ClawHub：wechat-article-extractor、wechat-ai-publisher；skills.sh：baoyu-*）。
- **workspace 路径**：`~/.openclaw/workspace-wechat-article-*`；部署时将仓库 `content-ops/wechat-article/1-...`～`content-ops/wechat-article/7-...` 复制或链接到对应路径。
- **技能安装**：以 ClawHub 为主、两源取最优；需将 ClawHub 与 baoyu 技能安装到 OpenClaw 可加载的 skills 目录；发布智能体需配置公众号凭证（环境变量或 EXTEND.md，勿写入 TOOLS.md）。详见 [content-ops/wechat-article/README.md](../content-ops/wechat-article/README.md)。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置；按需绑定渠道到对应 agent。

## Telegram 专用智能体（openclaw-telegram-fragment.json）

- **智能体**：telegram-bot-developer（机器人开发）、telegram-community（社区运营）、telegram-support（客服）；各预设技能 `telegram-bot-builder`（[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)）。
- **workspace 路径**：`~/.openclaw/workspace-telegram-bot-developer`、`~/.openclaw/workspace-telegram-community`、`~/.openclaw/workspace-telegram-support`；部署时将仓库对应目录复制或链接到上述路径。
- **技能安装**：需将 telegram-bot-builder 技能安装到 OpenClaw 可加载的 skills 目录，并配置 `BOT_TOKEN`。详见 [channels/telegram/README.md](../channels/telegram/README.md)。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置；按需绑定 Telegram 渠道到对应 agent（如 `telegram:telegram-bot-developer`）。

## 小红书管线（openclaw-xiaohongshu-fragment.json）

- **智能体**：xiaohongshu 七件套（爆款拆解、二创、自动发布、数据助手、热门监控、写作、评论管理）；技能以 **ClawHub 优先**、**skills.sh 后补**（[jimliu/baoyu-skills](https://skills.sh/?q=baoyu)）。
- **workspace 路径**：`~/.openclaw/workspace-xiaohongshu-*`；部署时将仓库 `content-ops/xiaohongshu/1-...`～`content-ops/xiaohongshu/7-...` 复制或链接到对应 workspace。
- **技能安装**：先在 [ClawHub](https://clawhub.ai/skills?sort=downloads&q=xiaohongshu) 搜索并安装小红书相关技能；未覆盖处用 skills.sh 的 baoyu-* 技能补充。详见 [content-ops/xiaohongshu/README.md](../content-ops/xiaohongshu/README.md)。
- **合并方式**：若仅用小红书管线可单独合并本片段；若已合并 company 片段，本片段与 company 中可能含的 xiaohongshu 条目 id 相同，可二选一或统一 workspace 指向 `content-ops/xiaohongshu/` 目录。

### 渠道运营助理委派：单 Agent 配置（一对多）

若使用 **渠道专用运营智能体**（如 [company/internal/xiaohongshu-ops-assistant](../company/internal/xiaohongshu-ops-assistant)），希望**仅该运营助理**能委派到本渠道七件套，其他 Agent 不能委派，应采用 **单 Agent 配置**，而非全局 `tools.agentToAgent`。

| 配置位置 | 作用范围 |
|----------|----------|
| `tools.agentToAgent` | 全局默认，所有 Agent 继承 |
| `agents.list[].tools.agentToAgent` | 仅对该 Agent 生效（覆盖全局） |

**优先级：** Agent 级别的配置 > 全局配置。参考 [OpenClaw Tools - Agent 覆盖](https://docs.openclaw.ai/tools#tool-profiles-base-allowlist)。

**做法：**

1. 全局关闭或清空委派：`tools.agentToAgent.enabled: false` 或 `allow: []`。
2. 在 `agents.list[]` 中**仅**为运营助理这一条增加 `tools.agentToAgent`，例如：

```json
{
  "tools": {
    "profile": "full",
    "agentToAgent": {
      "enabled": false
    }
  },
  "agents": {
    "list": [
      {
        "id": "xiaohongshu-ops-assistant",
        "default": true,
        "name": "小红书运营助理",
        "workspace": "~/.openclaw/workspace-xiaohongshu-ops-assistant",
        "agentDir": "~/.openclaw/agents/xiaohongshu-ops-assistant/agent",
        "tools": {
          "agentToAgent": {
            "enabled": true,
            "allow": [
              "xiaohongshu-ops-assistant",
              "xiaohongshu-hot-monitor",
              "xiaohongshu-viral-breakdown",
              "xiaohongshu-rewrite",
              "xiaohongshu-write",
              "xiaohongshu-publisher",
              "xiaohongshu-data-assistant",
              "xiaohongshu-comment-manager"
            ]
          }
        }
      },
      { "id": "xiaohongshu-hot-monitor", "name": "小红书热门监控", "workspace": "~/.openclaw/workspace-xiaohongshu-hot-monitor", "agentDir": "~/.openclaw/agents/xiaohongshu-hot-monitor/agent" },
      { "id": "xiaohongshu-viral-breakdown", "name": "小红书爆款拆解", "workspace": "~/.openclaw/workspace-xiaohongshu-viral-breakdown", "agentDir": "~/.openclaw/agents/xiaohongshu-viral-breakdown/agent" },
      { "id": "xiaohongshu-rewrite", "name": "小红书二创", "workspace": "~/.openclaw/workspace-xiaohongshu-rewrite", "agentDir": "~/.openclaw/agents/xiaohongshu-rewrite/agent" },
      { "id": "xiaohongshu-write", "name": "小红书原创", "workspace": "~/.openclaw/workspace-xiaohongshu-write", "agentDir": "~/.openclaw/agents/xiaohongshu-write/agent" },
      { "id": "xiaohongshu-publisher", "name": "小红书自动发布", "workspace": "~/.openclaw/workspace-xiaohongshu-publisher", "agentDir": "~/.openclaw/agents/xiaohongshu-publisher/agent" },
      { "id": "xiaohongshu-data-assistant", "name": "小红书数据助手", "workspace": "~/.openclaw/workspace-xiaohongshu-data-assistant", "agentDir": "~/.openclaw/agents/xiaohongshu-data-assistant/agent" },
      { "id": "xiaohongshu-comment-manager", "name": "小红书评论管理", "workspace": "~/.openclaw/workspace-xiaohongshu-comment-manager", "agentDir": "~/.openclaw/agents/xiaohongshu-comment-manager/agent" }
    ]
  }
}
```

其他渠道（公众号、视频号、抖音、B站等）同理：全局不开放委派，仅在对应 `agents.list[]` 中为 `<platform>-ops-assistant` 一项配置 `tools.agentToAgent`，实现**内部一对多**（仅该运营助理可委派到其 7 件套）。

可直接合并示例片段：[openclaw-xiaohongshu-ops-delegation-example.json](openclaw-xiaohongshu-ops-delegation-example.json)。

## B站 (bilibili) 管线（openclaw-bilibili-fragment.json）

- **智能体**：bilibili 七件套（热门监控、内容助手、视频发布、数据助手、爆款拆解、写作、评论管理）；技能来自 [ClawHub bilibili](https://clawhub.ai/skills?sort=downloads&q=bilibili) 及 baoyu。
- **workspace 路径**：`~/.openclaw/workspace-bilibili-*`；部署时将仓库 `content-ops/bilibili/1-...`～`content-ops/bilibili/7-...` 复制或链接到对应路径。
- **技能安装**：`clawhub install <slug>`（如 bilibili-hot-monitor、bilibili-update-viewer、bilibili-helper、bilibili-subtitle-download-skill、bilibili-video-publish、bilibili-upload、bilibili-analytics）。投稿/发布类技能需浏览器登录或 B 站凭证，勿写入 TOOLS.md。详见 [content-ops/bilibili/README.md](../content-ops/bilibili/README.md)。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置；按需绑定渠道到对应 agent。

## 知乎管线（openclaw-zhihu-fragment.json）

- **智能体**：zhihu 七件套（爆款拆解、二创、自动发布、数据助手、热门监控、写作、评论管理）；技能以 skills.sh + baoyu 为主，发布可接 [social-push](https://github.com/jihe520/social-push)（知乎想法）。
- **workspace 路径**：`~/.openclaw/workspace-zhihu-*`；部署时将仓库 `content-ops/zhihu/1-...`～`content-ops/zhihu/7-...` 复制或链接到对应路径。
- **技能安装**：见 [content-ops/zhihu/README.md](../content-ops/zhihu/README.md)（含技能列表与安装方式）。勿在 TOOLS.md 存凭证。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置。

## 百家号管线（openclaw-baijiahao-fragment.json）

- **智能体**：baijiahao 七件套（爆款拆解、二创、自动发布、数据助手、热门监控、写作、评论管理）；技能以 baoyu 系列为主，发布需浏览器或百家号开放平台。
- **workspace 路径**：`~/.openclaw/workspace-baijiahao-*`；部署时将仓库 `content-ops/baijiahao/1-...`～`content-ops/baijiahao/7-...` 复制或链接到对应路径。
- **技能安装**：见 [content-ops/baijiahao/README.md](../content-ops/baijiahao/README.md)（含技能列表与安装方式）。勿在 TOOLS.md 存凭证。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置。

## 微博管线（openclaw-weibo-fragment.json）

- **智能体**：weibo 七件套（热门监控、爆款拆解、二创、自动发布、数据助手、写作、评论管理）；技能以 baoyu 系列为主，发布可接 baoyu-post-to-weibo 或 social-push。
- **workspace 路径**：`~/.openclaw/workspace-weibo-*`；部署时将仓库 `content-ops/weibo/1-...`～`content-ops/weibo/7-...` 复制或链接到对应路径。
- **技能安装**：见 [content-ops/weibo/README.md](../content-ops/weibo/README.md)（含技能列表与安装方式）。勿在 TOOLS.md 存凭证。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置。

## 视频号管线（openclaw-wechat-video-fragment.json）

- **智能体**：wechat-video 七件套（热门监控、爆款拆解、二创、自动发布、数据助手、写作、评论管理）；发布依赖视频号开放能力或浏览器自动化，技能以 baoyu 系列为主。
- **workspace 路径**：`~/.openclaw/workspace-wechat-video-*`；部署时将仓库 `content-ops/wechat-video/1-...`～`content-ops/wechat-video/7-...` 复制或链接到对应路径。
- **技能安装**：见 [content-ops/wechat-video/README.md](../content-ops/wechat-video/README.md)（含技能列表与安装方式）。勿在 TOOLS.md 存凭证。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置。

## 掘金管线（openclaw-juejin-fragment.json）

- **智能体**：juejin 七件套（热门监控、爆款拆解、二创、自动发布、数据助手、写作、评论管理）；技术内容向，技能以 baoyu 系列与 social-push 为主。
- **workspace 路径**：`~/.openclaw/workspace-juejin-*`；部署时将仓库 `content-ops/juejin/1-...`～`content-ops/juejin/7-...` 复制或链接到对应路径。
- **技能安装**：见 [content-ops/juejin/README.md](../content-ops/juejin/README.md)（含技能列表与安装方式）。勿在 TOOLS.md 存凭证。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置。

## 头条号管线（openclaw-toutiao-fragment.json）

- **智能体**：toutiao 七件套（热门监控、爆款拆解、二创、自动发布、数据助手、写作、评论管理）；发布需头条开放平台或浏览器，技能以 baoyu 系列为主。
- **workspace 路径**：`~/.openclaw/workspace-toutiao-*`；部署时将仓库 `content-ops/toutiao/1-...`～`content-ops/toutiao/7-...` 复制或链接到对应路径。
- **技能安装**：见 [content-ops/toutiao/README.md](../content-ops/toutiao/README.md)（含技能列表与安装方式）。勿在 TOOLS.md 存凭证。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置。

## 抖音管线（openclaw-douyin-fragment.json）

- **智能体**：douyin 七件套（热门监控、爆款拆解、二创、自动发布、数据助手、写作、评论管理）；短视频平台，技能以 baoyu 系列为主，发布需抖音开放平台 API 或浏览器，须遵守平台 ToS。
- **workspace 路径**：`~/.openclaw/workspace-douyin-*`；部署时将仓库 `content-ops/douyin/1-douyin-hot-monitor`～`content-ops/douyin/7-douyin-comment-manager` 复制或链接到对应路径。
- **技能安装**：见 [content-ops/douyin/README.md](../content-ops/douyin/README.md)（含技能列表与安装方式）、[content-ops/douyin/CLAWHUB-SKILLS.md](../content-ops/douyin/CLAWHUB-SKILLS.md)。勿在 TOOLS.md 存凭证。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置。

## 快手管线（openclaw-kuaishou-fragment.json）

- **智能体**：kuaishou 七件套（热门监控、爆款拆解、二创、自动发布、数据助手、写作、评论管理）；短视频平台，技能以 baoyu 系列为主，发布需快手开放平台 API 或浏览器，须遵守平台 ToS。
- **workspace 路径**：`~/.openclaw/workspace-kuaishou-*`；部署时将仓库 `content-ops/kuaishou/1-kuaishou-hot-monitor`～`content-ops/kuaishou/7-kuaishou-comment-manager` 复制或链接到对应路径。
- **技能安装**：见 [content-ops/kuaishou/README.md](../content-ops/kuaishou/README.md)（含技能列表与安装方式）、[content-ops/kuaishou/CLAWHUB-SKILLS.md](../content-ops/kuaishou/CLAWHUB-SKILLS.md)。勿在 TOOLS.md 存凭证。
- **合并方式**：将片段的 `agents.list`、`bindings`、`tools` 合并进主配置。

# Game Studio / 游戏工作室

> Game design, engine-specific engineers (Unity/Unreal/Godot/Roblox) and creative tools
>
> 游戏设计、引擎专家（Unity/Unreal/Godot/Roblox）及创意工具

## Agents / 智能体列表

| ID | Name | 中文名 | Sub-scenario | Role |
|---|---|---|---|---|
| blender-addon-engineer | Blender Add-on Engineer | Blender 插件工程师 | game-tools | undefined |
| game-audio-engineer | Game Audio Engineer | 游戏音频工程师 | art-tech-audio | undefined |
| game-designer | Game Designer | 游戏设计师 | game-design | undefined |
| godot-gameplay-scripter | Godot Gameplay Scripter | Godot 玩法脚本工程师 | godot | undefined |
| godot-multiplayer-engineer | Godot Multiplayer Engineer | Godot 多人联网工程师 | godot | undefined |
| godot-shader-developer | Godot Shader Developer | Godot 着色器开发者 | godot | undefined |
| level-designer | Level Designer | 关卡设计师 | game-design | undefined |
| narrative-designer | Narrative Designer | 叙事设计师 | game-design | undefined |
| roblox-avatar-creator | Roblox Avatar Creator | Roblox 形象创建者 | roblox | undefined |
| roblox-experience-designer | Roblox Experience Designer | Roblox 体验设计师 | roblox | undefined |
| roblox-systems-scripter | Roblox Systems Scripter | Roblox 系统脚本工程师 | roblox | undefined |
| technical-artist | Technical Artist | 技术美术师 | art-tech-audio | undefined |
| unity-architect | Unity Architect | Unity 架构师 | unity | undefined |
| unity-editor-tool-developer | Unity Editor Tool Developer | Unity 编辑器工具开发者 | unity | undefined |
| unity-multiplayer-engineer | Unity Multiplayer Engineer | Unity 多人联网工程师 | unity | undefined |
| unity-shader-graph-artist | Unity Shader Graph Artist | Unity Shader 图形艺术家 | unity | undefined |
| unreal-multiplayer-architect | Unreal Multiplayer Architect | Unreal 多人网络架构师 | unreal | undefined |
| unreal-systems-engineer | Unreal Systems Engineer | Unreal 系统工程师 | unreal | undefined |
| unreal-technical-artist | Unreal Technical Artist | Unreal 技术美术师 | unreal | undefined |
| unreal-world-builder | Unreal World Builder | Unreal 世界构建师 | unreal | undefined |

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

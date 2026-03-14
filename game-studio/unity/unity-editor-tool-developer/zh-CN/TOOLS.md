# TOOLS.md - 本地备注

技能定义工具的**工作方式**，此文件记录你的**具体配置**。

## 交付物

### Custom EditorWindow — Asset Auditor
```csharp
public class AssetAuditWindow : EditorWindow
{
    [MenuItem("Tools/Asset Auditor")]
    public static void ShowWindow() => GetWindow<AssetAuditWindow>("Asset Auditor");

    private Vector2 _scrollPos;
    private List<string> _oversizedTextures = new();
    private bool _hasRun = false;

    private void OnGUI()
    {
        GUILayout.Label("Texture Budget Auditor", EditorStyles.boldLabel);



_[truncated]_

## 工作流程

### 1. Tool Specification
- Interview the team: "What do you do manually more than once a week?" — that's the priority list
- Define the tool's success metric before building: "This tool saves X minutes per import/per review/per build"
- Identify the correct Unity Editor API: Window, Postprocessor, Validator, Drawer, or MenuItem?

### 2. Prototype First
- Build the fastest possible working version — UX polish comes after functionality is confirmed


_[truncated]_

## 输入 / 输出路径

- **输入：** _（填写：从哪里读取来源材料、报告或任务定义）_
- **输出：** _（填写：将交付物、日志或报告写入哪里）_

## 技能

按需安装适合此智能体任务的技能：

```bash
# 示例 — 替换为 Unity 编辑器工具开发者 实际所需的技能 slug
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## 备注

_在此添加特定环境配置、字段约定或 API 端点。不要存储凭证。_

# TOOLS.md - Unity Editor Tool Developer

Skills define _how_ tools work. This file is for _your_ specifics — setup unique to your agent.

## Deliverables

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

        if (GUILayout.Button("Scan Project Textures"))
        {
            _oversizedTextures.Clear();
            ScanTextures();


_[truncated]_

## Workflow

### 1. Tool Specification
- Interview the team: "What do you do manually more than once a week?" — that's the priority list
- Define the tool's success metric before building: "This tool saves X minutes per import/per review/per build"
- Identify the correct Unity Editor API: Window, Postprocessor, Validator, Drawer, or MenuItem?

### 2. Prototype First
- Build the fastest possible working version — UX polish comes after functionality is confirmed
- Test with the actual team member who will use the tool, not just the tool developer
- Note every point of confusion in the prototype test

### 3.

_[truncated]_



## Input / Output Paths

- **Input:** _(fill in: where to read source material, reports, or task definitions)_
- **Output:** _(fill in: where to write deliverables, logs, or reports)_

## Skills

Install skills relevant to this agent's tasks:

```bash
# Example — replace with actual skill slugs for Unity Editor Tool Developer
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## Notes

_Add environment-specific notes, field conventions, or API endpoints here. Do not store credentials._

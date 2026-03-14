# TOOLS.md - Unity Architect

Skills define _how_ tools work. This file is for _your_ specifics — setup unique to your agent.

## Deliverables

### FloatVariable ScriptableObject
```csharp
[CreateAssetMenu(menuName = "Variables/Float")]
public class FloatVariable : ScriptableObject
{
    [SerializeField] private float _value;

    public float Value
    {
        get => _value;
        set
        {
            _value = value;
            OnValueChanged?.Invoke(value);
        }
    }

    public event Action<float> OnValueChanged;

    public void SetValue(float value) => Value = value;
    public void ApplyChange(float amount) => Value += amount;
}
```

### RuntimeSet — Singleton-Free Entity Tracking
```csharp


_[truncated]_

## Workflow

### 1. Architecture Audit
- Identify hard references, singletons, and God classes in the existing codebase
- Map all data flows — who reads what, who writes what
- Determine which data should live in SOs vs. scene instances

### 2. SO Asset Design
- Create variable SOs for every shared runtime value (health, score, speed, etc.)
- Create event channel SOs for every cross-system trigger
- Create RuntimeSet SOs for every entity type that needs to be tracked globally
- Organize under `Assets/ScriptableObjects/` with subfolders by domain

### 3. Component Decomposition


_[truncated]_



## Input / Output Paths

- **Input:** _(fill in: where to read source material, reports, or task definitions)_
- **Output:** _(fill in: where to write deliverables, logs, or reports)_

## Skills

Install skills relevant to this agent's tasks:

```bash
# Example — replace with actual skill slugs for Unity Architect
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## Notes

_Add environment-specific notes, field conventions, or API endpoints here. Do not store credentials._

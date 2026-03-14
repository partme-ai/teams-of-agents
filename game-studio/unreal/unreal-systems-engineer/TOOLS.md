# TOOLS.md - Unreal Systems Engineer

Skills define _how_ tools work. This file is for _your_ specifics — setup unique to your agent.

## Deliverables

### GAS Project Configuration (.Build.cs)
```csharp
public class MyGame : ModuleRules
{
    public MyGame(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

        PublicDependencyModuleNames.AddRange(new string[]
        {
            "Core", "CoreUObject", "Engine", "InputCore",
            "GameplayAbilities",   // GAS core
            "GameplayTags",        // Tag system
            "GameplayTasks"        // Async task framework
        });

        PrivateDependencyModuleNames.AddRange(new string[]
        {


_[truncated]_

## Workflow

### 1. Project Architecture Planning
- Define the C++/Blueprint split: what designers own vs. what engineers implement
- Identify GAS scope: which attributes, abilities, and tags are needed
- Plan Nanite mesh budget per scene type (urban, foliage, interior)
- Establish module structure in `.Build.cs` before writing any gameplay code

### 2. Core Systems in C++
- Implement all `UAttributeSet`, `UGameplayAbility`, and `UAbilitySystemComponent` subclasses in C++
- Build character movement extensions and physics callbacks in C++


_[truncated]_



## Input / Output Paths

- **Input:** _(fill in: where to read source material, reports, or task definitions)_
- **Output:** _(fill in: where to write deliverables, logs, or reports)_

## Skills

Install skills relevant to this agent's tasks:

```bash
# Example — replace with actual skill slugs for Unreal Systems Engineer
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## Notes

_Add environment-specific notes, field conventions, or API endpoints here. Do not store credentials._

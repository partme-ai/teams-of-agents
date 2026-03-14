# TOOLS.md - Unreal World Builder

Skills define _how_ tools work. This file is for _your_ specifics — setup unique to your agent.

## Deliverables

### World Partition Setup Reference
```markdown

## Workflow

### 1. World Scale and Grid Planning
- Determine world dimensions, biome layout, and point-of-interest placement
- Choose World Partition grid cell sizes per content layer
- Define the Always Loaded layer contents — lock this list before populating

### 2. Landscape Foundation
- Build Landscape with correct resolution for the target size
- Author master Landscape material with layer slots defined, RVT enabled
- Paint biome zones as weight layers before any props are placed

### 3. Environment Population
- Build PCG graphs for large-scale population; use Foliage Tool for hero asset placement


_[truncated]_



## Input / Output Paths

- **Input:** _(fill in: where to read source material, reports, or task definitions)_
- **Output:** _(fill in: where to write deliverables, logs, or reports)_

## Skills

Install skills relevant to this agent's tasks:

```bash
# Example — replace with actual skill slugs for Unreal World Builder
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## Notes

_Add environment-specific notes, field conventions, or API endpoints here. Do not store credentials._

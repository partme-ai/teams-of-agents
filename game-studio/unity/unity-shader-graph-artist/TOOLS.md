# TOOLS.md - Unity Shader Graph Artist

Skills define _how_ tools work. This file is for _your_ specifics — setup unique to your agent.

## Deliverables

### Dissolve Shader Graph Layout
```
Blackboard Parameters:
  [Texture2D] Base Map        — Albedo texture
  [Texture2D] Dissolve Map    — Noise texture driving dissolve
  [Float]     Dissolve Amount — Range(0,1), artist-driven
  [Float]     Edge Width      — Range(0,0.2)
  [Color]     Edge Color      — HDR enabled for emissive edge

Node Graph Structure:
  [Sample Texture 2D: DissolveMap] → [R channel] → [Subtract: DissolveAmount]
  → [Step: 0] → [Clip]  (drives Alpha Clip Threshold)

  [Subtract: DissolveAmount + EdgeWidth] → [Step] → [Multiply: EdgeColor]
  → [Add to Emission output]



_[truncated]_

## Workflow

### 1. Design Brief → Shader Spec
- Agree on the visual target, platform, and performance budget before opening Shader Graph
- Sketch the node logic on paper first — identify major operations (texturing, lighting, effects)
- Determine: artist-authored in Shader Graph, or performance-requires HLSL?

### 2. Shader Graph Authorship
- Build Sub-Graphs for all reusable logic first (fresnel, dissolve core, triplanar mapping)
- Wire master graph using Sub-Graphs — no flat node soups
- Expose only what artists will touch; lock everything else in Sub-Graph black boxes

### 3.

_[truncated]_



## Input / Output Paths

- **Input:** _(fill in: where to read source material, reports, or task definitions)_
- **Output:** _(fill in: where to write deliverables, logs, or reports)_

## Skills

Install skills relevant to this agent's tasks:

```bash
# Example — replace with actual skill slugs for Unity Shader Graph Artist
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## Notes

_Add environment-specific notes, field conventions, or API endpoints here. Do not store credentials._

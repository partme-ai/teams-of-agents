# TOOLS.md - Carousel Growth Engine

Skills define _how_ tools work. This file is for _your_ specifics — setup unique to your agent.

## Deliverables

### Website Analysis Output (`analysis.json`)
- Complete brand extraction: name, logo, colors, typography, favicon
- Content analysis: headline, tagline, features, pricing, testimonials, stats, CTAs
- Internal page navigation: pricing, features, about, testimonials pages
- Competitor detection from website content (20+ known SaaS competitors)
- Business type and niche classification
- Niche-specific hooks and pain points
- Visual context definition for slide generation

### Carousel Generation Output
- 6 visually coherent JPG slides (768x1376, 9:16 ratio) via Gemini


_[truncated]_

## Workflow

### Phase 1: Learn from History
1. **Fetch Analytics**: Call Upload-Post analytics endpoints for profile metrics and per-post performance via `check-analytics.sh`
2. **Extract Insights**: Run `learn-from-analytics.js` to identify best-performing hooks, optimal posting times, and engagement patterns
3. **Update Learnings**: Accumulate insights into `learnings.json` persistent knowledge base
4. **Plan Next Carousel**: Read `learnings.json`, pick hook style from top performers, schedule at optimal time, apply recommendations

### Phase 2: Research & Analyze
1.

_[truncated]_



## Input / Output Paths

- **Input:** _(fill in: where to read source material, reports, or task definitions)_
- **Output:** _(fill in: where to write deliverables, logs, or reports)_

## Skills

Install skills relevant to this agent's tasks:

```bash
# Example — replace with actual skill slugs for Carousel Growth Engine
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## Notes

_Add environment-specific notes, field conventions, or API endpoints here. Do not store credentials._

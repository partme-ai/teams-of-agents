# TOOLS.md - Inclusive Visuals Specialist

Skills define _how_ tools work. This file is for _your_ specifics — setup unique to your agent.

## Deliverables

Concrete examples of what you produce:
- Annotated Prompt Architectures (breaking prompts down by Subject, Action, Context, Camera, and Style).
- Explicit Negative-Prompt Libraries for both Image and Video platforms.
- Post-Generation Review Checklists for UX researchers.

### Example Code: The Dignified Video Prompt
```typescript
// Inclusive Visuals Specialist: Counter-Bias Video Prompt
export function generateInclusiveVideoPrompt(subject: string, action: string, context: string) {
  return `


_[truncated]_

## Workflow

1. **Phase 1: The Brief Intake:** Analyze the requested creative brief to identify the core human story and the potential systemic biases the AI will default to.
2. **Phase 2: The Annotation Framework:** Build the prompt systematically (Subject -> Sub-actions -> Context -> Camera Spec -> Color Grade -> Explicit Exclusions).
3. **Phase 3: Video Physics Definition (If Applicable):** For motion constraints, explicitly define temporal consistency (how light, fabric, and physics behave as the subject moves).
4.

_[truncated]_



## Input / Output Paths

- **Input:** _(fill in: where to read source material, reports, or task definitions)_
- **Output:** _(fill in: where to write deliverables, logs, or reports)_

## Skills

Install skills relevant to this agent's tasks:

```bash
# Example — replace with actual skill slugs for Inclusive Visuals Specialist
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## Notes

_Add environment-specific notes, field conventions, or API endpoints here. Do not store credentials._

# TOOLS.md - 本地备注

技能定义工具的**工作方式**，此文件记录你的**具体配置**。

## 交付物

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

## 工作流程

1. **Phase 1: The Brief Intake:** Analyze the requested creative brief to identify the core human story and the potential systemic biases the AI will default to.
2. **Phase 2: The Annotation Framework:** Build the prompt systematically (Subject -> Sub-actions -> Context -> Camera Spec -> Color Grade -> Explicit Exclusions).
3.

_[truncated]_

## 输入 / 输出路径

- **输入：** _（填写：从哪里读取来源材料、报告或任务定义）_
- **输出：** _（填写：将交付物、日志或报告写入哪里）_

## 技能

按需安装适合此智能体任务的技能：

```bash
# 示例 — 替换为 包容性视觉专家 实际所需的技能 slug
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## 备注

_在此添加特定环境配置、字段约定或 API 端点。不要存储凭证。_

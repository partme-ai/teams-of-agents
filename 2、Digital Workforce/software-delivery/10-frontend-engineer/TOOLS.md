# TOOLS.md - 前端工程师本地与技能备注

本文件用于：环境与构建偏好、**前端智能体所需技能**及安装命令。技能定义见各 SKILL.md；此处仅列推荐清单与安装方式。

---

## 前端智能体所需技能

### 一、full-stack-skills（优先）

通过 Cursor/Claude 插件或工作区引用 [full-stack-skills](https://github.com/partme-ai/full-stack-skills)，按插件类别安装即可。

| 能力 | 技能名 | 插件类别 |
|------|--------|----------|
| 框架与构建 | vue3, react, vite, nextjs, pinia, webpack, rollup | development-skills |
| UI 组件库 | element-plus-vue3, ant-design-vue, vant-vue3, ant-design-react | development-skills |
| 测试 | playwright, vitest, jest | testing-skills |
| 设计协作 | frontend-design | development-skills-utils |

**安装示例（插件级）：** `/plugin install development-skills@full-stack-skills`、`/plugin install testing-skills@full-stack-skills`。

### 二、skills.sh 前端技能（可选补充）

来源：[skills.sh ?q=frontend](https://skills.sh/?q=frontend)。与 full-stack-skills 同能力可二选一或并存。

| 技能名 | 仓库 | 安装量 | 用途 |
|--------|------|--------|------|
| frontend-design | anthropics/skills | 152.9K | 前端设计与高质量 UI（首选） |
| frontend-design-system | supercent-io/skills-template | 7.7K | 设计系统与组件规范 |
| frontend-code-review | langgenius/dify | 2.4K | 前端代码评审 |
| frontend-patterns | affaan-m/everything-claude-code | 2.0K | 前端模式与最佳实践 |
| frontend-testing | langgenius/dify | 1.4K | 前端测试 |
| frontend-testing-best-practices | sergiodxa/agent-skills | 1.4K | 前端测试最佳实践 |
| frontend responsive design standards | am-will/codex-skills | 1.2K | 响应式设计标准 |
| vercel-microfrontends | vercel/microfrontends | 21 | 微前端 |
| frontend-ui-ux-engineer | 404kidwiz/claude-supercode-skills | 1.0K | 前端 UI/UX 工程 |

**安装命令（复制执行）：**

```bash
# 首选：前端设计（anthropics，安装量最高）
npx skills add anthropics/skills --skill frontend-design -y -g

# 设计系统
npx skills add supercent-io/skills-template --skill frontend-design-system -y -g

# 前端代码评审
npx skills add langgenius/dify --skill frontend-code-review -y -g

# 前端模式与最佳实践
npx skills add affaan-m/everything-claude-code --skill frontend-patterns -y -g

# 前端测试最佳实践
npx skills add sergiodxa/agent-skills --skill frontend-testing-best-practices -y -g

# 前端测试
npx skills add langgenius/dify --skill frontend-testing -y -g

# 响应式设计标准（技能名含空格，以仓库实际标识为准）
npx skills add am-will/codex-skills --skill "frontend responsive design standards" -y -g

# 微前端
npx skills add vercel/microfrontends --skill vercel-microfrontends -y -g

# 前端 UI/UX 工程
npx skills add 404kidwiz/claude-supercode-skills --skill frontend-ui-ux-engineer -y -g
```

**说明：** 同质能力（如多个 frontend-design）只装一个时优先选 `anthropics/skills`。安装后技能名需与 OpenClaw config 中该 agent 的 `skills` 数组一致。

---

## 本地与环境备注

以下为**你当前环境**的偏好或约定，按需填写：

- **构建与框架：** 如 Vite / Webpack、Vue 3 / React、Next 等
- **UI 库与设计系统：** 如 Element Plus、Ant Design、Tailwind、Storybook
- **测试与 CI：** 如 Vitest、Playwright、Jest、CI 脚本路径
- **其它：** SSH、代理、内网 npm 源、预览地址等

---

Add whatever helps you do your job. This is your cheat sheet.

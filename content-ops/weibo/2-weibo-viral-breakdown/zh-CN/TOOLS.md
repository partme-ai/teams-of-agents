# TOOLS.md - 本地备注

技能定义工具行为；本文件记录你的具体配置。

## 拆解框架结构

输出拆解时保持以下字段一致，供二创与数据助手使用：

- **title** / 标题
- **hook** / 钩子
- **structure** / 结构
- **theme** / 主题

## 可写内容

- 微博搜索源或抓取方式（Playwright/Firecrawl 或 baoyu-url-to-markdown）
- 拆解报告输出路径（如 `breakdowns/`）
- 行业关键词与话题列表
- 与二创、数据助手的交接路径

## 推荐技能

- **baoyu-url-to-markdown**：将微博 URL 抓取为 Markdown。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown`。
- **baoyu-format-markdown**：规范拆解报告格式。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown`。

安装：`npx skills add <owner/repo> --skill <技能名>`（skills.sh）或 `clawhub install <slug>`（ClawHub）。技能列表见本平台 README。勿在此存储凭证。

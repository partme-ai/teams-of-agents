# TOOLS.md - 本地备注

技能定义工具行为；本文件记录你的具体配置。

## 可写内容

- 公众号/微信热点搜索源或 API（Playwright / Firecrawl / wechat-article-extractor 等）
- 日报或按需报告输出路径（如 `reports/`、`hot-daily/`）
- 行业关键词与话题列表
- 与爆款拆解、数据助手的交接路径
- 报告格式（字段：趋势话题、爆款文章 ID/URL、摘要统计）

## 技能（ClawHub 为主，skills.sh 后补）

- **ClawHub**：在 [clawhub.ai/skills?q=wechat](https://clawhub.ai/skills?sort=downloads&q=wechat) 搜索公众号监控/搜索类技能。
- **skills.sh**：**baoyu-url-to-markdown** 抓取链接成文；**baoyu-format-markdown** 规范报告格式。安装：`npx skills add <owner/repo> --skill <技能名>`（skills.sh）或 `clawhub install <slug>`（ClawHub）。技能列表见本平台 README。

勿在此存储凭证。

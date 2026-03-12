# TOOLS.md - 本地备注

技能定义工具**怎么用**。本文件写**你这边**的配置与约定。

## 拆解框架约定结构

产出拆解时使用一致、可复用字段，便于二创与数据助手消费：

- **title** / 标题
- **hook** / 钩子
- **outline** / 大纲
- **theme** / 主题
- **format** / 形式（如 list、story、before-after）

## 可写内容

- 搜索接口或来源（公众号 / wechat-article-extractor / 爬虫等）
- 拆解输出路径（如 `breakdowns/`）
- 行业关键词与主题列表
- 与二创、数据助手的交接路径或约定

## 推荐/已配置技能

- **wechat-article-extractor**（ClawHub）：公众号文章提取为 Markdown；支持镜像站与反爬。安装：`clawhub install wechat-article-extractor`（以 clawhub.ai 为准）。
- **baoyu-format-markdown**（skills.sh）：规范拆解报告格式。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown` 或按 skills.sh。

---

按需补充。本文件不存凭证。

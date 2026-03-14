# TOOLS.md - 本地备注

技能定义工具**怎么用**。本文件写**你这边**的配置与备注。

## 可写内容

- 草稿来源路径（来自二创）
- 发布接口或工具说明（不写明文密钥；用环境变量）
- 数据助手用发布日志路径（如 `publish-logs/`）
- 限流与排期规则
- 与数据助手的交接格式

## 技能（ClawHub 优先，skills.sh 后补）

- **ClawHub（优先）**：在 [clawhub.ai/skills?q=xiaohongshu](https://clawhub.ai/skills?sort=downloads&q=xiaohongshu) 搜索小红书发布相关技能，若有则 `clawhub install <技能名>`，并加入本 agent 的 `skills` 配置。
- **skills.sh（后补）**：
  - **baoyu-compress-image**：发布前对图片做压缩（WebP/PNG），减小体积、加快上传。安装：`npx skills add jimliu/baoyu-skills --skill baoyu-compress-image`。具体发布动作（小红书/脚本/第三方工具）以本文件配置为准。

---

按需补充。本文件不存凭证。

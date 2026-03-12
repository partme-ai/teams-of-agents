# TOOLS.md - 本地备注

技能定义工具**怎么用**。本文件写**你这边**的配置与约定。

## 草稿与发布日志的衔接

每条发布记录使用一致字段，供数据助手解析，例如：

- postId、时间、状态（成功/失败）、链接、错误（若有）、可选阅读/点赞等

日志存放路径与格式在此约定（如 `publish-logs/`），便于数据助手拉取。

## 可写内容

- 草稿输入路径（来自二创）
- 发布日志输出路径（如 `publish-logs/`）
- API/CDP 或账号配置引用（不写凭证；用环境变量或 EXTEND.md）

## 推荐/已配置技能

- **wechat-ai-publisher**（ClawHub）：自动发文（写稿、排版、封面、草稿）。安装：`clawhub install wechat-ai-publisher`（以 clawhub.ai 为准）。
- **baoyu-post-to-wechat**（skills.sh）：发布到公众号。
- **baoyu-markdown-to-html**（skills.sh）：MD 转微信 HTML。
- **baoyu-compress-image**（skills.sh）：发布前压缩图片。

---

本文件不存凭证。

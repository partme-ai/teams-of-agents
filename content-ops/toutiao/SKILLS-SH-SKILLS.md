# skills.sh 头条号相关技能一览

> 来源：[skills.sh/?q=baoyu](https://skills.sh/?q=baoyu)。安装方式：`npx skills add <owner/repo> --skill <技能名>`。与 [CLAWHUB-SKILLS.md](./CLAWHUB-SKILLS.md) 并列。头条号发布需开放平台或浏览器，当前以 baoyu 配图/抓取为主。

## Baoyu 系列（jimliu/baoyu-skills）本管线可用

| 技能名 | 本管线适用（agent / 用途） |
|--------|----------------------------|
| baoyu-url-to-markdown | hot-monitor、viral-breakdown：抓取链接成文 |
| baoyu-format-markdown | viral-breakdown、data-assistant：报告格式 |
| baoyu-cover-image | rewrite、write：封面 |
| baoyu-article-illustrator | rewrite、write：配图 |
| baoyu-compress-image | publisher：发布前压缩 |

## 安装方式（skills.sh）

```bash
npx skills add jimliu/baoyu-skills --skill baoyu-url-to-markdown
npx skills add jimliu/baoyu-skills --skill baoyu-format-markdown
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image
npx skills add jimliu/baoyu-skills --skill baoyu-article-illustrator
npx skills add jimliu/baoyu-skills --skill baoyu-compress-image
```

安装后技能目录名需与 config 中 `skills` 一致。**勿在 TOOLS.md 存凭证。**

### 更新
- 重新执行 `npx skills add <owner/repo> --skill <技能名>` 覆盖安装即可；或以 skills.sh CLI 文档为准。

### 卸载
- **命令**：`npx skills remove <技能名>`（技能名与安装后目录名一致）
- 或手动删除：项目安装为 `./.skills/<技能名>`，全局安装为 `~/.skills/<技能名>`。

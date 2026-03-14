# 内容运营管线 (Content-Ops)

> 统一内容管线七件套：热门监控、爆款拆解、二创/原创、自动发布、数据助手、评论管理。按渠道分目录部署（公众号、小红书、抖音、B 站等），技能以 **ClawHub（SkillHub）为主、skills.sh 取最优**。

## 渠道目录

| 渠道 | 目录 | 说明 |
|------|------|------|
| 公众号 | [wechat-article](./wechat-article/) | 微信公众号文章管线 |
| 小红书 | [xiaohongshu](./xiaohongshu/) | 小红书内容管线 |
| 抖音 | [douyin](./douyin/) | 抖音短视频管线 |
| B站 | [bilibili](./bilibili/) | B 站视频管线 |
| 微博 | [weibo](./weibo/) | 微博管线 |
| 知乎 | [zhihu](./zhihu/) | 知乎管线 |
| 头条号 | [toutiao](./toutiao/) | 头条号管线 |
| 快手 | [kuaishou](./kuaishou/) | 快手管线 |
| 掘金 | [juejin](./juejin/) | 掘金管线 |
| 视频号 | [wechat-video](./wechat-video/) | 微信视频号管线 |
| 百家号 | [baijiahao](./baijiahao/) | 百家号管线 |

各渠道技能列表与评估见对应目录下 `README.md`、`CLAWHUB-SKILLS.md`、`SKILLS-EVALUATION.md`。

---

## 技能安装（ClawHub / SkillHub）

使用 ClawHub 安装技能时，按以下两步执行。

**第一步：安装 SkillHub CLI**

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

**第二步：安装技能**

按渠道进入对应目录，执行该渠道 README 或 SKILLS-EVALUATION 中的 `clawhub install ...` 命令。示例（小红书）：

```bash
clawhub search xiaohongshu
clawhub install xiaohongshu-mcp --workdir ~/.openclaw;
clawhub install xiaohongshu-cn --workdir ~/.openclaw;
# … 其余见 xiaohongshu/README.md 或 xiaohongshu/SKILLS-EVALUATION.md
```


```bash
npx skills add https://github.com/anthropics/skills --skill pdf -y -g;
npx skills add https://github.com/anthropics/skills --skill pptx -y -g;
npx skills add https://github.com/anthropics/skills --skill docx -y -g;
npx skills add https://github.com/anthropics/skills --skill xlsx -y -g;
```



其他渠道见各目录 `README.md` 的「安装命令」小节。

**命令规范**：`clawhub install` 须带 `--workdir ~/.openclaw` 且以 `;` 结尾；`clawhub uninstall`、`npx skills remove` 须以 `;` 结尾；`npx skills add` 须以 `-y -g;` 结尾。

# ClawHub 抖音相关技能一览

> 来源：[ClawHub — 按 douyin 搜索](https://clawhub.ai/skills?sort=downloads&q=douyin)。安装方式：`clawhub install <slug> --workdir ~/.openclaw;`。若当前无或较少，以本目录 README 下方技能表与 baoyu 系列为主；安装：`npx skills add <owner/repo> --skill <名>`。发布与抓取须遵守抖音开放平台与平台 ToS。

## 技能总表（按下载量排序）

| # | Slug | 名称/功能摘要 | 作者 | 下载 | ★ | v |
|---|------|----------------|------|------|---|---|
| 1 | douyin-hot-trend | 抖音热榜/热搜榜：热门视频、挑战赛、音乐等，输出标题、热度、链接、封面 | franklu0819-lang | 2.9k | 11 | 3 |
| 2 | douyin-publish | 自动登录抖音、上传发布视频到创作者平台，支持标签管理与登录状态检查 | gonghaiquan | 2.3k | 10 | 1 |
| 3 | douyin-downloader | 抖音视频下载（链接或 modal_id 解析，稳定无水印） | valderwu3 | 1.9k | 4 | 1 |
| 4 | douyin-video-fetch | 下载抖音视频到本地（无水印优先），支持 URL/video_id/批量，供分析/复刻 | KAMIENDER | 1.7k | 8 | 1 |
| 5 | taobao | 淘宝/京东/拼多多/抖音/快手比价与优惠券（含抖音商品比价） | al-one | 1.5k | 6 | 3 |
| 6 | douyin-download | 抖音无水印视频下载与文案提取 | whille | 573 | 3 | 4 |
| 7 | douyin-keyword-search | 关键词搜索抓取抖音结果页数据，支持格式与数量限制（需 Playwright/Chromium） | urhd528 | 470 | 0 | 1 |
| 8 | douyin-messager | 抖音私信：浏览器自动化发送私信、获取聊天记录 | Moroiser | 447 | 3 | 3 |
| 9 | douyin-video-downloader | 抖音视频下载（第三方解析，无水印） | ansonlianson | 443 | 1 | 2 |
| 10 | douyin-downloader-nodejs | 抖音无水印视频下载与文案提取（Node.js） | whille | 318 | 2 | 1 |
| 11 | auto-publisher | 多平台视频自动发布：抖音、视频号、小红书、B 站、YouTube 等批量发布 | 954215110 | 313 | 0 | 1 |
| 12 | douyin-video-publish | 抖音视频发布：浏览器自动化在创作者平台发布视频 | Johnnyxu820 | 267 | 1 | 1 |
| 13 | save-douyin-video-to-feishu-drive | 从抖音链接解析视频直链/标题/描述，下载到本地或上传飞书云盘 | kuaner | 247 | 1 | 1 |
| 14 | video-crawler | 从抖音、Twitter 等按平台与 URL 提取并下载视频 | ly5201314gjx | 243 | 0 | 1 |
| 15 | douyin-download-v2 | 抖音无水印视频下载与文案提取（语义分段） | whille | 233 | 0 | 1 |
| 16 | lgcapture | 从抖音短链/标准链/分享链解析视频 ID，模拟 iPhone 浏览器下载 | ly5201314gjx | 204 | 0 | 1 |
| 17 | douyin-to-photos | 通过 Apple Shortcuts 将抖音分享链解析为无水印 MP4 并保存 | vahnxu | 144 | 0 | 1 |
| 18 | douyin-upload-skill | 登录并发布抖音视频（本地文件），OAuth、语音转文字、文案草稿 | YJLi-new | 136 | 0 | 1 |
| 19 | douyin-video-analyst | 账号视频批量采集与文案分析（抓取列表、语音转文字、总结归纳） | fishisnow | 129 | 0 | 2 |
| 20 | douyin-transcribe-skill | 抖音视频智能助手：链接/文件转录与智能处理（总结/逐字稿/归档） | junweiren98-rgb | 81 | 0 | 2 |
| 21 | douyin-transcribe | 抖音视频转文字：链接/文件转录为带标点中文文本 | junweiren98-rgb | 80 | 0 | 2 |
| 22 | dy-video-to-text | 抖音视频语音转文字、无水印下载链接与下载 | hljwwyy123 | 57 | 0 | 1 |
| 23 | douyin | 抖音原生流量结构诊断：前 3 秒钩子、留存摩擦、复播与推荐优化 | AGImodel | 49 | 0 | 1 |
| 24 | fast-douyin-publish | 抖音视频自动发布：一键上传、自动文案与标签优化 | DeadLining | 38 | 1 | 1 |
| 25 | douyin-video-download | 抖音视频批量下载：单条/批量、去重、无水印，yt-dlp/Playwright 择优 | franklu0819-lang | 28 | 0 | 1 |
| 26 | douyin-dl | 从抖音 URL（直链/搜索页 modal_id/分享链/note）下载短视频 | lskun | 0 | 0 | 1 |

*安装时以 ClawHub 当前 slug 为准；发布与抓取须遵守抖音开放平台与平台 ToS。*

## 推荐安装清单

本渠道**能用上的全要**时，以 [SKILLS-EVALUATION.md §6.3](./SKILLS-EVALUATION.md) 及 [README 全部安装/全部卸载](./README.md) 为准。ClawHub 段：douyin-hot-trend、douyin-downloader、douyin-publish；skills.sh 段见 6.3。

## 安装、更新与卸载

### 安装
- **搜索**：ClawHub 查看 douyin 最新技能。
- **命令**：`clawhub install <slug> --workdir ~/.openclaw;`
- 安装后技能目录名需与 config 中 `agents.list[].skills` 一致。
- **skills.sh**：安装：`npx skills add <owner/repo> --skill <名>`；技能列表见下方。**勿在 TOOLS.md 存凭证。** 合规与 ToS 见平台文档。

### 更新
- 重新执行 `clawhub install <slug> --workdir ~/.openclaw;` 覆盖安装即可；具体以 ClawHub CLI 文档为准。

### 卸载
- **命令**：`clawhub uninstall <slug>;`
- 或手动删除 ClawHub 技能目录下对应技能文件夹（目录名一般为 slug）。

### 各技能安装与卸载命令

上表「技能总表」中每个 Slug：**安装** `clawhub install <slug> --workdir ~/.openclaw;`，**卸载** `clawhub uninstall <slug>;`。示例：`clawhub install douyin-hot-trend --workdir ~/.openclaw;` / `clawhub uninstall douyin-hot-trend;`；其余将 `<slug>` 替换为表中对应 Slug 即可。

# HEARTBEAT.md

# 留空或仅保留注释即跳过心跳 API 调用。

# 需要周期性检查时在下方添加任务。
# OpenClaw 运维助手可选任务：未经用户同意不执行 CLI 或修改配置；无事可做时回复 HEARTBEAT_OK。
# - 浏览 https://docs.openclaw.ai/llms.txt 是否有新增/重命名路径（CLI、Gateway、插件、渠道）。
# - 若 MEMORY 中记录了重复故障，为每条补充一条官方文档链接（不代用户执行 doctor/logs）。

---

## 任务模板（可选）

以下为可复用的心跳任务描述，按需复制并填写后使用：

- **文档同步：** 拉取 `https://docs.openclaw.ai/llms.txt`，对比上次记录；若有与用户环境相关的页面变更（如 Gateway/Channels/Install），在 MEMORY 或 TOOLS 中记一笔。
- **故障沉淀：** 将近期排障结论（现象、原因、步骤）简要写入 `memory/YYYY-MM-DD.md` 或 MEMORY.md，便于后续同类问题快速参考。
- **环境校验：** 若 MEMORY 中记录了用户 Gateway URL、通道类型或提供商，检查是否有官方文档更新可能影响该配置；有则准备一句简短提醒（不主动执行变更）。

**何时主动触达：** 文档或环境变更影响对方时；有可复用的排障结论可分享时。  
**何时保持安静：** 深夜除非紧急；无新事；刚在 30 分钟内检查过。回复 `HEARTBEAT_OK` 即可。

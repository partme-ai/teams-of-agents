# USER.md

记录你正在服务的对象（团队、渠道或角色），由 configurer 填写。

## Channel-injected current user

当对话通过渠道接入（如 WeCom、Feishu、Telegram）时，网关或适配器可能会在会话上下文注入当前对话方信息。若已注入，以该信息为准；若缺失，先询问称呼，再写入此处或长期记忆。

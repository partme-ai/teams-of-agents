# USER.md

记录你正在服务的对象（团队、渠道或角色），由配置者填写。

## Channel-injected current user

当会话来自渠道（如 WeCom、Feishu、Telegram）时，网关或适配器可能会注入当前对话方信息。若存在该信息，应将其视为当前用户的权威来源；若缺失，先询问对方希望如何称呼，再写入此处或记忆中。

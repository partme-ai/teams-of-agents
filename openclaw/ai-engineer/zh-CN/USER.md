# USER.md

记录你正在支持的对象（团队、渠道或角色），由配置者按需补充。

## Channel-injected current user

当会话通过渠道接入（例如 WeCom、Feishu、Telegram）时，网关或适配器可能会注入当前对话方信息。若上下文已提供该信息，视为当前用户主信息源；若缺失，先询问称呼并写入此处或记忆系统。

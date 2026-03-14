# USER.md

记录你正在服务的对象（团队、渠道或角色），由 configurer 填写。

## Channel-injected current user

当对话通过渠道（如企微、飞书、Telegram）进入时，网关或适配器可能会在会话上下文注入当前对话人信息。若存在该信息，优先视为当前用户身份来源；若不存在，再询问称呼并写入本文件或 memory。

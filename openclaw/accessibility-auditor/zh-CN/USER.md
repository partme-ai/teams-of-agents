# USER.md

记录你正在服务的对象（团队、渠道或角色），由配置者维护。

## Channel-injected current user

当对话通过渠道（如 WeCom、Feishu、Telegram）进入时，网关或适配器可能会在会话上下文注入当前对话人信息。若存在该信息，优先作为当前会话身份来源；若不存在，再询问称呼并写入本文件或 memory。

# USER.md

记录你正在服务的对象（团队、渠道或角色），由配置者填写。

## Channel-injected current user

当会话 **通过渠道**（例如 WeCom、Feishu、Telegram）进入时，网关或适配器可能会将**当前对话对象**信息注入上下文。若存在，以其为准；若缺失，先询问对方称呼，再写入此文件或记忆中。

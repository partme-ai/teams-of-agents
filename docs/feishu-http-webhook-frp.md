# 飞书 HTTP 回调（webhook）+ frp 配置说明

当 main 智能体的飞书从 WebSocket 改为 **HTTP 回调**，并使用 frp 外网穿透（如 `http://124.221.173.158:18790/feishu/events`）时，若飞书报错 **「返回数据不是合法的JSON格式」**，按以下步骤排查与配置。

## 原因简述

- 飞书要求：对 `POST /feishu/events` 的响应必须是 **JSON**（URL 校验返回 `{"challenge":"..."}`，事件返回 `{"code":0}`），且 `Content-Type: application/json`。
- 若 frp 把公网端口转到 **Gateway 端口**，但当前运行的 OpenClaw **未在 Gateway 上注册 `/feishu/events`**（例如使用了旧版本，或配置了 `webhookPort` 导致走了独立端口），请求会落到 Gateway 的 404，返回 HTML/文本，飞书就会报「返回数据不是合法的JSON格式」。

## 推荐配置（回调走 Gateway + frp）

### 1. openclaw 配置（main 账号用 HTTP 回调）

在 `~/.openclaw/openclaw.json` 的 `channels.feishu` 中：

- 设置 **HTTP 模式**：`connectionMode: "webhook"`。
- 设置 **verificationToken**：在飞书开放平台该应用的「事件订阅」里可看到，必填。
- **不要设置** `webhookPort`（删掉或留空）。这样 feishu 插件会在 **Gateway 上**注册 `/feishu/events`，而不是单独起 3000 端口。

示例（仅保留相关片段）：

```json
"channels": {
  "feishu": {
    "enabled": true,
    "connectionMode": "webhook",
    "verificationToken": "你的飞书事件订阅 Verification Token",
    "webhookPath": "/feishu/events",
    "accounts": {
      "main": {
        "appId": "cli_xxx",
        "appSecret": "xxx",
        "botName": "助理-PartMe.AI",
        "connectionMode": "webhook"
      }
    }
  }
}
```

注意：**不要**在 `channels.feishu` 或 `accounts.main` 里写 `webhookPort`，否则会走独立端口，frp 若转的是 Gateway 端口就收不到回调。

### 2. frp 配置

将公网 `124.221.173.158:18790` 映射到本机 **Gateway 端口**（与 `gateway.port` 一致，例如 18789）：

- **frp 服务端**：`remote_port = 18790`（或你已用的公网端口）。
- **frp 客户端**：`local_ip = 127.0.0.1`，`local_port = 18789`（即 `gateway.port`）。

这样 `http://124.221.173.158:18790/feishu/events` 的请求会到达 Gateway，由 feishu 插件处理并返回合法 JSON。

### 3. 飞书开放平台

- 请求地址填：`http://124.221.173.158:18790/feishu/events`。
- 保存时飞书会做 URL 校验（POST 带 `challenge`），此时应由 Gateway 把请求交给 feishu，返回 `{"challenge":"..."}`，且 `Content-Type: application/json`。

### 4. gateway.port 与 gateway.bind

- `gateway.port`：与 frp 的 `local_port` 一致（如 18789）。
- `gateway.bind`：若为 `loopback`（只监听 127.0.0.1），frp 客户端需跑在**同一台机器**上，转发到 `127.0.0.1:gateway.port`。

## 为何返回 "no undefined event handle"

该文案来自 **飞书官方 Node SDK**（`@larksuiteoapi/node-sdk`）：当请求体中的**事件类型**解析不到（为 `undefined`）时，SDK 会返回这句话，表示「没有对应类型的事件处理器」。

常见原因：

1. **用浏览器直接打开** `http://124.221.173.158:18791/feishu/events`：这是 **GET** 请求，没有 body，SDK 拿不到 `type`，就会返回 "no undefined event handle"。属于正常现象，**飞书校验只会发 POST**。
2. **POST 请求体未正确传到处理逻辑**：frp 或 Gateway 若没有把 POST 的 body 原样转发，或上游已把 body 读掉未再传给 feishu 插件，SDK 收到的 body 为空/无效，`type` 为 undefined，也会出现该提示。
3. **飞书保存请求地址时仍报错**：说明飞书发出的 POST（带 `{"type":"url_verification","challenge":"..."}`）没有完整到达 feishu 的 webhook 处理函数，需检查 frp/Gateway 是否正确转发 **POST body** 和 **Content-Type: application/json**。

**建议自测**（在配置好且网关运行的前提下）：

```bash
# 应返回 JSON，且 body 中含 challenge（与请求里的一致）
curl -s -X POST http://124.221.173.158:18791/feishu/events \
  -H "Content-Type: application/json" \
  -d '{"type":"url_verification","challenge":"test123"}' 
```

若 curl 能收到 `{"challenge":"test123"}`，说明路径与 body 转发正常，飞书保存请求地址时应能通过校验；若仍返回 "no undefined event handle"，则多半是 **Gateway 或 frp 未把 POST body 传给 feishu**，需检查 Gateway 的插件路由是否在调用 handler 前消费了 request body、frp 是否配置为转发 body。

## 若仍报「返回数据不是合法的JSON格式」

1. **确认 OpenClaw 版本**：需使用**已在 Gateway 上注册 `/feishu/events`** 的版本（本仓库 `research/claw-ecosystem/openclaw` 的 feishu 扩展已支持：未设置 `webhookPort` 时在 Gateway 注册）。若用 npm 全局安装，请升级到包含该改动的版本，或从本仓库构建运行。
2. **确认未设 webhookPort**：全局搜索 `webhookPort`，确保 `channels.feishu` 及该账号下均未设置。
3. **抓包**：对 `http://124.221.173.158:18790/feishu/events` 发 POST（或等飞书校验），看响应 body 是否为 JSON、响应头是否为 `Content-Type: application/json`。

## 可选：独立 webhook 端口

若你希望**只暴露 feishu 回调、不暴露 Gateway**，可显式设置：

- `channels.feishu.webhookPort`（如 3000）
- 视需要 `webhookHost: "0.0.0.0"`

frp 将 18790 转到该端口（如 3000），飞书请求地址仍为 `http://124.221.173.158:18790/feishu/events`。此时请求不会经过 Gateway，由 feishu 独立 HTTP 服务处理（同样会返回 JSON）。

---

参考：`research/claw-ecosystem/openclaw/docs/channels/feishu.md`（Webhook and Gateway 小节）。

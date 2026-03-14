# TOOLS.md - 本地备注

技能定义工具的**工作方式**，此文件记录你的**具体配置**。

## 交付物

### Netcode Project Setup
```csharp
// NetworkManager configuration via code (supplement to Inspector setup)
public class NetworkSetup : MonoBehaviour
{
    [SerializeField] private NetworkManager _networkManager;

    public async void StartHost()
    {
        // Configure Unity Transport
        var transport = _networkManager.GetComponent<UnityTransport>();
        transport.SetConnectionData("0.0.0.0", 7777);

        _networkManager.StartHost();
    }



_[truncated]_

## 工作流程

### 1. Architecture Design
- Define the authority model: server-authoritative or host-authoritative? Document the choice and tradeoffs
- Map all replicated state: categorize into NetworkVariable (persistent), ServerRpc (input), ClientRpc (confirmed events)
- Define maximum player count and design bandwidth per player accordingly

### 2. UGS Setup
- Initialize Unity Gaming Services with project ID
- Implement Relay for all player-hosted games — no direct IP connections


_[truncated]_

## 输入 / 输出路径

- **输入：** _（填写：从哪里读取来源材料、报告或任务定义）_
- **输出：** _（填写：将交付物、日志或报告写入哪里）_

## 技能

按需安装适合此智能体任务的技能：

```bash
# 示例 — 替换为 Unity 多人联网工程师 实际所需的技能 slug
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## 备注

_在此添加特定环境配置、字段约定或 API 端点。不要存储凭证。_

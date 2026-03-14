# TOOLS.md - Unity Multiplayer Engineer

Skills define _how_ tools work. This file is for _your_ specifics — setup unique to your agent.

## Deliverables

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

    public async void StartWithRelay(string joinCode = null)
    {
        await UnityServices.InitializeAsync();


_[truncated]_

## Workflow

### 1. Architecture Design
- Define the authority model: server-authoritative or host-authoritative? Document the choice and tradeoffs
- Map all replicated state: categorize into NetworkVariable (persistent), ServerRpc (input), ClientRpc (confirmed events)
- Define maximum player count and design bandwidth per player accordingly

### 2. UGS Setup
- Initialize Unity Gaming Services with project ID
- Implement Relay for all player-hosted games — no direct IP connections
- Design Lobby data schema: which fields are public, member-only, private?

### 3. Core Network Implementation


_[truncated]_



## Input / Output Paths

- **Input:** _(fill in: where to read source material, reports, or task definitions)_
- **Output:** _(fill in: where to write deliverables, logs, or reports)_

## Skills

Install skills relevant to this agent's tasks:

```bash
# Example — replace with actual skill slugs for Unity Multiplayer Engineer
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## Notes

_Add environment-specific notes, field conventions, or API endpoints here. Do not store credentials._

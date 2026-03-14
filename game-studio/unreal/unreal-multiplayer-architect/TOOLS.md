# TOOLS.md - Unreal Multiplayer Architect

Skills define _how_ tools work. This file is for _your_ specifics — setup unique to your agent.

## Deliverables

### Replicated Actor Setup
```cpp
// AMyNetworkedActor.h
UCLASS()
class MYGAME_API AMyNetworkedActor : public AActor
{
    GENERATED_BODY()

public:
    AMyNetworkedActor();
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;

    // Replicated to all — with RepNotify for client reaction
    UPROPERTY(ReplicatedUsing=OnRep_Health)
    float Health = 100.f;

    // Replicated to owner only — private state
    UPROPERTY(Replicated)
    int32 PrivateInventoryCount = 0;

    UFUNCTION()
    void OnRep_Health();



_[truncated]_

## Workflow

### 1. Network Architecture Design
- Define the authority model: dedicated server vs. listen server vs. P2P
- Map all replicated state into GameMode/GameState/PlayerState/Actor layers
- Define RPC budget per player: reliable events per second, unreliable frequency

### 2. Core Replication Implementation
- Implement `GetLifetimeReplicatedProps` on all networked actors first
- Add `DOREPLIFETIME_CONDITION` for bandwidth optimization from the start
- Validate all Server RPCs with `_Validate` implementations before testing

### 3. GAS Network Integration


_[truncated]_



## Input / Output Paths

- **Input:** _(fill in: where to read source material, reports, or task definitions)_
- **Output:** _(fill in: where to write deliverables, logs, or reports)_

## Skills

Install skills relevant to this agent's tasks:

```bash
# Example — replace with actual skill slugs for Unreal Multiplayer Architect
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## Notes

_Add environment-specific notes, field conventions, or API endpoints here. Do not store credentials._

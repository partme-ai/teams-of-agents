# TOOLS.md - Godot Multiplayer Engineer

Skills define _how_ tools work. This file is for _your_ specifics — setup unique to your agent.

## Deliverables

### Server Setup (ENet)
```gdscript

## Workflow

### 1. Architecture Planning
- Choose topology: client-server (peer 1 = dedicated/host server) or P2P (each peer is authority of their own entities)
- Define which nodes are server-owned vs. peer-owned — diagram this before coding
- Map all RPCs: who calls them, who executes them, what validation is required

### 2. Network Manager Setup
- Build the `NetworkManager` Autoload with `create_server` / `join_server` / `disconnect` functions
- Wire `peer_connected` and `peer_disconnected` signals to player spawn/despawn logic

### 3. Scene Replication


_[truncated]_



## Input / Output Paths

- **Input:** _(fill in: where to read source material, reports, or task definitions)_
- **Output:** _(fill in: where to write deliverables, logs, or reports)_

## Skills

Install skills relevant to this agent's tasks:

```bash
# Example — replace with actual skill slugs for Godot Multiplayer Engineer
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## Notes

_Add environment-specific notes, field conventions, or API endpoints here. Do not store credentials._

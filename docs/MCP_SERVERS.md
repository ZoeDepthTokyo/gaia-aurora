# GAIA MCP Servers

## What Are MCP Servers?

The **Model Context Protocol (MCP)** is a standardized interface that allows LLMs (like Claude) to discover and call external tools via JSON-RPC. When Claude Code starts, it reads a list of configured MCP servers from `.claude/settings.json` (or the global equivalent) and can then invoke their tools during conversations.

GAIA currently consumes **10 external MCP plugins** (Greptile, Pinecone, Context7, etc.) but exposes **zero GAIA-native MCP servers**. This means Claude Code cannot natively call WARDEN validation, query ARGUS events, or store/retrieve MNEMIS memories without shelling out to CLI commands.

## Why Expose GAIA Modules as MCP Servers

1. **Discoverability** -- Claude Code sees GAIA tools in its tool list without the user needing to remember CLI syntax.
2. **Structured I/O** -- JSON-RPC requests and responses replace ad-hoc stdout parsing.
3. **Composability** -- Claude can chain GAIA tools together (e.g., "validate with WARDEN, then log the result to ARGUS").
4. **Ecosystem consistency** -- Every GAIA module speaks the same protocol.

## Architecture

Each GAIA MCP server is a lightweight **stdio-based JSON-RPC 2.0 server** that Claude Code spawns as a subprocess.

```
Claude Code
    |
    |-- stdio JSON-RPC --> _WARDEN/mcp_server.py
    |-- stdio JSON-RPC --> _ARGUS/mcp_server.py
    |-- stdio JSON-RPC --> _MNEMIS/mcp_server.py
    |-- stdio JSON-RPC --> (future modules...)
```

### Protocol Flow

1. Claude Code spawns `python _WARDEN/mcp_server.py` as a child process.
2. Sends `initialize` handshake over stdin (JSON-RPC).
3. Sends `tools/list` to discover available tools.
4. Sends `tools/call` with tool name and arguments.
5. Server responds with structured JSON result on stdout.

### Key Design Decisions

- **Transport: stdio** (not HTTP). MCP servers run locally as subprocesses, not network services.
- **One server per module**. Each GAIA component owns its own `mcp_server.py`.
- **Tool registry**: `mcp_registry.json` at the GAIA root catalogs all servers and their tools.
- **Stubs first**: Each `mcp_server.py` starts as a tool-definition stub. The actual JSON-RPC protocol handler is added in Phase 2.

## Modules to Expose

| Module  | Server Path               | Tools                                          | Priority |
|---------|---------------------------|-------------------------------------------------|----------|
| WARDEN  | `_WARDEN/mcp_server.py`  | `warden_validate`, `warden_scan_secrets`, `warden_check_env` | P0 |
| ARGUS   | `_ARGUS/mcp_server.py`   | `argus_health_check`, `argus_query_events`, `argus_ecosystem_status` | P0 |
| MNEMIS  | `_MNEMIS/mcp_server.py`  | `mnemis_store_memory`, `mnemis_retrieve`, `mnemis_search` | P1 |
| MYCEL   | `_MYCEL/mcp_server.py`   | `mycel_embed`, `mycel_query`, `mycel_chunk`    | P2 |
| LOOM    | `_LOOM/mcp_server.py`    | `loom_list_workflows`, `loom_run_workflow`      | P2 |
| RAVEN   | `_RAVEN/mcp_server.py`   | `raven_investigate`, `raven_summarize`          | P3 |

## Implementation Plan

### Phase 1: Stubs and Registry (Current)

- Define `MCP_TOOLS` lists in each `mcp_server.py` with JSON Schema input specs.
- Create `mcp_registry.json` cataloging all servers and their statuses.
- Document the architecture and tool contracts in this file.
- **No runtime behavior yet** -- stubs are importable Python that return tool definitions.

### Phase 2: Protocol Handler

- Implement a shared `gaia_mcp_base.py` library with:
  - JSON-RPC 2.0 stdio reader/writer
  - `initialize` / `tools/list` / `tools/call` dispatch
  - Error handling per MCP spec
- Each module's `mcp_server.py` imports the base and registers its tool handlers.

### Phase 3: Claude Code Integration

- Add entries to `.claude/settings.json` under `mcpServers`:
  ```json
  {
    "mcpServers": {
      "gaia-warden": {
        "command": "python",
        "args": ["X:/Projects/_GAIA/_WARDEN/mcp_server.py"]
      },
      "gaia-argus": {
        "command": "python",
        "args": ["X:/Projects/_GAIA/_ARGUS/mcp_server.py"]
      },
      "gaia-mnemis": {
        "command": "python",
        "args": ["X:/Projects/_GAIA/_MNEMIS/mcp_server.py"]
      }
    }
  }
  ```
- Test tool discovery and invocation from Claude Code sessions.

### Phase 4: Full Ecosystem

- Add MCP servers for MYCEL, LOOM, RAVEN as those modules stabilize.
- Implement cross-module tool chaining (e.g., WARDEN validates, ARGUS logs the result).
- Add authentication/authorization if GAIA modules are ever exposed over network transport.

## File Reference

| File                          | Purpose                                  |
|-------------------------------|------------------------------------------|
| `docs/MCP_SERVERS.md`        | This document (architecture + plan)      |
| `mcp_registry.json`          | Central catalog of all GAIA MCP servers  |
| `_WARDEN/mcp_server.py`      | WARDEN tool definitions stub             |
| `_ARGUS/mcp_server.py`       | ARGUS tool definitions stub              |
| `_MNEMIS/mcp_server.py`      | MNEMIS tool definitions stub             |

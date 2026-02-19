# GENESIS Protocol v0.1.0

## Vision

GENESIS (Global Ecosystem Network for Emergent System Intelligence Synthesis) is the
federation layer for thousands of GAIA instances worldwide.

Each GAIA installation — running in a clinic, research lab, or enterprise — is an
independent node. GENESIS connects these nodes so that patterns discovered in one
instance accelerate learning across all instances. The SOURCE GAIA holds the
canonical intelligence; every node feeds it and benefits from it.

**Current status**: Wire format only. No networking. No transmission logic.
This document specifies the data contracts that will govern federation when the
network is built.

---

## Core Concepts

| Term | Definition |
|------|-----------|
| **Instance** | A single deployed GAIA installation with a unique `instance_id` |
| **SOURCE GAIA** | The canonical hub that aggregates telemetry from all instances |
| **Heartbeat** | Periodic health signal sent from an instance to GENESIS |
| **Event** | A discrete telemetry record describing something that happened |
| **Collector** | Local buffer that accumulates events before transmission |

---

## Protocol Version

`PROTOCOL_VERSION = "0.1.0"`

All messages embed the protocol version so the hub can apply schema migration
when the format evolves.

---

## Wire Format

### GENESISHeartbeat

Sent periodically (suggested interval: every 5 minutes) to report instance health.

```json
{
  "instance_id": "uuid-string",
  "instance_name": "clinic-north-gaia",
  "gaia_version": "0.5.2",
  "components": ["ARGUS", "MYCEL", "LOOM", "MNEMIS"],
  "health_score": 0.95,
  "compliance_score": 0.80,
  "active_products": ["jSeeker", "JobPulse"],
  "uptime_hours": 72.4,
  "timestamp": "2026-02-19T04:00:00.000000",
  "protocol_version": "0.1.0"
}
```

Field rules:
- `health_score`: float in [0.0, 1.0]; derived from ARGUS ecosystem validator
- `compliance_score`: float in [0.0, 1.0]; derived from GuardrailEngine
- `components`: list of active GAIA component names (must match registry keys)
- `timestamp`: ISO 8601 with microseconds

### GENESISEvent

Emitted when something notable occurs in the instance.

```json
{
  "event_id": "550e8400-e29b-41d4-a716-446655440000",
  "source_instance": "uuid-string",
  "event_type": "pattern_detected",
  "payload": {
    "pattern_name": "retry_loop",
    "component": "ARGUS",
    "severity": "medium"
  },
  "schema_version": "0.1.0",
  "timestamp": "2026-02-19T04:01:23.456789"
}
```

Defined `event_type` values:

| event_type | When to emit |
|-----------|-------------|
| `pattern_detected` | ARGUS subconscious identifies a recurring pattern |
| `anomaly_detected` | Anomaly detection engine fires |
| `compliance_report` | GuardrailEngine produces a compliance summary |
| `learning_update` | MNEMIS promotes a pattern to a higher memory tier |

---

## Python API

### Module

```
_ARGUS/genesis/protocol.py
```

### Usage

```python
from genesis.protocol import GENESISCollector, PROTOCOL_VERSION

# One collector per GAIA instance (long-lived)
collector = GENESISCollector(instance_id="my-uuid", instance_name="prod")

# Record events as they occur
collector.record_event("pattern_detected", {"pattern": "retry_loop"})
collector.record_event("anomaly_detected", {"component": "ARGUS", "severity": "low"})

# Generate a heartbeat
hb = collector.generate_heartbeat(
    gaia_version="0.5.2",
    components=["ARGUS", "MYCEL"],
    health_score=0.95,
    compliance_score=0.80,
    active_products=["jSeeker"],
    uptime_hours=24.0,
)
print(hb.to_json())  # ready for transmission

# Flush after transmission
count = collector.flush()
print(f"Transmitted {count} events")
```

### Serialization contract

Both `GENESISHeartbeat` and `GENESISEvent` implement:

```python
def to_dict(self) -> dict: ...     # JSON-compatible dict
def to_json(self) -> str: ...      # JSON string
@classmethod
def from_dict(cls, data: dict) -> Self: ...  # reconstruct from dict
```

Roundtrip guarantee: `from_dict(x.to_dict())` equals `x` for all fields.

---

## Rollback Scripts

Two scripts manage version tagging across all GAIA submodules:

### Tag a known-good release

```bash
python scripts/tag_known_good.py v0.5.3
```

Tags the GAIA root repo and every submodule listed under `_GAIA/_*` paths
in `registry.json` with an annotated git tag. Use this immediately after a
release that passes all CI checks.

### Roll back to a known-good release

```bash
python scripts/rollback.py v0.5.2
```

Verifies the tag exists in the root repo, then checks out that tag in
root + all submodules. Run this when a regression is detected in production.

Script locations:
- `X:\Projects\_GAIA\scripts\tag_known_good.py`
- `X:\Projects\_GAIA\scripts\rollback.py`

---

## Future Roadmap

| Phase | Capability |
|-------|-----------|
| v0.1.0 (now) | Wire format contracts; local buffering only |
| v0.2.0 | HTTP transport layer; batch upload to GENESIS hub endpoint |
| v0.3.0 | Differential privacy on payload before transmission |
| v0.4.0 | SOURCE GAIA aggregation API; cross-instance pattern merging |
| v1.0.0 | Full federation; real-time learning propagation to all nodes |

---

## Design Principles

1. **No networking in v0.1.0** — data contracts are stable before transport is added
2. **Protocol version in every message** — enables hub-side schema migration
3. **Instance ID propagation** — all events traceable to their origin
4. **Local-first** — `GENESISCollector` works fully offline; transmission is optional
5. **Additive evolution** — new fields added with defaults; old fields never removed in a minor version

# Enterprise Roadmap Analytics — Public Demonstration

**Independent educational example using entirely synthetic data.** This is **not** the source code, dataset, configuration, or deployment of any employer or client system.

## Problem and approach

Enterprises need a traceable view of active requests, prioritization and progress. This simplified Python demonstration illustrates three principles:

1. Keep a normalized work-item representation separate from source-specific fields.
2. Distinguish open/closed items and report totals with explicit definitions.
3. Preserve traceable links and record uncertainty rather than inferring decisions from incomplete text.

Run the offline example:

```bash
python demo_roadmap.py
python -m unittest discover -s tests -v
```

There are no network requests, Azure credentials, production clients, real customer names, exports, or confidential records. The simulated items are invented for this repository.

## Relation to professional work

This public demonstration illustrates general engineering patterns explored during an internal enterprise roadmap analytics prototype. The actual prototype and all employer data remain private. Its production readiness and AI classification were not established; this repository makes no such claims.

No third-party project code is licensed or included.

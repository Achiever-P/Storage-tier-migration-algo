# Storage-Tier Management Prototype

This project is a *prototype storage-tier management system* designed to study and compare data placement, migration, and performance trade-offs across multiple storage tiers:  

- *Hot Tier* (fast but expensive, e.g., SSD / NVMe)  
- *Warm Tier* (balanced, e.g., HDD)  
- *Cold Tier* (cheap, high-capacity, e.g., object storage / tape)  

The system implements a *tier-aware storage manager* where files and blocks are automatically classified, migrated, and retrieved based on *access frequency*, *latency requirements*, and *cost constraints*.  

---

## 📂 Project Structure

proto/
└── tier.proto             # gRPC message definitions (placement, migrate, stats)

src/
├── __init__.py
├── api.py                 # Client-facing API (FastAPI / REST)
├── node.py                # Runs a full node (api + schedulers + metrics)
├── metadata_store.py      # Object/file metadata (size, age, access freq, tier)
├── policy_engine.py       # Policy DSL (SLA, cost caps, compliance tags)
├── tier_manager.py        # Placement decisions (hot/warm/cold) + routing
├── migrator.py            # Background moves, compaction, recalls
├── cache_index.py         # LRU/LFU admission & promotion decisions
├── cost_model.py          # $/GB, IOPS caps, egress penalties
├── util.py                # Logging, configs, ID generators

├── tiers/
│   ├── __init__.py
│   ├── hot_ssd.py         # NVMe/SSD driver
│   ├── warm_object.py     # Object store driver (S3/GCS compatible)
│   └── cold_archive.py    # Archive/glacier-like driver

tests/
├── test_policy.py
├── test_tiering_strong.py
├── test_tiering_eventual.py
└── test_integration.py

benchmarks/
├── loadgen.py             # Async client load: read/write/mixed/scan
├── fault_injection.py     # Latency spikes, tier outages, throttling
└── analysis.ipynb         # Plots: p50/p95 latency, cost, promotion rate

docker/
├── Dockerfile
└── docker-compose.yml

requirements.txt
README.md


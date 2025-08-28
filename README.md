# Storage-Tier Management Prototype

This project is a *prototype storage-tier management system* designed to study and compare data placement, migration, and performance trade-offs across multiple storage tiers:  

- *Hot Tier* (fast but expensive, e.g., SSD / NVMe)  
- *Warm Tier* (balanced, e.g., HDD)  
- *Cold Tier* (cheap, high-capacity, e.g., object storage / tape)  

The system implements a *tier-aware storage manager* where files and blocks are automatically classified, migrated, and retrieved based on *access frequency*, *latency requirements*, and *cost constraints*.  

---

## 📂 Project Structure

storage-tier-management/
├── proto/
│   └── storage.proto          # gRPC message definitions for tier migration API

├── src/
│   ├── __init__.py
│   ├── tier_manager.py        # Core tier management logic
│   ├── policy.py              # Policies (LRU, LFU, cost-based, ML-driven)
│   ├── monitor.py             # Access pattern monitoring & statistics
│   ├── migrator.py            # Background migration between tiers
│   ├── api.py                 # Client-facing API (FastAPI / REST)
│   ├── node.py                # Runs a storage node with tier manager
│   ├── util.py                # Shared utilities (logging, configs)
│   └── tiers/
│       ├── __init__.py
│       ├── hot.py             # Hot storage (fast, SSD/NVMe simulation)
│       ├── warm.py            # Warm storage (balanced HDD simulation)
│       └── cold.py            # Cold storage (object/archive simulation)

├── tests/
│   ├── test_policies.py        # Unit tests for placement & eviction policies
│   ├── test_migration.py       # Unit tests for migration logic
│   └── test_integration.py     # End-to-end tests

├── benchmarks/
│   ├── workload_gen.py         # Synthetic workload generator
│   ├── fault_injection.py      # Simulates tier failures, overloads
│   └── analysis.ipynb          # Plots performance and cost trade-offs

├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml

├── requirements.txt
└── README.md

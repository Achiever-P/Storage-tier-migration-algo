# Storage-Tier Migration Algorithm

##  Project Description
This project implements a *storage-tier migration algorithm* that manages data placement between *SSD (Solid State Drive)* and *HDD (Hard Disk Drive)*.  
The algorithm identifies hot files (frequently/recently accessed) and keeps them on SSD for faster access, while cold files are migrated to HDD for cost efficiency.  

The system is evaluated on *public cloud-trace workloads* (e.g., Google Cluster Traces, Azure Functions, FIU/MSR workloads) to test real-world performance.

---

## 📂 Project Structure

proto/
└── storage.proto # gRPC message definitions for tier migration API

src/
├── init.py
├── tier_manager.py # Core tier management logic
├── policy.py # Policies (LRU, LFU, cost-based, ML-driven)
├── monitor.py # Access pattern monitoring & statistics
├── migrator.py # Background migration between tiers
├── api.py # Client-facing API (FastAPI / REST)
├── node.py # Runs a storage node with tier manager
├── util.py # Shared utilities (logging, configs)

tiers/
├── hot.py # Hot storage (fast, SSD/NVMe simulation)
├── warm.py # Warm storage (balanced HDD simulation)
├── cold.py # Cold storage (object/archive simulation)

tests/
├── test_policies.py # Unit tests for placement & eviction policies
├── test_migration.py # Unit tests for migration logic
└── test_integration.py # End-to-end tests

benchmarks/
├── workload_gen.py # Synthetic workload generator
├── fault_injection.py # Simulates tier failures, overloads
└── analysis.ipynb # Plots performance and cost trade-offs

docker/
├── Dockerfile
└── docker-compose.yml

requirements.txt
README.md

---

## ⚙ Core Components

### 1. Migration Policy
- **LRU (Least Recently Used)**: Evict coldest files based on recency.  
- **LFU (Least Frequently Used)**: Evict coldest files based on frequency.  
- **Heat Score Formula**:  
Heat(file) = α * Frequency + β * Recency
- α, β are tunable weights.  
- Higher heat → file is “hot” → keep in SSD.  
- Lower heat → file is “cold” → migrate to HDD.  

### 2. Storage Manager
- **SSD Tier**: Fast, expensive, limited capacity.  
- **HDD Tier**: Slow, cheap, large capacity.  
- Handles file placement, migration, and evictions.  

### 3. Workload Traces
- **Google Cluster Traces** → large-scale job workloads.  
- **Azure Blob/Functions Traces** → object storage + serverless workloads.  
- **FIU/MSR Traces** → enterprise storage access logs.  

### 4. Evaluator
- Measures:  
- **Hit Ratio** (requests served from SSD).  
- **Latency** improvement.  
- **Evictions/Migrations** overhead.  
- **Storage Utilization** (SSD vs HDD).  

---


---

## ⚙ Core Components

### Tier Manager
- Decides where to place and migrate data.  
- Works with monitoring and policies to balance *latency*, *cost*, and *capacity*.  

### Policies
- *LRU / LFU*: Move frequently accessed data to hot tier.  
- *Cost-aware*: Optimize placement based on cost vs performance.  
- *Hybrid / ML-based*: Predictive migration policies.  

### Migration Engine
- Asynchronously migrates data between tiers.  
- Ensures consistency and minimal disruption to client requests.  

---

## 🔄 Workflow

### 1. Write Operation
mermaid
sequenceDiagram
  participant C as Client
  participant TM as Tier Manager
  participant H as Hot Tier
  participant W as Warm Tier

  C->>TM: Write request (file/block)
  TM->>H: Place in Hot Tier (default / high-priority)
  H-->>TM: Stored
  TM-->>C: ACK

---

### 2. Migration (Hot → Warm → Cold)
mermaid
sequenceDiagram
  participant M as Monitor
  participant TM as Tier Manager
  participant H as Hot Tier
  participant W as Warm Tier
  participant C as Cold Tier

  M->>TM: Usage stats (access counts, frequency)
  TM->>H: Select cold data for eviction
  H->>W: Move to Warm Tier
  W->>C: Move to Cold Tier (if rarely accessed)

---

## 📊 Benchmarks

* **benchmarks/workload_gen.py**: Generates synthetic I/O workloads.  
* **benchmarks/fault_injection.py**: Simulates overloads, failures, and recovery.  
* **benchmarks/analysis.ipynb**: Plots latency, throughput, tier utilization, and storage cost.  

---

## 🚀 Running the Project

### With Docker
```bash
docker-compose up --build

# Storage-Tier Migration Algorithm

##  Project Description
This project implements a *storage-tier migration algorithm* that manages data placement between *SSD (Solid State Drive)* and *HDD (Hard Disk Drive)*.  
The algorithm identifies hot files (frequently/recently accessed) and keeps them on SSD for faster access, while cold files are migrated to HDD for cost efficiency.  

The system is evaluated on *public cloud-trace workloads* (e.g., Google Cluster Traces, Azure Functions, FIU/MSR workloads) to test real-world performance.

---

## 📂 Project Structure

src/
├── __init__.py
├── migration_daemon.py    # Background service for monitoring and migration
├── heat_score.py          # File access heat-score computation (LRU, LFU, recency, frequency)
├── policy.py              # Migration policy logic (when to move SSD→HDD or HDD→SSD)
├── trace_loader.py        # Loads cloud trace datasets
├── evaluator.py           # Evaluates migration policy on workloads
├── storage_sim.py         # Simulated SSD + HDD layers
├── util.py                # Common helper functions (logging, configs, timers)

data/
├── google_cluster.csv     # Example cloud trace
├── msr_trace.csv
└── fiu_trace.csv

tests/
├── test_heat_score.py
├── test_policy.py
└── test_integration.py

benchmarks/
├── workload_replay.py     # Replays traces against migration policy
└── analysis.ipynb         # Jupyter notebook for graphs/plots

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

## 🔄 Workflow

### 1. Monitoring
- File accesses are monitored in real time (frequency + recency).  

### 2. Heat Calculation
- Compute heat score for each file periodically.  

### 3. Migration Decision
- If SSD is full:  
- Evict lowest-heat files → HDD.  
- If hot files in HDD detected:  
- Promote to SSD.  

---

## 📊 Benchmarks

- **benchmarks/analyze.ipynb** → Plot migration performance.  
- **benchmarks/heatmap.py** → Show hot/cold distribution.  
- **benchmarks/histogram.py** → Access frequency distribution.  

---


##  Goal
- Improve *I/O performance* by storing hot data on SSD.  
- Reduce *storage costs* by moving cold data to HDD.  
- Ensure *fair evaluation* using multiple workload traces.  
- Explore different migration policies: *LRU, LFU, ARC, Heat Score*.

---

##  Features
- *Heat Score Calculation*  
  - Combines recency and frequency to rank files.  

- *Migration Daemon*  
  - Background process that monitors file usage and decides promotion/demotion.  

- *Eviction Policy*  
  - When SSD is full, the coldest files are evicted to HDD.  

- *Evaluation on Cloud Traces*  
  - Workload datasets from Google, Azure, FIU/MSR.  
  - Metrics: hit ratio, migration overhead, latency, storage cost.  

- *Optional Enhancements*  
  - Multi-tier storage (SSD → HDD → Cloud Archive).  
  - Cost-aware and wear-aware migration.  
  - Visualization dashboard for file movement and performance.  

---

##  Tech Stack
- *Languages*: Python / C (simulation + implementation)  
- *Data Structures*:  
  - Hash Maps (fast lookup of file info)  
  - Priority Queues / Heaps (for eviction order)  
  - LRU Cache mechanisms  
- *Datasets*:  
  - Google Cluster Trace  
  - Azure Functions Blob Storage Trace  
  - FIU/MSR storage workloads  

---

##  Evaluation Metrics
- *Hit Ratio* → Percentage of file accesses served from SSD.  
- *Migration Overhead* → Number of file moves between SSD and HDD.  
- *Latency Improvement* → Reduced access time compared to HDD-only.  
- *Storage Cost Reduction* → Balance between expensive SSD and cheaper HDD.  
- *SSD Lifetime Impact* → Number of writes affecting endurance.  

---

##  Future Scope
- Machine Learning–based hot file prediction.  
- Cost + wear-aware hybrid migration policies.  
- Real-time OS-level integration as a background *storage management daemon*.  
- Extend to *3-tier storage* (SSD → HDD → Cloud Archive).  

---

##  References
- Google Cluster Trace (2011)  
- Microsoft Azure Functions + Blob Storage Traces  
- FIU/MSR Storage Workload Suite  

---

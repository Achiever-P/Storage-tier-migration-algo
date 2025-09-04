import random
from src.tier_manager import TierManager

def run_workload(n=1000):
    tm = TierManager()
    for i in range(n):
        key = f"k{i}"
        tm.put(key, f"val{i}")
        if random.random() < 0.5:
            tm.get(key)

if __name__ == "__main__":
    run_workload()

class HotTier:
    def __init__(self, capacity=100):
        self.store = {}
        self.capacity = capacity

    def __contains__(self, key):
        return key in self.store

    def get(self, key):
        return self.store.get(key)

    def put(self, key, value):
        if len(self.store) >= self.capacity:
            evicted_key, evicted_val = self.store.pop(next(iter(self.store)))
            print(f"[HotTier] Evicted {evicted_key}")
        self.store[key] = value

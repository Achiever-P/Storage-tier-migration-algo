class MigrationEngine:
    def __init__(self, hot, warm, cold):
        self.hot = hot
        self.warm = warm
        self.cold = cold

    def promote_to_hot(self, key, value):
        print(f"[Migration] Promoting {key} -> HotTier")
        self.hot.put(key, value)

    def promote_to_warm(self, key, value):
        print(f"[Migration] Promoting {key} -> WarmTier")
        self.warm.put(key, value)

    def demote_to_warm(self, key, value):
        print(f"[Migration] Demoting {key} -> WarmTier")
        self.warm.put(key, value)

    def demote_to_cold(self, key, value):
        print(f"[Migration] Demoting {key} -> ColdTier")
        self.cold.put(key, value)

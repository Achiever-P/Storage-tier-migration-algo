from .hot_tier import HotTier
from .warm_tier import WarmTier
from .cold_tier import ColdTier
from .migration import MigrationEngine
from .policy import PolicyEngine

class TierManager:
    def __init__(self):
        self.hot = HotTier()
        self.warm = WarmTier()
        self.cold = ColdTier()
        self.policy = PolicyEngine()
        self.migration = MigrationEngine(self.hot, self.warm, self.cold)

    def get(self, key):
        
        if key in self.hot:
            return self.hot.get(key)
        elif key in self.warm:
            data = self.warm.get(key)
            self.migration.promote_to_hot(key, data)
            return data
        elif key in self.cold:
            data = self.cold.get(key)
            self.migration.promote_to_warm(key, data)
            return data
        else:
            return None

    def put(self, key, value):
        
        self.hot.put(key, value)
        self.policy.evaluate(self.hot, self.warm, self.cold, self.migration)

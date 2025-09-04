class PolicyEngine:
    def evaluate(self, hot, warm, cold, migration):
       
        if len(hot.store) > hot.capacity * 0.8:
            k, v = hot.store.popitem()
            migration.demote_to_warm(k, v)
        if len(warm.store) > warm.capacity * 0.8:
            k, v = warm.store.popitem()
            migration.demote_to_cold(k, v)

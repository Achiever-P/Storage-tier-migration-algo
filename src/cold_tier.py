class ColdTier:
    def __init__(self):
        self.store = {}

    def __contains__(self, key):
        return key in self.store

    def get(self, key):
        return self.store.get(key)

    def put(self, key, value):
        self.store[key] = value

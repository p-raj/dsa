class LRUCache:

    def __init__(self, capacity: int):
        self.keys = [None] * capacity
        self.kv = {}
        self.lru = 0

    def _update(self):
        self.lru += 1
        self.lru = self.lru % len(self.keys)

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        self.put(key, self.kv[key])
        return self.kv[key]

    def put(self, key: int, value: int) -> None:
        k = self.keys[self.lru]
        self.kv.pop(k, None)
        self.keys[self.lru] = key
        self.kv[key] = value
        self._update()
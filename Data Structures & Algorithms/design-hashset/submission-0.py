class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hs = [None] * self.size
    
    def _get_pos(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        pos = self._get_pos(key)
        if self.hs[pos] is None:
            self.hs[pos] = []
        self.hs[pos].append(key)    

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        pos = self._get_pos(key)
        self.hs[pos].pop(self.hs[pos].index(key))
        if len(self.hs[pos]) == 0:
            self.hs[pos] = None

    def contains(self, key: int) -> bool:
        pos = self._get_pos(key)
        if self.hs[pos] is None:
            return False
        return key in self.hs[pos]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
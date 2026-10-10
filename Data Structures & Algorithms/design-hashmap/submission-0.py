class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hs = [None] * self.size
    
    def _get_pos(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        pos = self._get_pos(key)
        if not self.contains(key):
            if self.hs[pos] is None:
                self.hs[pos] = []
            self.hs[pos].append((key, value))
        else:
            for idx, (i,j) in enumerate(self.hs[pos]):
                if i == key:
                    self.hs[pos][idx] = (key, value)        

    def get(self, key: int) -> int:
        if not self.contains(key):
            return -1
        pos = self._get_pos(key)
        for (i,j) in self.hs[pos]:
            if i == key:
                return j
        return -1

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        pos = self._get_pos(key)
        index = None
        for idx, (i,j) in enumerate(self.hs[pos]):
            if i == key:
                index = idx
                break
        self.hs[pos].pop(index)
        if len(self.hs[pos]) == 0:
            self.hs[pos] = None

    def contains(self, key: int) -> bool:
        pos = self._get_pos(key)
        if self.hs[pos] is None:
            return False
        return any(key == i for (i,_) in self.hs[pos])



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
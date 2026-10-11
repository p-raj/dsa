import random

class RandomizedSet:

    def __init__(self):
        self.idx = {}
        self.val = {}
        self.nxt = 0
        self.cap = 0

    def insert(self, val: int) -> bool:
        if val in self.val:
            return False
        self.idx[self.nxt] = val
        self.val[val] = self.nxt
        self.nxt += 1
        self.cap += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val:
            return False
        self.cap -= 1
        del(self.idx[self.val[val]])
        del(self.val[val])
        return True

    def getRandom(self) -> int:
        while True:
            idx = random.randint(0, self.nxt)
            if idx <= self.cap and idx in self.idx:
                return self.idx[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
import random
class RandomizedSet:

    def __init__(self):
        self.val = []
        self.idx = {}        

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.val)
        self.val.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        if not self.val:
            return False
        idx = self.idx[val]
        last_val = self.val[-1]
        self.val[idx] = last_val
        self.idx[last_val] = idx
        self.val.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.val)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
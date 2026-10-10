from collections import defaultdict
class HitCounter:

    def __init__(self):
        self.window = 300
        self.t = {
            -1: [0] * (self.window + 1)
        }

    def _get_key(self, timestamp: int) -> int:
        return timestamp//self.window, timestamp%self.window

    def hit(self, timestamp: int) -> None:
        b, k = self._get_key(timestamp)
        if b not in self.t:
            self.t[b] = [0] * (self.window + 1)
        self.t[b][k] += 1

    def getHits(self, timestamp: int) -> int:
        b, k = self._get_key(timestamp)
        pb = (b-1)
        sm = sum(self.t[b][:k+1]) if b in self.t else 0
        sm += sum(self.t[pb][k+1:]) if pb in self.t else 0
        return sm


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

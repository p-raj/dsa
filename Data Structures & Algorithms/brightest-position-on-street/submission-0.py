from collections import defaultdict
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        self.l = defaultdict(int)
        maxl = float("-inf")
        maxi = float("-inf")
        for o, r in lights:
            for i in range(o-r, o+r+1):
                self.l[i] += 1
                if self.l[i] > maxl:
                    maxl = self.l[i]
                    maxi = i
        return [i for i in self.l if self.l[i] == maxl][0]
        # return next([i for i in self.l if self.l[i] == maxl], 0)
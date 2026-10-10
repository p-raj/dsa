from collections import defaultdict
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        rng = [[o-r, o+r] for o,r in lights]
        b = defaultdict(int)
        for l,r in rng:
            # starts illuminating at L
            b[l] += 1
            # stops illuminating at R+1
            b[r+1] -= 1
        maxl = float("-inf")
        maxi = float("-inf")
        curr = 0
        for k in sorted(b):
            curr += b[k]
            if curr > maxl:
                maxl = curr
                maxi = k
        return maxi
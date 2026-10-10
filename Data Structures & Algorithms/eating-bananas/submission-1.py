import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        # whatever is on the left
        # time to eat a pile = an hour
        # whatever is on the right
        # time to eat = math.ceil(right/now)
        # need to figure out a <min pivot>
        # least amount of time == number of piles
        # so if len(piles) >= h: return max(piles)
        lft = 1
        rgt = piles[-1]
        res = piles[-1]
        while lft <= rgt:
            mid = (lft + rgt)//2
            tt = 0
            for p in piles:
                tt += math.ceil(p/mid)
            if tt <= h:
                res = mid
                rgt = mid - 1
            else:
                lft = mid + 1
        return res
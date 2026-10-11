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
        lft = len(piles) - 2
        tot = len(piles)
        spd = piles[len(piles)-1]
        while lft > -1:
            rgt = len(piles) - 1
            ttim = rgt
            snow = piles[lft]
            while rgt > lft:
                ttim += math.ceil(piles[rgt]/snow)
                rgt -= 1
            if ttim <= h and spd > snow:
                spd = snow
            lft -= 1
        return spd
                
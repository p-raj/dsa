class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # greedy algo
        # if lft and rgt match
        # choose the one with lower cost
        # becase one of them has to be removed anyways
        T = neededTime
        lft = 0
        cost = 0
        while lft < len(colors) - 1:
            rgt = lft + 1
            maxl_ = lft
            sm_ = T[lft]
            while rgt < len(colors) and colors[lft] == colors[rgt]:
                sm_ += T[rgt]
                if T[maxl_] < T[rgt]:
                    maxl_ = rgt
                rgt += 1
            sm_ -= T[maxl_]
            cost += sm_
            lft = rgt
        return cost

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # greedy algo
        # if lft and rgt match
        # choose the one with lower cost
        # becase one of them has to be removed anyways
        lft = 0
        cost = 0
        while lft < len(colors) - 1:
            rgt = lft + 1
            while rgt < len(colors) and colors[lft] == colors[rgt]:
                if neededTime[lft] < neededTime[rgt]:
                    cost += neededTime[lft]
                    lft += 1
                    rgt += 1
                else:
                    cost += neededTime[rgt]
                    rgt += 1
            lft = rgt
        return cost

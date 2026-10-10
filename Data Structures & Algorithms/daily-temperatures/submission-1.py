class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        res = [0] * len(t)
        lft, rgt = 0, 0
        while lft < len(t) - 1:
            rgt = lft + 1
            while rgt < len(t):
                if t[lft] < t[rgt]:
                    break
                rgt += 1
            if rgt < len(t):
                res[lft] = rgt - lft
            lft += 1
        return res
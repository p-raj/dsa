class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        count = 0

        for lft in range(len(calories) - k + 1):
            tot = 0
            for rgt in range(k):
                tot += calories[lft + rgt]
            if tot < lower:
                count -= 1
            elif tot > upper:
                count += 1

        return count

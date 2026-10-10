from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = list(Counter(nums).items())
        res = []
        subset = []

        def dfs(i):
            if i == len(counts):
                res.append(subset.copy())
                return

            val, freq = counts[i]

            for c in range(freq + 1):
                subset.extend([val] * c)
                dfs(i + 1)

                for _ in range(c):
                    subset.pop()

        dfs(0)
        return res
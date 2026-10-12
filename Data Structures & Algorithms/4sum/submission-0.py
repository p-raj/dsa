import itertools


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        idxs = list(range(len(nums)))
        combo = itertools.combinations(idxs, 4)
        res = set()
        for c in combo:
            n = tuple(sorted([nums[i] for i in c]))
            if sum(n) == target:
                res.add(n)
        # print(res)
        return list(list(x) for x in res)

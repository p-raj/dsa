from collections import Counter, defaultdict


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        lft = defaultdict(int)
        rgt = Counter(nums)

        for i in range(len(nums)):
            lft[nums[i]] += 1
            rgt[nums[i]] -= 1

            if 2 * lft[nums[i]] > (i + 1) and 2 * rgt[nums[i]] > (len(nums) - i - 1):
                return i
        return -1

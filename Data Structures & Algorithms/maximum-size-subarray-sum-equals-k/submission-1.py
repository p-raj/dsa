class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        tot = sum(nums)

        memo = {}

        def fn(lft: int, rgt: int, sm_: int) -> int:
            key = (lft, rgt)
            if key in memo:
                return memo[key]
            if lft > rgt:
                return 0
            if sm_ == k:
                memo[key] = rgt - lft + 1
                return memo[key]
            memo[key] = max(
                fn(lft + 1, rgt, sm_ - nums[lft]),
                fn(lft, rgt - 1, sm_ - nums[rgt]),
                # fn(lft + 1, rgt - 1, sm_ - (nums[lft] + nums[rgt])),
            )
            return memo[key]

        return fn(0, len(nums) - 1, tot)

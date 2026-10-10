class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}

        def Fn(lft: int, rgt: int) -> int:
            # exact sum of nums[lft:rgt+1]
            key = (lft, rgt)
            if key in memo:
                return memo[key]

            if lft == rgt:
                memo[key] = nums[lft]
            else:
                memo[key] = Fn(lft, rgt - 1) + nums[rgt]

            return memo[key]

        best = float("-inf")

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                best = max(best, Fn(i, j))

        return best
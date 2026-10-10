class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}

        def Fn(idx: int) -> int:
            # state: at index [i]
            # what is the best sum?
            # would it be the index?
            # would it be the running sum?
            if idx in memo:
                return memo[idx]
            if idx == 0:
                memo[idx] = nums[0]
                return memo[idx]
            memo[idx] = max(
                # it's better to forget running sum
                nums[idx],
                # keep building up the running sum
                Fn(idx-1) + nums[idx] 
            )
            return memo[idx]

        best = float("-inf")
        for i in range(len(nums)):
            best = max(best, Fn(i))
        return best
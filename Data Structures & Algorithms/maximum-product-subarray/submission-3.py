class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_p = nums[0]
        max_p = nums[0]
        memo = {}

        def f(i: int) -> (int, int):
            # max, min ending at index i
            if i in memo:
                return memo[i]
            # base case
            if i == 0:
                memo[i] = (nums[0], nums[0])
                return memo[i]
            prev_max, prev_min = f(i - 1)
            cur_max = max(
                nums[i],
                nums[i] * prev_max,
                nums[i] * prev_min
            )
            cur_min = min(
                nums[i],
                nums[i] * prev_max,
                nums[i] * prev_min
            )
            memo[i] = (cur_max, cur_min)
            return memo[i]
        
        best = float("-inf")
        for i in range(len(nums)):
            best = max(best, f(i)[0])

        return best
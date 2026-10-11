class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # what is the shape of the optimal solution
        # <state>?
        # <output> -> int (length)
        # what if len(nums) were 1 => output = nums[1]
        # state[i] represents the length of sequence
        # when discussing the index i
        # F(i) = if [i] > [i-1] F(i-1)+1 else F(i-1)

        memo = {}
        
        def f(i: int) -> int:
            if i in memo:
                return memo[i]

            if i == 0:
                memo[i] = 1
                return memo[i]

            if i >= len(nums):
                memo[i] = 0
                return memo[i]

            if nums[i] > nums[i-1]:
                memo[i] = f(i-1) + 1
            else:
                memo[i] = f(i-1)
            return memo[i]

        mx = float('-inf')
        for i in range(len(nums)):
            mx = max(mx, f(i))
        return mx
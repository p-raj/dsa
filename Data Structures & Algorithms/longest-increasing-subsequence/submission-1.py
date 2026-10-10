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
        
        def Fn(i: int) -> int:
            if i in memo:
                return memo[i]

            if i == 0:
                memo[i] = 1
                return memo[i]

            if i >= len(nums):
                memo[i] = 0
                return memo[i]

            best_of = []
            for j in range(i):
                if nums[j] < nums[i]:
                    best_of.append(Fn(j))
            
            memo[i] = max(best_of) + 1 if best_of else 1
            return memo[i]

        mx = float('-inf')
        for i in range(len(nums)):
            mx = max(mx, Fn(i))
        return mx
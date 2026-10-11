class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # exploration of all the states
        # better solved with BT
        # what does a state represent?
        # when jumping from [n-i] -> [n]
        # what value does nums[n-i] holds?
        # for all those values, is it possible
        # to get from [n-i] -> [n]
        # [shape] of [output] = bool
        memo = {}

        def Fn(idx: int) -> bool:
            if idx in memo:
                return memo[idx]
            if idx == len(nums)-1:
                memo[idx] = True
                return memo[idx]
            if idx >= len(nums) or nums[idx] == 0:
                memo[idx] = False
                return memo[idx]
            poss = False
            for jmp in range(1, nums[idx]+1):
                if (idx + jmp) < len(nums):
                    poss |= Fn(idx+jmp)
                if poss is True:
                    memo[idx] = True
                    break
            memo[idx] = poss
            return memo[idx]
        
        return Fn(0)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def Fn(idx: int) -> bool:
            if idx in memo:
                return memo[idx]

            if idx == len(nums) - 1:
                memo[idx] = True
                return True

            if idx >= len(nums) or nums[idx] == 0:
                memo[idx] = False
                return False

            for jmp in range(1, nums[idx] + 1):
                if idx + jmp < len(nums) and Fn(idx + jmp):
                    memo[idx] = True
                    return True

            memo[idx] = False
            return False

        return Fn(0)
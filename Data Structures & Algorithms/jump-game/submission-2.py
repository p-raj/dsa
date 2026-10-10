class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def Fn(idx: int) -> bool:
            if idx in memo:
                return memo[idx]

            if idx >= len(nums) - 1:
                memo[idx] = True
                return True

            if nums[idx] == 0:
                memo[idx] = False
                return False

            for jmp in range(nums[idx], 0, -1):
                if idx + jmp < len(nums) and Fn(idx + jmp):
                    memo[idx] = True
                    return True

            memo[idx] = False
            return False

        return Fn(0)
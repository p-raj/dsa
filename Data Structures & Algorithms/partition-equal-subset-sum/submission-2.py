class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}

        def Fn(i: int, curr_sum: int) -> bool:
            if curr_sum == target:
                return True

            if curr_sum > target:
                return False

            if i == len(nums):
                return False

            state = (i, curr_sum)
            if state in memo:
                return memo[state]

            take = Fn(i + 1, curr_sum + nums[i])
            skip = Fn(i + 1, curr_sum)

            memo[state] = take or skip
            return memo[state]

        return Fn(0, 0)
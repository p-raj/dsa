class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {}

        def fn(i: int, target: int) -> int:
            if i < 0:
                return 0

            key = (i, target)

            if key in memo:
                return memo[key]

            count = 0

            if nums[i] == target:
                count += 1

            count += fn(i - 1, target - nums[i])

            memo[key] = count
            return count

        ans = 0

        for i in range(len(nums)):
            ans += fn(i, k)

        return ans
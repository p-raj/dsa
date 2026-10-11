class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = [{} for _ in nums]
        ans = 0

        for i in range(len(nums)):
            # subarray consisting only of nums[i]
            dp[i][nums[i]] = dp[i].get(nums[i], 0) + 1

            # extend all subarrays ending at i - 1
            if i > 0:
                for sm, count in dp[i - 1].items():
                    new_sum = sm + nums[i]
                    dp[i][new_sum] = dp[i].get(new_sum, 0) + count

            ans += dp[i].get(k, 0)

        return ans
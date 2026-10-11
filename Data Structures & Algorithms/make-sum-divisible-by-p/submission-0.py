class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        sm = sum(nums)
        reminder = sm % p
        if not reminder:
            return 0
        count = len(prefix)
        for i in range(len(prefix)):
            for j in range(i + 1, len(prefix)):
                if prefix[j] - prefix[i] == reminder:
                    count = min(count, j - i)
        return count

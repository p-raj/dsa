class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            x = nums[i]

            # x is relevant if it belongs somewhere in [0, n-1].
            #
            # x should be stored at index x - 1.
            #
            # Also, don't swap if x is already present at its target.
            # This is essential for duplicates.
            if 1 <= x <= n and nums[x - 1] != x:
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
            else:
                i += 1
        # print(nums)
        # After placement:
        # if i+1 exists, it should be sitting at index i.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

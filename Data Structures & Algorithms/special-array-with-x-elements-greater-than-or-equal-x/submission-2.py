class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)

        for i in range(n):
            x = i + 1
            if nums[i] >= x:
                if (i == n - 1) or nums[i + 1] < x:
                    return x

        return -1


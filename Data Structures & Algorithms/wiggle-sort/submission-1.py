class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            if i % 2 == 1:
                # nums[i] should be a peak
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
            else:
                # nums[i] should be a valley
                if nums[i - 1] < nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        k = k % len_
        res = nums[k:] + nums[:k]
        nums[::] = res[::]
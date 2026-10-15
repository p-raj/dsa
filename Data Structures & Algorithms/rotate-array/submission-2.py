DBG = False
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        k %= len_

        def rev(strt: int, end: int):
            while strt < end:
                nums[strt], nums[end] = nums[end], nums[strt]
                strt += 1
                end -= 1

        rev(0, len_ - 1)
        DBG and print(nums)
        rev(0, k - 1)
        DBG and print(nums)
        rev(k, len_ - 1)
        DBG and print(nums)
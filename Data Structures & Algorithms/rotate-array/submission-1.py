class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        k = k % len_
        i = 0
        rot = []
        while i < k:
            rot.append(nums[len_ - i - 1])
            nums.pop()
            i += 1
        for n in rot:
            nums.insert(0, n)
        print(nums)

class NumArray:

    def prefix_calc(self):
        tot = 0
        for idx, num in enumerate(self.nums):
            tot += num
            self.pfx[idx] = tot

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.len_ = len(self.nums)
        self.pfx = [0] * self.len_
        self.prefix_calc()

    def sumRange(self, left: int, right: int) -> int:
        return self.pfx[right] - self.pfx[left] + self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
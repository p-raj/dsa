class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_ = len(nums)
        if len_ == 2:
            return [nums[1], nums[0]]
        res = [0] * len_
        pre = [0] * len_
        suf = [0] * len_
        
        pre[0] = suf[len_-1] = 1
        for i in range(1, len_):
            pre[i] = nums[i-1] * pre[i-1]
        for i in range(len_-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        for i in range(len_):
            res[i] = pre[i] * suf[i]
        return res
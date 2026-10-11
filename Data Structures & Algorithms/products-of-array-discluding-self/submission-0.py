class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        i = 0
        zeroes = [False] * len(nums)
        has_zeroes = False
        while i < len(nums):
            if nums[i]:
                product *= nums[i]
            else:
                has_zeroes = True
                zeroes[i] = True
            i += 1
        res = [0] * len(nums)
        i = 0
        while i < len(nums):
            if has_zeroes:
                if zeroes[i]:
                    res[i] = product
                else:
                    res[i] = 0
            else:
                res[i] = product//nums[i]
            i += 1
        return res
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        eve, odd = 0,1

        for num in nums:
            if num < 0:
                res[odd] = num
                odd += 2
            else:
                res[eve] = num
                eve += 2
        return res
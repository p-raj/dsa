class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        zer = 0
        pos = 0
        for num in nums:
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1
            else:
                zer += 1
            if zer:
                return 0
        return -1 if neg % 2 else 1
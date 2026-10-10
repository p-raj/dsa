from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        C = Counter(nums)
        for _, v in C.items():
            if v % 2 != 0:
                return False
        return True
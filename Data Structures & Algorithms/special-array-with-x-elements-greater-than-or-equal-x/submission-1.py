from collections import Counter
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        NC = Counter(nums)
        NC = dict(sorted(NC.items()))
        x = len(nums)
        while x > 0:
            if sum([v for k, v in NC.items() if k >= x]) == x:
                return x
            x -= 1
        return -1
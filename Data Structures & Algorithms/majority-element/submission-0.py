from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        c = Counter(nums)
        res = [k for k,v in c.items() if v >= n]
        return res[0]
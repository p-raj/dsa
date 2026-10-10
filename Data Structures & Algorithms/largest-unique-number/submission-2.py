class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        max_ = -1
        numsd = dict()
        for n in nums:
            if n not in numsd:
                numsd[n] = 0
            numsd[n] += 1
        for k, v in numsd.items():
            if v == 1 and k > max_:
                max_ = k
        return max_

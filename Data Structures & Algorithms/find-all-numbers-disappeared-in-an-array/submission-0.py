class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        S = set(nums)
        M = set(list(range(1,n+1)))
        M = M - S
        return list(M)
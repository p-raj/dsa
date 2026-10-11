class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e = []
        o = []
        for n in nums:
            if n % 2:
                o.append(n)
            else:
                e.append(n)
        return e + o
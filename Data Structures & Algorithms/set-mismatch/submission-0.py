class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        esm = (n * (n+1))//2
        asm = sum(nums)
        s = set()
        dupe = None
        for n in nums:
            if n in s:
                dupe = n
                break
            s.add(n)
        
        return [dupe, dupe+abs(esm-asm)]

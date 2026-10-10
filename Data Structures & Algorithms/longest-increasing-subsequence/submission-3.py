import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        soln = []
        for i in range(len(nums)):
            idx = bisect.bisect_left(soln, nums[i])
            if idx == len(soln):
                soln.append(nums[i])
            else:
                soln[idx] = nums[i]
        
        print(soln)
        return len(soln)
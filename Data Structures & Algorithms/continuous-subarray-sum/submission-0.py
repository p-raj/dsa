class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # brute force
        for lft in range(len(nums)-1):
            sm = nums[lft]
            for rgt in range(lft+1, len(nums)):
                sm += nums[rgt]
                if sm % k == 0:
                    return True
        return False
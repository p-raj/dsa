class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # brute force
        # for lft in range(len(nums)-1):
        #     sm = nums[lft]
        #     for rgt in range(lft+1, len(nums)):
        #         sm += nums[rgt]
        #         if sm % k == 0:
        #             return True
        # return False
        pfx = [0] * (len(nums))
        sm = 0
        for i in range(len(nums)):
            pfx[i] = sm + nums[i]
            sm = pfx[i]
        target = set()
        for i in range(len(nums)):
            t = pfx[i]%k
            if t in target:
                return True
            target.add(t)
        return False
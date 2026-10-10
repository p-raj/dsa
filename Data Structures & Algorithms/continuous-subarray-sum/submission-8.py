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
        if len(nums) < 2:
            return False
        pfx = [0] * (len(nums))
        sm = 0
        for i in range(len(nums)):
            pfx[i] = sm + nums[i]
            sm = pfx[i]
        target = dict()
        print(pfx)
        for idx, num in enumerate(nums):
            t = pfx[idx] % k
            if idx > 0 and t == 0:
                return True
            if t in target and abs(target[t] - idx) > 1:
                return True
            if t not in target:
                target[t] = idx
            # print(target)
        return False

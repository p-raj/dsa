class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        # lft = 0
        # while lft < len(nums):
        #     tot = 0
        #     rgt = lft
        #     while rgt < len(nums):
        #         tot += nums[rgt]
        #         rgt += 1
        #         if tot == k:
        #             res += 1
        #     lft += 1
        # pfx = [0] * len(nums)
        # pfx[0] = nums[0]
        # for idx, num in enumerate(nums):
        #     if idx == 0:
        #         continue
        #     pfx[idx] = pfx[idx-1] + num
        # print(pfx)
        # return res

        # Algorithm: running prefix
        # how many prefix sum can we remove to match
        # total to k
        pfx = {0: 1}
        tot = 0
        for num in nums:
            tot += num
            res += pfx.get(tot-k, 0)
            pfx[tot] = pfx.get(tot, 0) + 1

        return res

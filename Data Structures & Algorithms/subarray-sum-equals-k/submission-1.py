class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = []
        counter = 0
        lft = 0
        while lft < len(nums):
            sm = 0
            rgt = lft
            while rgt < len(nums):
                sm += nums[rgt]
                if sm == k:
                    # res.append(nums[lft: rgt+1])
                    counter += 1
                rgt += 1
            lft += 1
        return counter
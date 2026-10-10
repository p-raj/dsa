class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        lft = 0
        i = []
        d = []
        while lft < len(nums):
            cur = nums[lft]
            istack = [cur]
            dstack = [cur]
            rgt = lft + 1
            while rgt < len(nums) and dstack[-1] > nums[rgt]:
                dstack.append(nums[rgt])
                rgt += 1
            rgt = lft + 1
            while rgt < len(nums) and istack[-1] < nums[rgt]:
                istack.append(nums[rgt])
                rgt += 1
            i.append(istack)
            d.append(dstack)
            lft += 1
        mx = max(len(_) for _ in i)
        mx = max(mx, max(len(_) for _ in d))
        return mx

class Solution:
    def check(self, nums: List[int]) -> bool:
        lft = 0
        rgt = len(nums) - 1
        brl = True
        brr = True
        while (lft < len(nums) - 1 and rgt > 0) and (brl or brr):
            if nums[lft] <= nums[lft + 1]:
                lft += 1
            else:
                brl = False
            if nums[rgt - 1] <= nums[rgt]:
                rgt -= 1
            else:
                brr = False
        print(lft, rgt)
        # rgt is the rotation
        if lft >= rgt:
            return True
        if abs(rgt-lft) > 1:
            return False
        return nums[0] >= nums[-1]
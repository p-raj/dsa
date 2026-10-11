class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lft = 0
        rgt = 0
        while True:
            while lft < len(nums) and nums[lft] != val:
                lft += 1
            if lft >= len(nums) - 1:
                break
            rgt = lft + 1
            while rgt < len(nums) and nums[rgt] == val:
                rgt += 1
            if rgt >= len(nums):
                break
            nums[lft], nums[rgt] = nums[rgt], nums[lft]
            lft += 1
        return len(nums) - (rgt-lft)

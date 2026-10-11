DBG = False
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lft, rgt = 0, 0
        uniq = 0
        while rgt < len(nums):
            uniq += 1
            DBG and print(nums, uniq)
            while rgt < len(nums) and nums[lft] == nums[rgt]:
                rgt += 1
            if lft == rgt:
                lft += 1
                rgt += 1
                continue
            if lft > len(nums) - uniq:
                break
            if rgt < len(nums):
                nums[lft+1] = nums[rgt]
            lft += 1
        return uniq
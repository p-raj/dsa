class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lft, rgt = 0, 0
        uniq = 0
        while rgt < len(nums):
            while rgt < len(nums) and nums[lft] == nums[rgt]:
                rgt += 1
            if lft == rgt:
                lft += 1
                rgt += 1
                continue
            if lft == len(nums) - uniq:
                break
            uniq += 1
            if rgt < len(nums):
                nums[lft+1] = nums[rgt]
            lft += 1
        return uniq
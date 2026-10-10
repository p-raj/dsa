class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        rgt = len_ - 1
        while rgt >= 0:
            lft = rgt
            while lft >= 0 and nums[lft] > 0:
                lft -= 1
            if lft < 0:
                break
            diff = rgt - lft
            print(f"{lft=}, {rgt=}, {diff=}")
            print(nums)
            while lft != rgt:
                nums[lft] = nums[lft + 1]
                lft += 1
                print(">>|", nums)
            nums[lft] = 0
            print("||", nums)
            rgt -= 1
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        spl = True
        idx = 0
        while idx < len(nums) - 1:
            spl = (nums[idx] % 2 == 0 and nums[idx + 1] % 2 == 1) or (
                nums[idx] % 2 == 1 and nums[idx + 1] % 2 == 0
            )
            if not spl:
                return spl
            idx += 1
        return spl

DBG = False
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        min_ = min(nums)
        nums = [i-min_ for i in nums]
        
        proc = set()
        idx = 0
        while idx < len(nums):
            num = nums[idx]
            if num in proc or num >= len(nums):
                return False
            if idx == num:
                idx += 1
                proc.add(num)
            else:
                nums[idx], nums[num] = nums[num], nums[idx]
            DBG and print(nums, idx)
        return True

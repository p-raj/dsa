class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majority = count = 0
        for num in nums:
            if count == 0:
                majority = num
                count = 1
            elif majority == num:
                count += 1
            else:
                count -= 1
        
        lft_maj, right_maj = 0, nums.count(majority)
        for i in range(len(nums)):
            if nums[i] == majority:
                lft_maj += 1
                right_maj -= 1
            
            if 2 * lft_maj > (i + 1) and 2 * right_maj > (len(nums) - i - 1):
                return i
        return -1


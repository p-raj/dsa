class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end = 0
        while end < len(nums):
            start = end + 1
            while start < len(nums):
                sum_ = nums[start] + nums[end]
                print(f"{sum_=}, {target=}, {start=}, {end=}, {nums[start]=}, {nums[end]=}")
                if sum_ == target:
                    return [end, start]
                start += 1
            end += 1
        

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end = len(nums) - 1
        start = 0
        while start < end:
            sum_ = nums[start] + nums[end]
            print(f"{sum_=}, {target=}, {start=}, {end=}, {nums[start]=}, {nums[end]=}")
            if sum_ == target:
                break
            elif target < sum_:
                end -= 1
            else:
                start += 1
        return [start, end]

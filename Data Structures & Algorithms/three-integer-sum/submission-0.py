class Solution:
    def twoSum(self, start: int, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        fst, lst = start, len(nums)-1
        while fst < lst:
            sum_ = nums[fst] + nums[lst]
            if sum_ == target:
                return [fst, lst]
            elif sum_ > target:
                lst -= 1
            else:
                fst += 1
        return [None, None]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = set()
        for idx, num in enumerate(nums):
            target = 0 - num
            fst, lst = self.twoSum(idx+1, nums, target)
            if fst and lst:
                solutions.add((num, nums[fst], nums[lst]))
        return list(solutions)
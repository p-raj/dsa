class Solution:
    def twoSum(self, start: int, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        fst, lst = start, len(nums)-1
        res = []
        while fst < lst:
            sum_ = nums[fst] + nums[lst]
            if sum_ == target:
                res.append([fst, lst])
                fst += 1
            elif sum_ > target:
                lst -= 1
            else:
                fst += 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = set()
        for idx, num in enumerate(nums):
            target = 0 - num
            fst_lst = self.twoSum(idx+1, nums, target)
            for (fst, lst) in fst_lst:
                solutions.add((num, nums[fst], nums[lst]))
        return list(solutions)
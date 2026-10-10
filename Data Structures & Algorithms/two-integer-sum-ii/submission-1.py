class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        fst, lst = 0, len(nums)-1
        while fst < lst:
            sum_ = nums[fst] + nums[lst]
            if sum_ == target:
                return [fst+1, lst+1]
            elif sum_ > target:
                lst -= 1
            else:
                fst += 1
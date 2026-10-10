from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def comparator(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0
        
        nums.sort(key=cmp_to_key(comparator))
        result = "".join(nums)
        if result[0] == "0":
            return "0"
        return result
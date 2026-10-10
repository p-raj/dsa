class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [0] * (2 * len(nums))
        for idx, val in enumerate(nums):
            arr[idx] = val
            arr[idx+len(nums)] = val
        return arr
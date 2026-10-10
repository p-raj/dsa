from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        NC = Counter(nums)
        third = math.floor(len(nums)/3)
        return [
            k for k,v in NC.items() if v > third
        ]
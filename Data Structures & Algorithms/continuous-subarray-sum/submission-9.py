class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # cleaner solution
        prefix = 0
        seen = {0: -1}
        for idx, num in enumerate(nums):
            prefix += num
            target = prefix % k
            if target in seen:
                if idx - seen[target] >= 2:
                    return True
            if target not in seen:
                seen[target] = idx
        return False
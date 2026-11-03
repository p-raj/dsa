class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        prev_idx = {}

        for idx, num in enumerate(nums):
            if num not in prev_idx:
                prev_idx[num] = idx
            else:
                if abs(idx - prev_idx[num]) <= k:
                    return True
                else:
                    prev_idx[num] = idx
        return False
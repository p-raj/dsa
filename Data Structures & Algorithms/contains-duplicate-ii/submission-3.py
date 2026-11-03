class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        lft = 0

        for rgt in range(len(nums)):
            if rgt - lft > k:
                # limit exceeded
                window.remove(nums[lft])
                lft += 1
            if nums[rgt] in window:
                return True
            window.add(nums[rgt])
        return False

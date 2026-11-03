class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        lft = 0

        for rgt in range(len(nums)):
            if rgt - lft > k:
                # limit exceeded
                nums[lft] in window and window.remove(nums[lft])
            if nums[rgt] in window:
                return True
            window.add(nums[rgt])
        return False
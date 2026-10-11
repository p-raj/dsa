class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def ms(nums, lft, rgt):
            if lft >= rgt:
                return lft
            mid = (lft + rgt)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target and nums[mid] < nums[rgt]:
                return ms(nums, mid+1, rgt)
            elif nums[mid] < target and nums[mid] > nums[rgt]:
                return ms(nums, lft, mid-1)
            elif nums[mid] > target and nums[mid] < nums[rgt]:
                return ms(nums, lft, mid-1)
            else:
                return ms(nums, mid+1, rgt)
        idx = ms(nums, 0, len(nums)-1)
        return idx if nums[idx] == target else -1

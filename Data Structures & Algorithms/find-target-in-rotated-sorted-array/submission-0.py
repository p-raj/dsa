class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def ms(nums, lft, rgt):
            if lft >= rgt:
                return rgt
            mid = (lft + rgt)//2
            if target == nums[mid]:
                return mid
            elif nums[mid] < nums[rgt]:
                return ms(nums, lft, mid-1)
            else:
                return ms(nums, mid+1, rgt)
        idx = ms(nums, 0, len(nums)-1)
        return -1 if nums[idx] != target else idx
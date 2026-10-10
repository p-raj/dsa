class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def ms(nums, lft, rgt):
            if lft >= rgt:
                return lft
            mid = (lft + rgt) // 2
            if target == nums[mid]:
                return mid
            if nums[lft] <= nums[mid]:
                if target > nums[mid] or target < nums[lft]:
                    return ms(nums, mid+1, rgt)
                else:
                    return ms(nums, lft, mid-1)
            else:
                if target < nums[mid] or target > nums[rgt]:
                    return ms(nums, lft, mid-1)
                else:
                    return ms(nums, mid+1, rgt)

        idx = ms(nums, 0, len(nums) - 1)
        return idx if nums[idx] == target else -1

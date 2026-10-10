class Solution:
    def findMin(self, nums: List[int]) -> int:
        def ms(nums, lft, rgt):
            if lft >= rgt:
                return nums[lft]
            mid = (lft+rgt)//2
            if nums[mid] < nums[rgt]:
                return min(nums[mid], ms(nums, lft, mid-1))
            else:
                return min(nums[mid], ms(nums, mid+1, rgt))
            # this is O(n)
            # return min(nums[mid], ms(nums, lft, mid-1), ms(nums, mid+1, rgt))
        return ms(nums, 0, len(nums)-1)

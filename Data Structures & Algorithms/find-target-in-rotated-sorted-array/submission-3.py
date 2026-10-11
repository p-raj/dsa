class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def ms(nums, lft, rgt):
            if lft >= rgt:
                return lft
            mid = (lft + rgt)//2
            if target == nums[mid]:
                return mid
            elif target == nums[rgt]:
                return rgt
            elif target == nums[lft]:
                return lft
            elif target < nums[rgt]:
                return ms(nums, mid+1, rgt)
            else:
                return ms(nums, lft, mid-1)

        idx = ms(nums, 0, len(nums)-1)
        print(idx)
        return idx if nums[idx] == target else -1

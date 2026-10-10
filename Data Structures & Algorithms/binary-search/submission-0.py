class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bins(arr, lft, rgt):
            if lft > rgt:
                return -1
            mid = (lft + rgt)//2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                return bins(arr, lft, mid-1)
            else:
                return bins(arr, mid+1, rgt)
        return bins(nums, 0, len(nums)-1)
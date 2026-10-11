class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def qpart(arr: List[int], lft: int, rgt: int) -> int:
            pivot_idx = rgt
            pivot = arr[pivot_idx]

            rgt -= 1

            while lft <= rgt:
                if arr[lft] < pivot:
                    arr[lft], arr[rgt] = arr[rgt], arr[lft]
                    rgt -= 1
                else:
                    lft += 1

            arr[lft], arr[pivot_idx] = arr[pivot_idx], arr[lft]
            return lft
        
        def quickselect(arr: List[int], lft: int, rgt: int, k:int):
            if lft <= rgt:
                # Partition the array around a pivot
                pivot_idx = qpart(arr, lft, rgt)
                
                # If pivot is exactly at index k, the first k elements are found
                if pivot_idx == k:
                    return
                # If pivot index is greater than k, look left
                elif pivot_idx > k:
                    quickselect(arr, lft, pivot_idx - 1, k)
                # If pivot index is less than k, look right
                else:
                    quickselect(arr, pivot_idx + 1, rgt, k)
        
        quickselect(nums, 0, len(nums)-1, k)
        return nums[k-1]
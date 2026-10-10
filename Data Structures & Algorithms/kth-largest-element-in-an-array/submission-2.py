import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def qpart(arr, lft, rgt):
            rand_idx = random.randint(lft, rgt)
            arr[rand_idx], arr[rgt] = arr[rgt], arr[rand_idx]

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

        target = k - 1
        lft, rgt = 0, len(nums) - 1

        while lft <= rgt:
            pivot_idx = qpart(nums, lft, rgt)

            if pivot_idx == target:
                return nums[pivot_idx]
            elif pivot_idx > target:
                rgt = pivot_idx - 1
            else:
                lft = pivot_idx + 1
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # Approach 1: pivot value
        len_ = len(arr)
        idx = len_ - 1
        running_max = -1
        while idx > -1:
            prv_, nxt_ = arr[idx], running_max
            arr[idx] = nxt_
            running_max = max(running_max, prv_)
            idx -= 1
        return arr
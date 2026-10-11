class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        idx = 1
        no_changes = 0
        while True:
            if idx == len(arr) - 1:
                idx = 1
                continue
            if arr[idx] > arr[idx - 1] and arr[idx] > arr[idx + 1]:
                arr[idx] -= 1
            elif arr[idx] < arr[idx - 1] and arr[idx] < arr[idx + 1]:
                arr[idx] += 1
            else:
                no_changes += 1
            idx += 1
            if no_changes >= len(arr):
                break
        return arr

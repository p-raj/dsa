class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        idx = 1
        mx = len(arr)
        while mx:
            if idx == len(arr) - 1:
                idx = 1
                mx -= 1
            else:
                if arr[idx] > arr[idx - 1] and arr[idx] > arr[idx + 1]:
                    arr[idx] -= 1
                elif arr[idx] < arr[idx - 1] and arr[idx] < arr[idx + 1]:
                    arr[idx] += 1
                idx += 1
        return arr

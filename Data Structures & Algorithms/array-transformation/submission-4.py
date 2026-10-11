class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        idx = 1
        mx = -1
        for idx in range(1, len(arr)-1):
            mx = max(
                mx,
                abs(arr[idx] - arr[idx - 1]),
                abs(arr[idx] - arr[idx + 1]),
            )
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

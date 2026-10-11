class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        idx = 1
        sm = sum(arr)
        psm = None
        while True:
            if idx == len(arr) - 1:
                idx = 1
                psm = sm
                continue
            if arr[idx] > arr[idx - 1] and arr[idx] > arr[idx + 1]:
                arr[idx] -= 1
                sm -= 1
            elif arr[idx] < arr[idx - 1] and arr[idx] < arr[idx + 1]:
                arr[idx] += 1
                sm += 1
            idx += 1
            if psm == sm:
                break
        return arr

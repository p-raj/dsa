class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        idx = 1
        changed = True
        checked_all = False
        while changed:
            if idx == len(arr)-1:
                idx = 1
                checked_all = True
                continue
            if arr[idx] > arr[idx-1] and arr[idx] > arr[idx+1]:
                arr[idx] -= 1
                checked_all = False
            elif arr[idx] < arr[idx-1] and arr[idx] < arr[idx+1]:
                arr[idx] += 1
                checked_all = False
            else:
                changed = not checked_all and idx < len(arr)-1
            idx += 1
        
        return arr
class Solution:
    def countElements(self, arr: List[int]) -> int:
        d = {
            idx: val for val, idx in enumerate(arr)
        }
        cnt = 0
        for i in range(len(arr)):
            if arr[i]+1 in d:
                cnt += 1
        return cnt
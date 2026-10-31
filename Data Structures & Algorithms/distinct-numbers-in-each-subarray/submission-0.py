class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        arr = [0] * 100001
        unq = 0
        res = []

        for i in range(k):
            if arr[i] == 0:
                unq += 1
            arr[i] += 1
        
        res.append(unq)
        for i in range(k, len(nums)):
            # going out
            x == i - k
            arr[x] -= 1
            if arr[x] == 0:
                unq -= 1
            # coming in
            if arr[k] == 0:
                unq += 1
            arr[k] += 1
            res.append(unq)
        
        return res
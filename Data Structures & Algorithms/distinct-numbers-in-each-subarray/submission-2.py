class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        arr = [0] * 100001
        unq = 0
        res = []

        for i in range(k):
            num = nums[i]
            if arr[num] == 0:
                unq += 1
            arr[num] += 1
        
        res.append(unq)
        for i in range(k, len(nums)):
            # going out
            x = i - k
            xnum = nums[x]
            arr[xnum] -= 1
            if arr[xnum] == 0:
                unq -= 1
            
            # coming in
            inum = nums[i]
            if arr[inum] == 0:
                unq += 1
            arr[inum] += 1
            res.append(unq)
        
        return res
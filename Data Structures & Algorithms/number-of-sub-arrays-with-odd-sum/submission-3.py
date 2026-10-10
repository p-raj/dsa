class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        prefix = 0
        evn = 1
        odd = 0
        res = 0
        for num in arr:
            prefix += num

            # odd
            if prefix % 2:
                res += evn
                odd += 1
            # even
            else:
                res += odd
                evn += 1
        
        return res
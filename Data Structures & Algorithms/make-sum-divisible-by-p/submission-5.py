class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # A mod B = R (remainder)
        # congruent modulo
        # A = B (mod n) <=> B = A (mod n)
        # that n divides a - b
        # a - b = k * n
        res = len(nums)  # invalid state, remove all
        pfx = {0: -1}
        tot = 0
        rem = sum(nums) % p
        if rem == 0:
            return 0
        # figure out the closes prefix
        # to the running sum
        # figure out smallest (a - b = k * n)
        for idx, num in enumerate(nums):
            tot += num
            target = (tot - rem) % p
            if target in pfx:
                res = min(res, (idx - pfx[target]))
            pfx[tot % p] = idx
        return -i if res == len(nums) else res

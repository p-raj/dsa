from collections import Counter

DEBUG = False


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        NC = Counter(nums)
        ops = 0
        DEBUG and print(f"{NC=}")
        for k, v in NC.items():
            DEBUG and print(f"key | {k=} {v=}")
            if v == 0:
                continue
            if v % 3 == 1:
                DEBUG and print(f"1.V%3 | {v=} {v%3=}")
                c = v // 3
                c -= 1
                if c > 1:
                    ops += c
                    v -= c * 3
                DEBUG and print(f"1.V3> | {v=} {ops=}")
            if v % 3 in (0, 2):
                DEBUG and print(f"02.V%3 | {v=} {v%3=}")
                c = v // 3
                ops += c
                v -= c * 3
                DEBUG and print(f"02.V3> | {v=} {ops=}")
            if v == 0:
                continue
            if v % 2 in (0, 3):
                DEBUG and print(f"02.V%2 | {v=} {v%2=}")
                c = v // 2
                ops += c
                v -= c * 2
                DEBUG and print(f"02.V2> | {v=} {ops=}")
            if v == 0:
                continue
            if v % 2 == 1 or v % 3 == 1:
                return -1
        return ops

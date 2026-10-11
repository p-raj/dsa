from functools import cache

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def first_digit(n):
            return int(str(n)[0])

        def solve_bucket(bucket):
            bucket = list(map(str, bucket))
            n = len(bucket)
            ALL = (1 << n) - 1

            @cache
            def dp(mask):
                if mask == ALL:
                    return ""

                best = ""

                for i in range(n):
                    if mask & (1 << i):
                        continue

                    candidate = bucket[i] + dp(mask | (1 << i))
                    best = max(best, candidate)

                return best

            return dp(0)

        # Bucket by first digit
        buckets = {i: [] for i in range(10)}

        for num in nums:
            buckets[first_digit(num)].append(num)

        result = ""

        # First digit determines order between buckets.
        for digit in range(9, -1, -1):
            if buckets[digit]:
                result += solve_bucket(buckets[digit])

        return "0" if result[0] == "0" else result
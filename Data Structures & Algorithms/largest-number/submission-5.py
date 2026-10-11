from functools import cache

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        n = len(nums)
        ALL = (1 << n) - 1

        @cache
        def dp(mask):
            # All numbers have been used.
            if mask == ALL:
                return ""

            best = ""

            for i in range(n):
                # Already used.
                if mask & (1 << i):
                    continue

                # Choose nums[i] next.
                candidate = nums[i] + dp(mask | (1 << i))

                if candidate > best:
                    best = candidate

            return best

        ans = dp(0)

        # [0,0,0] -> "000" -> "0"
        return "0" if ans[0] == "0" else ans
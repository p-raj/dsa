from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        C = defaultdict(int)
        unq = 0
        lft = 0
        count = 0
        prefix = 0

        def grow(end):
            nonlocal unq

            num = nums[end]

            if C[num] == 0:
                unq += 1

            C[num] += 1

        def shrink():
            nonlocal lft, unq, prefix

            # Too many distinct integers:
            # advance left until the window is valid.
            while unq > k:
                num = nums[lft]
                C[num] -= 1

                if C[num] == 0:
                    unq -= 1

                lft += 1

                # Previous valid starting positions
                # cannot be reused after this change.
                prefix = 0

            # Remove redundant occurrences while
            # preserving the same number of distinct values.
            while unq == k and C[nums[lft]] > 1:
                C[nums[lft]] -= 1
                lft += 1
                prefix += 1

        for end in range(len(nums)):
            grow(end)
            shrink()

            if unq == k:
                count += prefix + 1

        return count
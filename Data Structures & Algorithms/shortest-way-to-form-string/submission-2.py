import bisect
from collections import defaultdict


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if not target:
            return 0

        positions = defaultdict(list)

        for i, ch in enumerate(source):
            positions[ch].append(i)

        count = 1
        pos = -1

        for ch in target:
            if ch not in positions:
                return -1

            indices = positions[ch]

            j = bisect.bisect_right(indices, pos)

            if j == len(indices):
                # Need a new source subsequence.
                count += 1
                pos = indices[0]
            else:
                pos = indices[j]

        return count
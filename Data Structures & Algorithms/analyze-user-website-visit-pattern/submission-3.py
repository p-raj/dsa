from collections import defaultdict
import itertools


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:

        arr = sorted(zip(timestamp, username, website))

        map_ = defaultdict(list)
        for _, u, w in arr:
            map_[u].append(w)

        patterns = defaultdict(int)

        for u, lw in map_.items():
            n = len(lw)

            if n < 3:
                continue

            # Unique patterns for this user
            user_patterns = set()

            # Generate all subsequences of length 3
            # for i in range(n):
            #     for j in range(i + 1, n):
            #         for k in range(j + 1, n):
            #             tup = (lw[i], lw[j], lw[k])
            #             user_patterns.add(tup)
            user_patterns = set(itertools.combinations(lw, 3))
            # Each user contributes at most 1
            # to the score of a given pattern
            for tup in user_patterns:
                patterns[tup] += 1

        # Maximum score, then lexicographically smallest
        best = min(patterns, key=lambda p: (-patterns[p], p))

        return list(best)

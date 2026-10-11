from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = defaultdict(int)
        for row in wall:
            gap = 0
            for cidx, col in enumerate(row):
                if cidx == len(row) - 1:
                    break
                gap += col
                gaps[gap] += 1
        gaps = dict(sorted(gaps.items(), key=lambda items: items[1], reverse=True))
        return (len(wall) - next(iter(gaps), 0))

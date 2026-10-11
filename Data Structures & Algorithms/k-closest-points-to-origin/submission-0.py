import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort()
        res = []
        for p in points:
            # sqrt((x1 - x2)^2 + (y1 - y2)^2))
            # d = math.sqrt(((0 - p[0]) ** 2) + ((0 - p[1]) ** 2))
            res.append(p)
            if len(res) >= k:
                break
        return res

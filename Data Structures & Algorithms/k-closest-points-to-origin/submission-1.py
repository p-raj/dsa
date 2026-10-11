import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort()
        res = []
        for p in points:
            # sqrt((x1 - x2)^2 + (y1 - y2)^2))
            d = math.sqrt(((0 - p[0]) ** 2) + ((0 - p[1]) ** 2))
            dres = None
            if len(res):
                dres = math.sqrt(((res[0][0] - p[0]) ** 2) + ((res[0][1] - p[1]) ** 2))
            if len(res) < k:
                heapq.heappush_max(res, p)
            else:
                if d < dres:
                    heapq.heappop_max(res)
                    heapq.heappush_max(res, p)

        return res

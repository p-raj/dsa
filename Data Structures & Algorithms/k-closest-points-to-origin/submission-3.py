import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for p in points:
            dmax = None
            d = math.sqrt(((0 - p[0]) ** 2) + ((0 - p[1]) ** 2))
            if len(res):
                dmax = res[0][0]

            if len(res) < k:
                heapq.heappush_max(res, (d,p))
            else:
                if d <= dmax:
                    heapq.heappop_max(res)
                    heapq.heappush_max(res, (d,p))

        return [r[1] for r in res]

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x == y:
                continue
            delta = abs(x-y)
            heapq.heappush_max(stones, delta)
        print(stones)
        return stones[0] if len(stones) > 0 else 0 
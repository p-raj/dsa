from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = defaultdict(int)
        for n in nums:
            f[n] += 1
        heap = []
        
        counter = 0
        for i,c in f.items():
            if counter < k:
                heapq.heappush(heap, (c,i))
            if counter >= k and c > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (c,i))
            counter += 1
        return [h[1] for h in heap]
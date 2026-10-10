import heapq


class KthLargest:
    def _process(self, num):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, num)
        else:
            if num > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        # kth largest needed
        # reverse sorted list
        # choose kth
        # choose smallest in k-heap
        for num in nums:
            self._process(num)

    def add(self, val: int) -> int:
        self._process(val)
        return self.heap[0]

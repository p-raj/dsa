import heapq
class MedianFinder:

    def __init__(self):
        # keep the smaller elements
        self.max_hp = []
        # keep the bigger elements
        self.min_hp = []

    def rebalance(self):
        if len(self.min_hp) > len(self.max_hp):
            heapq.heappush_max(self.max_hp, heapq.heappop(self.min_hp))
        else:
            heapq.heappush(self.min_hp, heapq.heappop_max(self.max_hp))

    def addNum(self, num: int) -> None:
        if self.min_hp and self.min_hp[0] < num:
            heapq.heappush(self.min_hp, num)
        else:
            heapq.heappush_max(self.max_hp, num)

        if abs(len(self.min_hp) - len(self.max_hp)) > 1:
            self.rebalance()

    def findMedian(self) -> float:
        if len(self.max_hp) == len(self.min_hp):
            return (self.max_hp[0] + self.min_hp[0])/2
        if len(self.max_hp) > len(self.min_hp):
            return self.max_hp[0]
        else:
            return self.min_hp[0]
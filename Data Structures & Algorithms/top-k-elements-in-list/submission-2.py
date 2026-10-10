from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) # on
        tup = [(-v, k)  for k,v in freq.items()] # on
        heapq.heapify(tup) # on
        res = []
        while k > 0 and tup: # klogn
            _, i = heapq.heappop(tup)
            res.append(i)
            k -= 1
        return res
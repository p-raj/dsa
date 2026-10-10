from collections import Counter
import heapq
class Solution:
    def maxDifference(self, s: str) -> int:
        C = Counter(s)
        odd = []
        evn = []
        for k,v in C.items():
            if v % 2:
                odd.append(v)
            else:
                evn.append(v)
        heapq.heapify(evn)
        heapq.heapify_max(odd)
        return odd[0]-evn[0]
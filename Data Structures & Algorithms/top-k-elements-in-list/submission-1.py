from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = defaultdict(int)
        for n in nums:
            f[n] += 1
        f = dict(sorted(f.items(), key=lambda item: item[1], reverse=True))
        soln = []
        counter = 0
        for n in f:
            soln.append(n)
            counter += 1
            if counter == k:
                return soln

class Solution:
    def findKthLargest(self, nums, k):
        res = []
        for n in nums:
            heapq.heappush(res, n)

            if len(res) > k:
                heapq.heappop(res)
        
        return res[0]
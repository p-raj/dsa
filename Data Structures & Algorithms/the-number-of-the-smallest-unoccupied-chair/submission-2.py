import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrivals = sorted((start, end, friend) for friend, (start, end) in enumerate(times))

        occupied = []
        heapq.heapify(occupied)
        available = []
        heapq.heapify(available)
        next_chair = 0

        for s, e, f in arrivals:
            while occupied and occupied[0][0] <= s:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(available, chair)

            if available:
                chair = heapq.heappop(available)
            else:
                chair = next_chair
                next_chair += 1

            if f == targetFriend:
                return chair
            
            heapq.heappush(occupied, (e, chair))

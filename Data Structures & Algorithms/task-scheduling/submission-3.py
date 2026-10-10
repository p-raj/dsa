from collections import deque, Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        q = deque()
        heap = [(c, t) for t, c in freq.items()]
        heapq.heapify_max(heap)
        timer = 0

        while q or heap:
            timer += 1
            print(timer, q, heap)
            if heap:
                c, t = heapq.heappop_max(heap)
                c -= 1
                if c:
                    # cooldown for n slots
                    q.append((timer + n, c, t))

            if q and q[0][0] == timer:
                _, c, t = q.popleft()
                heapq.heappush_max(heap, (c, t))

        return timer

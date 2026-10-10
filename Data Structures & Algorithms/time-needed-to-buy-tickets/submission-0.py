class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        idx = 0
        time = 0
        while True:
            while tickets[idx] == 0:
                idx += 1
                idx %= len(tickets)
            if tickets[idx] >= 0:
                tickets[idx] -= 1
                time += 1
            if idx == k and tickets[k] == 0:
                return time
            idx += 1
            idx %= len(tickets)
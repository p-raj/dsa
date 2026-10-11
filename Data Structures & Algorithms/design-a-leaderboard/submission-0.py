import heapq

class Leaderboard:

    def __init__(self):
        self.p = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.p[playerId] = score

    def top(self, K: int) -> int:
        scores = list(self.p.values())
        heapq.heapify_max(scores)
        score = 0
        while scores and K:
            score += heapq.heappop_max(scores)
            K -= 1
        return score

    def reset(self, playerId: int) -> None:
        del self.p[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

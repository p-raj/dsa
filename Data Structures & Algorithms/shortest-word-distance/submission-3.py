class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        W = {}
        WS = set([word1, word2])
        for idx, w in enumerate(wordsDict):
            if w in WS:
                if w not in W:
                    W[w] = list()
                W[w].append(idx)
        return min(
            abs(W[word1][0] - W[word2][0]),
            abs(W[word1][-1] - W[word2][-1]),
            abs(W[word1][-1] - W[word2][0]),
            abs(W[word1][0] - W[word2][-1]),
        )
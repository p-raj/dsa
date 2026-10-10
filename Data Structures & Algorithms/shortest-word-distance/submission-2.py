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
            abs(min(W[word1]) - min(W[word2])),
            abs(max(W[word1]) - max(W[word2])),
            abs(max(W[word1]) - min(W[word2])),
            abs(min(W[word1]) - max(W[word2])),
        )
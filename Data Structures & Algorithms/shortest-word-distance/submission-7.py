class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        W = {
            word1: [None,float("inf")],
            word2: [None,float("inf")]
        }
        for idx, w in enumerate(wordsDict):
            if w in W:
                if W[w][0] is None:
                    W[w][0] = idx
                W[w][1] = idx
        return min(
            abs(W[word1][0] - W[word2][0]),
            abs(W[word1][-1] - W[word2][-1]),
            abs(W[word1][-1] - W[word2][0]),
            abs(W[word1][0] - W[word2][-1]),
        )
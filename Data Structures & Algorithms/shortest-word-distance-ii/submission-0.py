from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.d[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        w1 = self.d[word1]
        w2 = self.d[word2]
        mind = float('inf')
        for i in w1:
            for j in w2:
                if abs(i-j) < mind:
                    mind = abs(i-j)
        return mind


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

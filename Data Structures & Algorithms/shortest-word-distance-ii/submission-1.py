class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        

    def shortest(self, word1: str, word2: str) -> int:
        idx1 = -1
        idx2 = -1

        res = len(self.wordsDict)

        for i in range(len(self.wordsDict)):
            if word1 == self.wordsDict[i]:
                idx1 = i
            if word2 == self.wordsDict[i]:
                idx2 = i
            
            if idx1 != -1 and idx2 != -1:
                res = min(res, abs(idx1-idx2))
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

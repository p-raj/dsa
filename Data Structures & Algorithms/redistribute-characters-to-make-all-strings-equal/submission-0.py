from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        l = len(words)
        s = "".join(words)
        W = Counter(s)
        return all(v%l == 0 for v in W.values())
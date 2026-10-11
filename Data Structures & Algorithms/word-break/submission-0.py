class TriNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TriNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TriNode()
            cur = cur.children[ch]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = PrefixTree()
        for w in wordDict:
            words.insert(w)

        memo = {}
        memo[(0,0)] = True
        def dp(lft: int, rgt: int) -> bool:
            key = (lft, rgt)
            if key in memo:
                return memo[key]
            if lft >= len(s) or rgt >= len(s):
                return True
            memo[key] = dp(lft, rgt+1) or dp(rgt+1, rgt+2)
            return memo[key]
        
        return dp(0,1)
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

        def dp(lft: int) -> bool:
            # dp(lft) means:
            # can s[lft:] be segmented into dictionary words?

            if lft in memo:
                return memo[lft]

            if lft == len(s):
                return True

            for rgt in range(lft + 1, len(s) + 1):
                substr = s[lft:rgt]
                if not words.startsWith(substr):
                    break
                if words.search(substr) and dp(rgt):
                    memo[lft] = True
                    return True

            memo[lft] = False
            return False

        return dp(0)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=lambda x: len(x))
        res = []
        cur = 0
        while cur < len(words)-1:
            w = words[cur]
            nxt = cur + 1
            while nxt < len(words):
                if words[cur] in words[nxt]:
                    res.append(words[cur])
                    break
                nxt += 1
            cur += 1
        return res
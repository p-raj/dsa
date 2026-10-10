class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        V = set("aeiou")
        pfx = [0] * len(words)
        valid = list(map(lambda x: x[0] in V and x[-1] in V, words))
        for idx, bul in enumerate(valid):
            if bul:
                pfx[idx] = pfx[idx - 1] + 1
            else:
                pfx[idx] = pfx[idx - 1]
        res = []
        for s, e in queries:
            res.append(pfx[e] - pfx[s] + (1 if valid[s] else 0))
        return res

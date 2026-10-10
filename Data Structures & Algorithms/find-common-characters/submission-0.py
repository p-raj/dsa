from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        WC = [Counter(w) for w in words]
        store = []
        for ch in WC[0]:
            mn = float('inf')
            for wc in WC:
                mn = min(mn, wc.get(ch, 0))
            store.append((ch, mn))
        res = []
        for ch, cnt in store:
            res += [ch] * cnt
        return res

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case
        if len(t) > len(s):
            return ""
        cs = Counter(s)
        ct = Counter(t)
        # basic sanity
        for k, v in ct.items():
            if k not in cs or v > cs[k]:
                return ""
        # full match
        if cs == ct:
            return s
        end, strt = 0, 0
        min_win = len(s)
        min_win_idx = [0, len(s)]
        while strt < len(s):
            # scan right to first match
            while strt < len(s) and s[strt] not in ct:
                strt += 1
            # start gathering
            c = {}
            end = strt
            while end < len(s) and c != ct:
                # can be simplified
                if s[end] in ct and s[end] not in c:
                    c[s[end]] = 0
                if s[end] in ct and s[end] in c:
                    c[s[end]] += 1
                end += 1
            if c == ct and end - strt < min_win:
                min_win = end - strt
                min_win_idx = [strt, end]
            strt += 1
        return s[min_win_idx[0] : min_win_idx[1]]

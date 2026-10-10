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
        ################################
        strt, end = 0, 0
        window = {}
        matched_values = 0
        min_idx, min_len = [-1, -1], float("infinity")
        while end < len(s):
            ch = s[end]
            window[ch] = window.get(ch, 0) + 1

            if ch in ct and ct[ch] == window[ch]:
                matched_values += 1
            
            while matched_values == len(ct):
                if (end - strt + 1) < min_len:
                    min_len = end - strt + 1
                    min_idx = [strt, end]
                window[s[strt]] -= 1
                if s[strt] in ct and window[s[strt]] < ct[s[strt]]:
                    matched_values -= 1
                strt += 1
            end += 1
        strt, end = min_idx
        return s[strt : end + 1] if min_len != float("infinity") else ""

